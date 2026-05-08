---
title: "LN Extension 开发实战 - Infor 生态第三方资源导航站"
description: "Infor LN Extension 扩展开发实战指南，涵盖 4 种 Extension 类型、DLL 创建流程、调试技巧、与 User Exit 对比和冲突排查。"
---

# LN Extension 开发实战

> Extension 是 Infor LN 推荐的二次开发机制，通过独立的 Extension DLL 挂载自定义逻辑，**不修改标准代码**，升级时不受影响。本指南基于 Infor LN 2604 Design Principles 编写。
>
> **前置阅读**：[LN 4GL 语言基础](ln-4gl-tips.md) | [LN DAL 完全指南](ln-dal-guide.md)

---

## 📋 目录

- [一、Extension 机制概述](#一extension-机制概述)
- [二、Extension vs User Exit vs 直接修改](#二extension-vs-user-exit-vs-直接修改)
- [三、Extension 类型详解](#三extension-类型详解)
- [四、Extension DLL 创建流程](#四extension-dll-创建流程)
- [五、Hook 编写实战](#五hook-编写实战)
- [六、调用 Public Interfaces](#六调用-public-interfaces)
- [七、调试技巧](#七调试技巧)
- [八、多 Extension 冲突排查](#八多-extension-冲突排查)
- [九、Design Principles 设计原则](#九design-principles-设计原则)
- [十、常见问题与最佳实践](#十常见问题与最佳实践)

---

## 一、Extension 机制概述

### 1.1 什么是 Extension

Extension 是 LN 中的一种**独立 4GL 脚本（DLL）**，挂载到标准 Session 或 DAL 的特定扩展点上，在业务流程中自动触发执行。

### 1.2 核心优势

| 优势 | 说明 |
|------|------|
| **升级安全** | 不修改标准代码，LN 版本升级时 Extension 自动保留 |
| **即插即用** | 可通过 LN 工具启用/禁用，无需重新编译标准程序 |
| **多扩展支持** | 同一扩展点可挂载多个 Extension，按优先级顺序执行 |
| **独立维护** | Extension 代码与标准代码分离，便于版本管理和问题排查 |
| **标准集成** | 可调用 Public Interfaces 复用 LN 标准功能 |

### 1.3 Extension 工作原理

```
标准程序（Session/DAL）
    ↓ 触发扩展点
Extension DLL #1（优先级 10）
    ↓
Extension DLL #2（优先级 20）
    ↓
Extension DLL #3（优先级 30）
    ↓
返回标准程序继续执行
```

---

## 二、Extension vs User Exit vs 直接修改

| 对比维度 | 直接修改标准 Script | User Exit（UE） | **Extension（推荐）** |
|----------|:------------------:|:---------------:|:--------------------:|
| 修改标准代码 | ✅ 是 | ❌ 否 | ❌ 否 |
| 升级影响 | ❌ 被覆盖 | ⚠️ 部分保留 | ✅ 完全保留 |
| 调试难度 | 高 | 中 | 低 |
| 功能覆盖 | 全部 | 预定义点 | 全部 |
| 多扩展支持 | ❌ | ❌ | ✅ |
| 启用/禁用 | 需改代码 | 需改代码 | 工具一键切换 |
| 版本兼容性 | 差 | 中 | 好 |
| **推荐度** | ❌ 不推荐 | ⚠️ 旧方案 | ✅ **推荐** |

> **迁移建议**：如果现有系统中有 User Exit 或直接修改的代码，建议在版本升级时逐步迁移到 Extension。

---

## 三、Extension 类型详解

### 3.1 四种 Extension 类型

| 类型 | 执行时机 | 典型用途 | 适用场景 |
|------|----------|----------|----------|
| **Before DAL** | DAL 操作（insert/update/delete）之前 | 字段校验、默认值设置、数据补全 | 需在数据保存前介入 |
| **After DAL** | DAL 操作之后 | 联动更新其他表、记录日志、发送通知 | 需在数据保存后处理 |
| **Before Logic** | 标准 UI 逻辑之前 | 拦截/修改输入参数、条件性阻止操作 | 需在标准逻辑执行前控制流程 |
| **After Logic** | 标准 UI 逻辑之后 | 补充处理、显示额外信息 | 需在标准逻辑执行后追加处理 |

### 3.2 类型选择指南

```
需要校验/修改数据？ ─── 是 ─── Before DAL
需要保存后联动？     ─── 是 ─── After DAL
需要控制 UI 流程？   ─── 是 ─── Before Logic
需要追加 UI 逻辑？   ─── 是 ─── After Logic
```

### 3.3 执行顺序

```
Session UI 操作
    ↓
Before Logic Extension
    ↓
标准 UI 逻辑（choice / field sections）
    ↓
After Logic Extension
    ↓
Before DAL Extension（如涉及 DAL 操作）
    ↓
DAL 执行（含 Hook 链）
    ↓
After DAL Extension
    ↓
事务提交
```

---

## 四、Extension DLL 创建流程

### 4.1 命名约定

| 项目 | 约定 |
|------|------|
| DLL 名称 | 标准格式为 `<module>dllcustom`（如 `tdslsdllcustom`） |
| 也可自定义 | `<prefix>dll<suffix>`（如 `myextdll001`） |

### 4.2 完整创建步骤

#### Step 1：创建 Extension DLL 源文件

```4gl
| Extension: ZSSO001
| 用途: 销售订单行保存后自动更新订单备注
| DLL: tdslsdllcustom
| 扩展点: After Save Sales Order Line (After DAL)

#include <bic_dam>

declaration:
    | 声明外部变量和函数原型
    extern long Common.ConvertAmount(
        domain tccmp, domain tcamnt, domain tcccur,
        domain tcrtyp, domain tcdate, domain tcccur,
        ref domain tcamnt, ref domain tcmcs.s999m, ref long )
    extern domain tcmcs.s999m oExcMsg mb
    extern long oExcID

    | 变量声明
    domain tcmcs.s999m remark.text
    long log.count

before.program:
    | 初始化
    log.count = 0

after.save.object:
    | 在 DAL after.save.object Hook 中处理
    if action = DAL_NEW then
        handle_new_line()
    elif action = DAL_UPDATE then
        handle_update_line()
    endif

| 自定义函数
functions:
    function void handle_new_line()
        | 新建行后的处理逻辑
        log.count = log.count + 1
        | 示例：记录日志
    endfunction

    function void handle_update_line()
        | 修改行后的处理逻辑
        | 检查数量变更
        if old.whinh215.sqty <> whinh215.sqty then
            | 数量变更，联动处理
        endif
    endfunction
```

#### Step 2：在 LN 开发工具中注册

1. 打开 LN Development 扩展管理工具
2. 创建新 Extension，指定 DLL 名称和扩展点
3. 设置优先级（数字越小优先级越高）
4. 启用 Extension

#### Step 3：编译和部署

1. 使用 `bic6.2` 或 LN Studio 编译
2. 将编译后的 `.dll6` / `.o` 文件部署到 `$BSE/lib` 目录
3. 重启 bshell 或重新加载

### 4.3 Extension 模板（通用）

```4gl
| ==================================================
| Extension: [名称]
| 用途: [描述]
| DLL: [DLL名称]
| 扩展点: [扩展点名称和类型]
| 作者: [作者]
| 日期: [日期]
| ==================================================

#include <bic_dam>

declaration:
    | 外部变量
    #pragma used dll [其他DLL]    | 引用其他 DLL
    extern long ...

    | 内部变量
    long ...

before.program:
    | 初始化（可选）
    ...

| === Before DAL Hooks ===
before.save.object:
    ...
before.new.object:
    ...
before.change.object:
    ...
before.destroy.object:
    ...

| === After DAL Hooks ===
after.save.object:
    if action = DAL_NEW then
        ...
    elif action = DAL_UPDATE then
        ...
    endif
after.new.object:
    ...
after.destroy.object:
    ...

| === Field Hooks ===
whinh215.item.update:
    ...
whinh215.item.make.valid:
    ...

| === Before Logic ===
| (UI 逻辑相关 sections)
choice.cont.process:
    on.choice:
        ...

| === 自定义函数 ===
functions:
    function long my_function(...)
        ...
        return(0)
    endfunction
```

---

## 五、Hook 编写实战

### 5.1 After DAL Hook —— 保存后联动

**场景**：销售订单行保存后，自动更新订单头上的总备注。

```4gl
after.save.object:
    if action = DAL_NEW or action = DAL_UPDATE then
        | 检查金额是否超过阈值
        if tdsls401.amnt(1) > 100000 then
            | 调用公共接口记录大额订单备注
            update_order_remark(tdsls401.orno, "大额订单，金额: " & str$(tdsls401.amnt(1)))
        endif
    endif

functions:
    function void update_order_remark(domain tcorno i.order, string i.remark)
        long ret
        string dal.name(20)

        dal.name = "tdsls400"

        | 读取订单头
        tdsls400.orno = i.order
        ret = dal.find.object(dal.name)
        if ret <> 0 then
            return
        endif

        | 加锁 + 修改
        ret = db.bind(tdsls400, db.FIND.BY.KEYS, db.LOCK)
        if ret <> 0 then
            return
        endif

        ret = dal.change.object(dal.name)
        if ret <> 0 then
            db.release(tdsls400)
            return
        endif

        dal.set.field("tdsls400.rema", i.remark)
        ret = dal.save.object(dal.name)

        db.release(tdsls400)
    endfunction
```

### 5.2 Before DAL Hook —— 保存前校验

**场景**：保存采购订单行前，校验交货日期不能是过去。

```4gl
before.save.object:
    if action = DAL_NEW or action = DAL_UPDATE then
        if tdpur401.ddtb < utc.num() then
            | 交货日期在过去，阻止保存
            dal.set.error.message("tddel00101")  | 引用错误消息代码
        endif
    endif
```

### 5.3 Field Hook —— 字段联动

**场景**：当物料编码改变时，自动填充物料描述和默认仓库。

```4gl
tdsls401.item.update:
    if dal.any.parent.changed() then
        | 清空当前值
        dal.set.field("tdsls401.dsca", "")
        dal.set.field("tdsls401.cwar", "")

        | 查询物料信息
        select tccom001.dsca:desc, twhinh200.cwar:war
        from tccom001
        left outer join twhinh200 on twhinh200.item = tccom001.item
            and twhinh200.defa = tcyesno.yes
        where tccom001.item = :tdsls401.item
        as set with 1 rows
        selectdo
            dal.set.field("tdsls401.dsca", desc)
            dal.set.field("tdsls401.cwar", war)
        selectempty
            message("Item %s not found", tdsls401.item)
        endselect
    endif
```

---

## 六、调用 Public Interfaces

### 6.1 在 Extension 中调用 PI

```4gl
declaration:
    | 声明 PI 函数原型
    extern long Common.ConvertAmount(
        domain tccmp iFinancialCompany,
        domain tcamnt iSourceAmount,
        domain tcccur iSourceCurrency,
        domain tcrtyp iExchangeRateType,
        domain tcdate iRateDateUTC,
        domain tcccur iTargetCurrency,
        ref domain tcamnt oTargetAmount,
        ref domain tcmcs.s999m oExceptionMessage mb,
        ref long oExceptionID )

    extern long BusinessPartner.GetGeneralData(
        domain tccmp iFinancialCompany,
        domain tccom.bpid iBusinessPartner,
        domain tccwoc iDepartment,
        boolean iForceRead,
        ref domain tcmcs.s999m oExceptionMessage mb,
        ref long oExceptionID )

    | 异常处理变量
    extern domain tcmcs.s999m oExcMsg mb
    extern long oExcID

before.program:
    | 示例：在程序启动时获取业务伙伴信息
    long ret
    domain tcamnt converted.amount

    ret = Common.ConvertAmount(
        575,                           | 财务公司
        10000.00,                      | 源金额
        "USD",                         | 源币种
        1,                             | 汇率类型
        date.to.utc(),                 | 汇率日期
        "CNY",                         | 目标币种
        converted.amount,              | 输出：转换后金额
        oExcMsg, oExcID )              | 异常输出

    if ret = 0 then
        Exception.Delete(exception.id)
        message("转换结果: %.2f", converted.amount)
    else
        Exception.GetMessage(oExcID, 1, oExcMsg)
        message("PI 调用失败: " & oExcMsg)
    endif
```

### 6.2 PI 调用参数规则

| 参数类型 | 说明 | 示例 |
|----------|------|------|
| 固定输入 | 必须按顺序传递 | `domain tccmp iFinancialCompany` |
| 固定输出 | `ref` 引用传递 | `ref domain tcamnt oTargetAmount` |
| 可变输入 | `"字段名"`, `值` 成对传递 | `"cadr"`, l.tccom114.cadr` |
| 可变输出 | `"字段名"`, `变量` 成对传递 | `"ccnt"`, l.tccom114.ccnt` |

### 6.3 异常处理标准模式

```4gl
long ret
domain tcmcs.s999m oMsg mb
long oID

ret = SomePublicInterface( fixed_args..., oMsg, oID )
if ret = 0 then
    Exception.Delete(exception.id)    | 成功：清理异常
else
    Exception.GetMessage(oID, 1, oMsg)
    message("错误: " & oMsg)
    raise error                       | 失败：抛出错误
endif
```

> **更多 PI 函数速查**：参见 [LN Public Interfaces 速查](ln-pi-reference.md)

---

## 七、调试技巧

### 7.1 日志输出

```4gl
| 方法一：message() 弹窗（最简单，但会中断流程）
message("Debug: item = %s, qty = %f", tdsls401.item, tdsls401.amnt(1))

| 方法二：put.var() 输出到日志文件
put.var("my_extension_log", "before.save.object triggered for %s", tdsls401.item)

| 方法三：append.var() 追加到日志
append.var("my_extension_log", "step %d completed", step.counter)
```

### 7.2 条件断点

```4gl
| 只在特定订单号时触发调试信息
if tdsls401.orno = "SO000123" then
    message("Debug point reached, quantity = %f", tdsls401.amnt(1))
endif
```

### 7.3 使用 LN Debug 工具

| 步骤 | 操作 |
|------|------|
| 1 | 在 LN Development 中启用 Debug 模式 |
| 2 | 设置断点（在 Extension 源代码中标记） |
| 3 | 通过 Session 触发 Extension |
| 4 | 在 Debug 窗口中逐步执行和检查变量 |

### 7.4 DAL2 Test Mode

DAL2 提供三种测试模式，可在启动 bshell 时设置：

| 模式 | 说明 | 用途 |
|------|------|------|
| **Mode 1** | 仅执行 `field.is.*` Hook | 测试字段属性定义 |
| **Mode 2** | 执行所有 Hook，但不保存 | 测试 Hook 逻辑 |
| **Mode 3** | 完整执行（含保存） | 生产环境 |

---

## 八、多 Extension 冲突排查

### 8.1 冲突场景

| 场景 | 示例 |
|------|------|
| 两个 Extension 修改同一字段 | Extension A 设置 `dsca`，Extension B 也设置 `dsca`，后者覆盖前者 |
| 一个 Extension 阻止保存 | Extension A 返回 `DALHOOKERROR`，Extension B 的 After Logic 不会执行 |
| 执行顺序错误 | Extension B 依赖 Extension A 设置的值，但 B 优先级更高先执行 |

### 8.2 排查方法

```4gl
| 在每个 Extension 中加入标识信息
after.save.object:
    | 输出当前 Extension 的名称和优先级
    put.var("ext_debug", "[ZSSO001] after.save.object triggered, action = %d", action)
    ...
```

### 8.3 冲突预防原则

| 原则 | 说明 |
|------|------|
| **单一职责** | 每个 Extension 只负责一个功能点 |
| **优先级规划** | 基础功能 Extension 优先级高，增强功能优先级低 |
| **避免覆盖** | 不要修改其他 Extension 可能已经设置的字段 |
| **幂等设计** | Extension 的逻辑应该是幂等的（多次执行结果相同） |
| **文档记录** | 每个 Extension 记录：名称、扩展点、优先级、功能描述 |

### 8.4 优先级管理

| 优先级 | 范围 | 建议 |
|--------|------|------|
| 核心业务逻辑 | 1-100 | 最先执行 |
| 数据校验 | 101-200 | 在核心逻辑之后 |
| 联动更新 | 201-300 | 在校验之后 |
| 日志/通知 | 301-400 | 最后执行 |

---

## 九、Design Principles 设计原则

基于 Infor Design Principles 2024 版：

### 9.1 核心原则

| 原则 | 说明 |
|------|------|
| **不修改标准代码** | 所有定制逻辑通过 Extension 实现 |
| **数据完整性集中管理** | 校验规则放在 DAL 中，不放在 UI 脚本中 |
| **使用 Public Interfaces** | 调用标准功能而非重新实现 |
| **字段依赖代替 when.field.changes** | 用 DAL 字段依赖机制替代 UI 事件 |
| **幂等性** | Hook 逻辑应该是幂等的，避免副作用 |

### 9.2 Extension 设计原则

| 原则 | 说明 |
|------|------|
| 独立性 | Extension 不依赖特定 UI 状态 |
| 可测试性 | Extension 应能通过 DAL 测试框架独立测试 |
| 向后兼容 | Extension 不应假设标准 Hook 的执行顺序 |
| 最小权限 | Extension 只使用必要的权限和资源 |

---

## 十、常见问题与最佳实践

### 10.1 最佳实践清单

| # | 规则 | 说明 |
|---|------|------|
| 1 | 始终使用 Extension | 不直接修改标准 Script |
| 2 | 单一职责 | 一个 Extension 只做一件事 |
| 3 | 检查 action 值 | 在 `after.save.object` 中区分 `DAL_NEW` 和 `DAL_UPDATE` |
| 4 | 使用 PI | 调用 Public Interfaces 而非重新实现标准功能 |
| 5 | 处理异常 | PI 调用必须检查返回值并处理异常 |
| 6 | 日志记录 | 使用 `put.var()` 记录关键操作，便于排查 |
| 7 | 优先级规划 | 合理设置 Extension 优先级 |
| 8 | 文档化 | 每个 Extension 记录功能描述和依赖关系 |

### 10.2 常见错误排查

| 错误现象 | 可能原因 | 解决方案 |
|----------|----------|----------|
| Extension 未触发 | 未启用或扩展点不匹配 | 检查 Extension 注册状态和扩展点 |
| Extension 编译错误 | 函数原型声明不正确 | 检查 `extern` 声明与实际 PI 签名 |
| `dal.set.field()` 失败 | 未在 `new/chg` 上下文中调用 | 确认已调用 `dal.new.object()` 或 `dal.change.object()` |
| PI 调用返回异常 | 参数类型或值不正确 | 检查 Domain 类型和必填参数 |
| 字段联动不生效 | `dal.field.depends.on()` 位置不对 | 放在 `before.program` 中 |
| 多 Extension 结果异常 | 优先级冲突或字段覆盖 | 调整优先级，使用 `put.var()` 排查执行顺序 |

### 10.3 Extension 开发检查清单

- [ ] 确定扩展点类型（Before/After DAL/Logic）
- [ ] 确定扩展的 Session/DAL
- [ ] 创建 Extension DLL 源文件
- [ ] 编写 Hook 逻辑（区分 action 类型）
- [ ] 如需调用 PI，声明函数原型
- [ ] 实现完整的异常处理
- [ ] 添加调试日志（`put.var()`）
- [ ] 在 LN 开发工具中注册 Extension
- [ ] 设置合理的优先级
- [ ] 编译和部署
- [ ] 测试（正常流程 + 异常流程 + 并发场景）
- [ ] 编写文档（功能描述、依赖关系、配置说明）

---

## 相关资源

| 资源 | 说明 |
|------|------|
| [LN 4GL 语言基础](ln-4gl-tips.md) | 4GL 语法和基础概念 |
| [LN DAL 完全指南](ln-dal-guide.md) | DAL 开发和 Hook 详解 |
| [LN Public Interfaces 速查](ln-pi-reference.md) | PI 函数列表和调用模板 |
| [LN 数据库与性能调优](ln-performance.md) | SQL 优化和性能分析 |

---

*最后更新：2026-05-08*

> 💡 本页内容由 **Infor LN 4GL 编程开发助手** Skill 输出，基于 Infor LN 2604 官方编程指南和 Design Principles 2024。如有错误或补充，欢迎通过 [GitHub Issue](https://github.com/cuiwenyuan/infor-ecosystem-open-resources/issues/new) 反馈！
