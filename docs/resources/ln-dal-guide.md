---
title: "LN DAL 完全指南 - Infor 生态第三方资源导航站"
description: "Infor LN DAL（Data Access Layer）完全指南，涵盖 DAL1 vs DAL2 深度对比、所有 Hook 函数详解、执行顺序、错误码速查和加锁机制。"
---

# LN DAL 完全指南

> DAL（Data Access Layer）是 LN 的核心数据操作框架，封装了数据库操作并自动触发数据校验和业务规则。本指南基于 Infor LN 2604 官方编程指南编写。
>
> **前置阅读**：[LN 4GL 语言基础](ln-4gl-tips.md)
>
> **适用人群**：LN 开发者、二次开发工程师

---

## 📋 目录

- [一、DAL 概述](#一dal-概述)
- [二、DAL1 vs DAL2 对比](#二dal1-vs-dal2-对比)
- [三、DAL2 标准工作流](#三dal2-标准工作流)
- [四、DAL 函数速查表](#四dal-函数速查表)
- [五、Hook 完全解析](#五hook-完全解析)
- [六、Hook 执行顺序详解](#六hook-执行顺序详解)
- [七、字段级 Hook 详解](#七字段级-hook-详解)
- [八、字段依赖机制](#八字段依赖机制)
- [九、错误码与异常处理](#九错误码与异常处理)
- [十、加锁机制详解](#十加锁机制详解)
- [十一、DAL 上下文](#十一dal-上下文)
- [十二、常见问题与最佳实践](#十二常见问题与最佳实践)

---

## 一、DAL 概述

### 1.1 什么是 DAL

DAL（Data Access Layer，数据访问层）是 LN 中用于**集中管理数据完整性和业务规则**的框架。每个 LN 数据库表都有对应的 DAL 脚本。

### 1.2 DAL 的核心目标

| 目标 | 说明 |
|------|------|
| **集中数据校验** | 所有数据完整性检查统一在 DAL 中实现，避免在 UI 脚本中重复编写 |
| **可复用性** | 通过 ION/BOD 集成和 Service Tier 调用时，DAL 中的校验规则自动生效 |
| **字段联动** | 修改一个字段后，自动更新其依赖字段 |
| **UI 自动适配** | 4GL 引引擎根据 DAL Hook 自动控制字段的启用/禁用/只读状态 |

### 1.3 DAL 文件

| 文件类型 | 说明 |
|----------|------|
| `<table>_d.c` | DAL 脚本源文件（如 `twhinh215_d.c`） |
| `<table>_d` | 编译后的 DAL 对象 |
| `#include "bic_dal2"` | DAL2 必须包含的头文件 |

---

## 二、DAL1 vs DAL2 对比

| 特性 | DAL1 | DAL2（推荐） |
|------|------|-------------|
| **头文件** | `#include "bic_dam"` | `#include "bic_dal2"` |
| **新建** | `dal.new()` | `dal.new.object()` |
| **修改** | `dal.update()` | `dal.change.object()` + `dal.set.field()` + `dal.save.object()` |
| **删除** | `dal.delete()` | `dal.delete.object()` |
| **字段依赖** | 不支持 | 自动触发 `field.update()` |
| **Hook 完整性** | 部分触发 | 完整触发（含 `method.is.allowed()`、`field.is.*` 等） |
| **UI 交互** | 不支持 | 4GL 引擎自动读取 Hook 控制字段状态 |
| **性能** | 稍快（功能少） | 略慢（功能更全） |
| **字段属性** | `check.field()` | `field.is.applicable()`、`field.is.valid()` 等多个 Hook |
| **测试模式** | 不支持 | 支持 DAL2 Test Mode（3 种模式） |

> **原则**：新开发始终使用 DAL2。仅在确认 DAL 没有字段依赖且不涉及 UI 交互时可考虑 DAL1。

---

## 三、DAL2 标准工作流

### 3.1 新建记录（Insert）

```4gl
#include "bic_dam.h"

function long insert_record()
{
    long ret
    string dal.name(20)

    dal.name = "twhinh215"

    | Step 1: 开始新建
    ret = dal.new.object(dal.name)
    if ret <> 0 then
        message("dal.new.object failed: %d", ret)
        return(ret)
    endif

    | Step 2: 设置字段值
    dal.set.field("whinh215.item", "ITM000123")
    dal.set.field("whinh215.cwar", "WH001")
    dal.set.field("whinh215.locn", "A01")
    dal.set.field("whinh215.sqty", 100.0)

    | Step 3: 保存
    ret = dal.save.object(dal.name)
    if ret <> 0 then
        if ret = DALHOOKERROR then
            message("Hook blocked the save")
        elif ret = DALNOSETPERM then
            message("No table level permission")
        elif ret = DALNOOBJPERM then
            message("No record level permission")
        else
            message("DB error: %d", ret)
        endif
        return(ret)
    endif

    message("Record inserted")
    return(0)
}
```

### 3.2 修改记录（Update）

```4gl
function long update_record()
{
    long ret
    string dal.name(20)

    dal.name = "twhinh215"

    | Step 1: 加锁（重要！dal.change.object 不加锁）
    twhinh215.item = "ITM000123"
    twhinh215.cwar = "WH001"
    twhinh215.locn = "A01"
    ret = db.bind(twhinh215, db.FIND.BY.KEYS, db.LOCK)
    if ret <> 0 then
        if ret = db.error.DBRECORDLOCKED then
            message("Record is locked by another user")
        endif
        return(ret)
    endif

    | Step 2: 开始修改
    ret = dal.change.object(dal.name)
    if ret <> 0 then
        db.release(twhinh215)
        return(ret)
    endif

    | Step 3: 设置要修改的字段
    dal.set.field("whinh215.sqty", 200.0)

    | Step 4: 保存
    ret = dal.save.object(dal.name)
    db.release(twhinh215)    | 释放锁！

    return(ret)
}
```

### 3.3 删除记录（Delete）

```4gl
function long delete_record()
{
    long ret
    string dal.name(20)

    dal.name = "twhinh215"

    ret = dal.delete.object(dal.name)
    if ret <> 0 then
        message("Delete failed: %d", ret)
        return(ret)
    endif

    message("Record deleted")
    return(0)
}
```

### 3.4 查找记录

```4gl
function long find_record()
{
    long ret
    string dal.name(20)

    dal.name = "twhinh215"

    | 设置主键值
    twhinh215.item = "ITM000123"
    twhinh215.cwar = "WH001"
    twhinh215.locn = "A01"

    ret = dal.find.object(dal.name)
    if ret = 0 then
        | 找到记录，可读取字段值
        message("Found: qty = %f", twhinh215.sqty)
    else
        message("Record not found")
    endif

    return(ret)
}
```

### 3.5 复制记录

```4gl
function long copy_record()
{
    long ret
    string dal.name(20)

    dal.name = "twhinh215"

    | 先查找源记录
    twhinh215.item = "ITM000123"
    twhinh215.cwar = "WH001"
    twhinh215.locn = "A01"
    ret = dal.find.object(dal.name)
    if ret <> 0 then
        return(ret)
    endif

    | 复制
    ret = dal.copy.object(dal.name)
    if ret <> 0 then
        return(ret)
    endif

    | 修改复制后的字段
    dal.set.field("whinh215.locn", "A02")
    dal.set.field("whinh215.sqty", 50.0)

    | 保存新记录
    ret = dal.save.object(dal.name)
    return(ret)
}
```

---

## 四、DAL 函数速查表

### 4.1 DAL2 函数（在 4GL Script 中调用）

| 函数 | 说明 | 返回值 |
|------|------|--------|
| `dal.new.object(dal.name)` | 开始新建记录 | 0=成功 |
| `dal.change.object(dal.name)` | 开始修改记录（**不加锁**） | 0=成功 |
| `dal.copy.object(dal.name)` | 复制当前记录 | 0=成功 |
| `dal.set.field("fld", val)` | 设置字段值 | — |
| `dal.get.field("fld", var)` | 读取字段值 | 0=成功 |
| `dal.save.object(dal.name)` | 保存记录（insert 或 update） | 0=成功 |
| `dal.delete.object(dal.name)` | 删除记录 | 0=成功 |
| `dal.find.object(dal.name)` | 查找记录 | 0=找到 |
| `dal.destroy.object(dal.name)` | 销毁 DAL 对象 | 0=成功 |

### 4.2 DAL1 函数（兼容旧代码）

| 函数 | 说明 |
|------|------|
| `dal.new()` | DAL1 插入 |
| `dal.update(flag)` | DAL1 更新（`db.UPDATE.NORMAL` / `db.UPDATE.WITHOUT.RECURSION`） |
| `dal.delete()` | DAL1 删除 |
| `dal.find(flag)` | DAL1 查找 |

### 4.3 DAL Hook 中的辅助函数

| 函数 | 说明 |
|------|------|
| `dal.require.field("fld")` | 标记字段为必填（仅提示，不阻止保存） |
| `dal.field.depends.on("parent", "child")` | 声明字段依赖关系 |
| `dal.any.parent.changed()` | 检查是否有任何父字段被修改 |

---

## 五、Hook 完全解析

### 5.1 对象级 Hook（Object Hooks）

| Hook | 触发时机 | 用途 |
|------|----------|------|
| `before.new.object()` | `dal.new.object()` 之后，字段设置之前 | 设置默认值 |
| `after.new.object()` | 新建完成后 | 记录日志、触发后续操作 |
| `before.change.object()` | `dal.change.object()` 之后，字段修改之前 | 校验是否允许修改 |
| `after.change.object()` | 修改完成后 | 记录日志 |
| `before.destroy.object()` | `dal.delete.object()` 之后，实际删除之前 | 检查是否允许删除 |
| `after.destroy.object()` | 删除完成后 | 清理关联数据 |
| `before.get.object()` | `dal.find.object()` 之后 | 过滤查找结果 |
| `after.get.object()` | 查找完成后 | 补充数据 |
| `before.save.object()` | 实际数据库操作之前 | 最终校验 |
| `after.save.object()` | 实际数据库操作之后 | 联动更新、通知 |
| `set.object.defaults()` | 设置对象默认值 | 初始化默认值 |

### 5.2 业务方法 Hook（Business Method Hooks）

| Hook | 说明 |
|------|------|
| `method.is.allowed()` | 控制哪些业务方法可执行（如 Insert/Update/Delete） |
| `business.method.is.allowed()` | 同上，更细粒度控制 |

### 5.3 属性 Hook（Property Hooks）

| Hook | 说明 |
|------|------|
| `check.all.props()` | 检查所有属性 |
| `check.prop.<prop>()` | 检查指定属性 |

### 5.4 事务 Hook

| Hook | 触发时机 |
|------|----------|
| `before.commit.transaction()` | 事务提交之前 |
| `after.commit.transaction()` | 事务提交之后 |
| `after.abort.transaction()` | 事务回滚之后 |

### 5.5 审批 Hook

| Hook | 触发时机 |
|------|----------|
| `on.submit()` | 提交审批时 |
| `on.approve()` / `on.set.approved()` | 审批通过时 |
| `on.reject()` | 审批驳回时 |
| `on.recall()` / `on.set.recalled()` | 撤回审批时 |
| `on.set.draft()` | 设为草稿时 |

---

## 六、Hook 执行顺序详解

### 6.1 `dal.save.object()` 完整执行流程

```
dal.save.object() 调用后：

  1. 检查表级权限（Table Level Permission）
       ↓
  2. 对每个已设置字段执行 dal.validate.field()
     ├── field.is.never.applicable()
     ├── field.is.applicable()
     ├── field.is.readonly()（仅 UPDATE 模式）
     ├── field.is.derived()
     ├── field.is.mandatory()
     ├── field.is.valid()（非枚举字段）或
     │  field.enum.is.applicable() / field.enum.is.never.applicable()（枚举字段）
     └── fieldname.make.valid()
       ↓
  3. 触发依赖字段的 field.update()
     └── 递归触发依赖链上的所有 field.update()
       ↓
  4. 检查记录级权限（Record Level Permission）
       ↓
  5. 触发 method.is.allowed()
       ↓
  6. 触发字段级 Hooks
       ↓
  7. 触发 before.save.object()
       ↓
  8. 执行实际数据库操作
     ├── INSERT（新建模式）
     └── UPDATE（修改模式）
       ↓
  9. 触发 after.save.object()
       ↓
 10. 触发 after.commit.transaction() 或 after.abort.transaction()
```

### 6.2 `dal.delete.object()` 执行流程

```
dal.delete.object() 调用后：

  1. 检查表级权限
       ↓
  2. 触发 method.is.allowed()
       ↓
  3. 触发 before.destroy.object()
       ↓
  4. 执行实际 DELETE
       ↓
  5. 触发 after.destroy.object()
```

---

## 七、字段级 Hook 详解

### 7.1 字段验证 Hook

| Hook | 作用 | 返回值 |
|------|------|--------|
| `field.is.never.applicable()` | 字段永远不可用（任何情况下隐藏/禁用） | `true`=不可用 |
| `field.is.applicable()` | 字段在当前上下文中是否可用 | `true`=可用 |
| `field.is.readonly()` | 字段在修改模式下是否只读 | `true`=只读 |
| `field.is.derived()` | 字段值是否由系统计算（不可手动编辑） | `true`=派生 |
| `field.is.mandatory()` | 字段是否为必填 | `true`=必填 |
| `field.is.valid()` | 字段值是否合法（非枚举字段） | `true`=合法 |

### 7.2 枚举字段专用 Hook

| Hook | 作用 |
|------|------|
| `field.enum.is.applicable(enum.value)` | 指定枚举值是否可选 |
| `field.enum.is.never.applicable(enum.value)` | 指定枚举值是否永远不可选 |

### 7.3 字段值操作 Hook

| Hook | 触发时机 |
|------|----------|
| `fieldname.make.valid()` | 字段值被设置后，用于格式化/校验/四舍五入 |
| `fieldname.check()` | 字段值校验（旧版，DAL2 推荐用 `field.is.valid()`） |
| `fieldname.set.defaults()` | 设置字段默认值 |
| `field.update()` | 字段值修改后触发，用于更新依赖字段 |

### 7.4 字段验证完整流程（伪代码）

```
dal.validate.field(mode):
    if 字段为空 then
        if not field.is.never.applicable() and field.is.applicable() then
            if mode = DAL_UPDATE and field.is.readonly() then
                return(DALHOOKERROR)
            if field.is.derived() then
                return(DALHOOKERROR)
            if field.is.mandatory() then
                return(DALHOOKERROR)
        endif
    else
        if 是枚举字段 then
            if field.is.never.applicable() then
                return(DALHOOKERROR)
            if not field.is.applicable() then
                return(DALHOOKERROR)
            if not field.enum.is.applicable(value) then
                return(DALHOOKERROR)
            if not field.enum.is.never.applicable(value) then
                return(DALHOOKERROR)
        else
            if not field.is.valid() then
                return(DALHOOKERROR)
        endif
    endif
    return(0)
```

### 7.5 UI 字段状态自动推导

```
dal.get.field.state(mode):
    if not field.is.applicable() then
        return(DISABLED)         | 字段禁用
    if (mode = DAL_UPDATE and field.is.readonly()) or field.is.derived() then
        return(READONLY)         | 字段只读
    return(ENABLED)              | 字段可编辑
```

> **关键**：4GL 引擎自动读取上述 Hook 来控制 UI 字段状态，无需在 UI 脚本中手动设置 `attr.input=false`。

---

## 八、字段依赖机制

### 8.1 什么是字段依赖

字段依赖定义了字段间的联动关系：当父字段值改变时，自动重新计算和校验子字段。

### 8.2 声明字段依赖

```4gl
declaration:
    table twhinh215

before.program:
    | 声明：当 item 改变时，自动更新 cwrs
    dal.field.depends.on("whinh215.item", "whinh215.cwar")
    | 声明：当 item 改变时，自动更新 description
    dal.field.depends.on("whinh215.item", "whinh215.dsca")
```

### 8.3 字段更新流程

```
父字段 "whinh215.item" 被修改
    ↓
dal.set.field("whinh215.item", new_value)
    ↓
dal.save.object() 时自动：
    1. 执行 whinh215.item.make.valid()    | 校验 item 值
    2. 执行 whinh215.item.update()        | item 的 field.update() Hook
    3. 检查依赖关系 → 发现 whinh215.cwar 依赖 item
    4. 自动重新执行 whinh215.cwar 的更新流程：
       ├── whinh215.cwar.make.valid()
       ├── whinh215.cwar.update()
       └── 递归处理 whinh215.cwar 的依赖字段
```

### 8.4 在 field.update() 中实现联动逻辑

```4gl
| 当 item 改变时，自动清空并重新填充仓库字段
whinh215.item.update():
    | item 改变了，清空仓库并设置默认值
    if dal.any.parent.changed() then
        dal.set.field("whinh215.cwar", "")   | 清空
        | 根据新 item 设置默认仓库
        select twhinh200.cwar
        from twhinh200
        where twhinh200.item = :whinh215.item
        and   twhinh200.defa = tcyesno.yes
        as set with 1 rows
        selectdo
            dal.set.field("whinh215.cwar", twhinh200.cwar)
        endselect
    endif
```

---

## 九、错误码与异常处理

### 9.1 `dal.save.object()` 返回值

| 返回值 | 常量 | 含义 | 处理建议 |
|--------|------|------|----------|
| `0` | — | 保存成功 | 清理异常 `Exception.Delete(exception.id)` |
| `DALHOOKERROR` | — | Hook 函数返回错误 | 检查 `before.save.object()`、`field.is.valid()` 等 Hook 逻辑 |
| `DALDBERROR` | — | 域或引用错误（Integration 上下文） | 检查字段引用完整性 |
| `DALNOSETPERM` | — | 无表级权限 | 检查用户权限配置 |
| `DALNOOBJPERM` | — | 无记录级权限 | 检查记录级授权规则 |
| `> 0` | — | `db.insert()` 或 `db.update()` 的错误码 | 检查字段约束、唯一键、外键引用 |

> ⚠️ **注意**：官方文档**未列出** `-1` 作为 `dal.save.object()` 的返回值。如果收到 `-1`，应检查：① `dal.change.object()` 或 `dal.new.object()` 的返回值；② DAL 对象名称是否正确；③ DAL 是否已正确初始化。

### 9.2 `db.bind()` 错误码

| 返回值 | 常量 | 含义 |
|--------|------|------|
| `0` | — | 成功 |
| `db.error.DBRECORDLOCKED` | — | 记录被其他用户锁定 |
| `db.error.DBNOTFOUND` | — | 记录不存在 |
| `db.error.DBERROR` | — | 其他数据库错误 |

### 9.3 标准异常处理模板

```4gl
| 公共接口调用标准模板
long ret
domain tcmcs.s999m oMsg mb
long oID

ret = SomePublicInterface( ..., oMsg, oID )
if ret = 0 then
    Exception.Delete(exception.id)
else
    Exception.GetMessage( oID, 1, oMsg )
    message( "错误: " & oMsg )
    raise error
endif
```

### 9.4 异常处理函数

| 函数 | 说明 |
|------|------|
| `Exception.Delete(id)` | 删除异常（成功时调用） |
| `Exception.GetMessage(id, seq, msg)` | 获取异常消息（seq 从 1 开始） |
| `Exception.NumberOfMessages(id)` | 获取异常消息数量 |

---

## 十、加锁机制详解

### 10.1 为什么需要手动加锁

`dal.change.object()` **不会自动加锁**！多人同时修改同一记录会导致数据覆盖。

### 10.2 方式一：`db.bind()` 加锁（推荐）

```4gl
function long update_with_lock()
{
    long ret
    string dal.name(20)

    dal.name = "twhinh215"

    | 加锁
    twhinh215.item = "ITM000123"
    twhinh215.cwar = "WH001"
    twhinh215.locn = "A01"
    ret = db.bind(twhinh215, db.FIND.BY.KEYS, db.LOCK)
    if ret <> 0 then
        if ret = db.error.DBRECORDLOCKED then
            message("Record locked by another user")
        endif
        return(ret)
    endif

    | 修改
    ret = dal.change.object(dal.name)
    if ret <> 0 then
        db.release(twhinh215)
        return(ret)
    endif

    dal.set.field("whinh215.sqty", 200.0)

    | 保存
    ret = dal.save.object(dal.name)
    db.release(twhinh215)    | 始终释放！

    return(ret)
}
```

### 10.3 方式二：`SELECT FOR UPDATE`

```4gl
function long update_with_sql_lock()
{
    long ret

    select twhinh215.*
    from twhinh215 for update
    where twhinh215.item = :item
    selectdo
        twhinh215.sqty = twhinh215.sqty + 10.0
        update twhinh215
        commit.transaction()
    selectempty
        message("Record not found")
        return(-1)
    endselect

    return(0)
}
```

### 10.4 加锁对比

| 特性 | `db.bind()` | `SELECT FOR UPDATE` |
|------|-------------|---------------------|
| 事务范围 | 自动事务管理 | 需手动 `commit.transaction()` |
| 与 DAL 配合 | 完美配合 `dal.change.object()` | 直接操作数据库，绕过 DAL |
| 错误处理 | 返回 `DBRECORDLOCKED` | 需要检查 `db.error` |
| 推荐场景 | 通过 DAL 修改数据 | 批量 SQL 更新 |

> **最佳实践**：始终配对使用 `db.bind()` 和 `db.release()`，并在错误处理路径中确保释放锁。

---

## 十一、DAL 上下文

### 11.1 三种运行上下文

| 上下文 | 说明 |
|--------|------|
| **UI（Data Input）** | 通过 Session UI 操作，字段 Hook 和业务逻辑完整触发 |
| **DAL（Service Tier）** | 通过 Service Tier 调用，完整触发 |
| **Integration** | 通过 ION/BOD 集成调用，部分 Hook 可能不触发 |

### 11.2 上下文检测

```4gl
function check_context()
    long ctx
    ctx = dal.context()
    on case ctx
    case dal.ctx.ui:
        message("Running in UI context")
    case dal.ctx.dal:
        message("Running in DAL context")
    case dal.ctx.integration:
        message("Running in Integration context")
    endcase
endfunction
```

### 11.3 上下文对 Hook 的影响

| Hook | UI | DAL | Integration |
|------|:--:|:---:|:-----------:|
| `field.is.derived()` | ✅ | ✅ | ✅ |
| `field.update()` | ✅ | ✅ | ✅ |
| `field.is.valid()` | ✅ | ✅ | ✅ |
| UI 状态推导 | ✅ | ❌ | ❌ |

---

## 十二、常见问题与最佳实践

### 12.1 最佳实践清单

| 规则 | 说明 |
|------|------|
| 始终使用 DAL2 | 除非确认无字段依赖且不需 UI 交互 |
| 始终检查返回值 | 不要忽略 `dal.save.object()` 的返回值 |
| 手动加锁 | `dal.change.object()` 不会加锁，并发场景必须手动加锁 |
| 始终释放锁 | `db.bind()` 后必须配对 `db.release()`，包括错误路径 |
| 使用常量名 | 不要硬编码错误码数字，使用 `DALHOOKERROR` 等常量 |
| 善用字段依赖 | 用 `dal.field.depends.on()` 替代 UI 的 `when.field.changes` |
| 正确清理异常 | 成功时 `Exception.Delete()`，失败时 `Exception.GetMessage()` |

### 12.2 常见错误排查

| 错误现象 | 可能原因 | 排查方向 |
|----------|----------|----------|
| `dal.save.object()` 返回 `DALHOOKERROR` | Hook 函数返回错误 | 检查 `before.save.object()` 和 `field.is.valid()` |
| `dal.change.object()` 返回错误 | DAL 无法打开记录 | 检查主键是否正确、记录是否存在 |
| 修改后字段值未更新 | 忘记调用 `dal.set.field()` | 确认使用 `dal.set.field()` 而非直接赋值 |
| 并发修改导致数据丢失 | 未加锁 | 添加 `db.bind()` 或 `SELECT FOR UPDATE` |
| 字段依赖未触发 | 依赖声明位置不对 | `dal.field.depends.on()` 应放在 `before.program` 中 |
| UI 字段状态不正确 | DAL2 Hook 未正确定义 | 检查 `field.is.applicable()` / `field.is.readonly()` |
| `DALNOSETPERM` | 无表级权限 | 检查用户权限配置（Session 授权） |
| `DALNOOBJPERM` | 无记录级权限 | 检查记录级授权规则 |

### 12.3 DAL1 迁移到 DAL2 检查清单

- [ ] 替换 `#include "bic_dam"` 为 `#include "bic_dal2"`
- [ ] 替换 `dal.new()` 为 `dal.new.object()` + `dal.set.field()` + `dal.save.object()`
- [ ] 替换 `dal.update()` 为 `dal.change.object()` + `dal.set.field()` + `dal.save.object()`
- [ ] 替换 `dal.delete()` 为 `dal.delete.object()`
- [ ] 检查是否有字段依赖需求，如有则添加 `dal.field.depends.on()`
- [ ] 添加完整的错误处理（返回值检查 + 异常清理）
- [ ] 添加并发锁处理（`db.bind()` + `db.release()`）

---

*最后更新：2026-05-08*

> 💡 本页内容由 **Infor LN 4GL 编程开发助手** Skill 输出，基于 Infor LN 2604 官方编程指南。如有错误或补充，欢迎通过 [GitHub Issue](https://github.com/cuiwenyuan/infor-ecosystem-open-resources/issues/new) 反馈！
