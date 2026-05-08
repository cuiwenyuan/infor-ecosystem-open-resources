---
title: "Infor LN 4GL 开发技巧 - Infor 生态第三方资源导航站"
description: "Infor LN 4GL/Baan 编程开发技巧汇总，涵盖 DAL2 开发、Extension 机制、Public Interfaces 调用、Session/Report 开发等实战经验。"
---

# Infor LN 4GL 开发技巧

> Infor LN 4GL（源自 Baan 4GL）是 Infor LN ERP 的核心编程语言。本页汇总实战开发技巧、最佳实践和常见陷阱，帮助开发者提升编码效率和代码质量。
>
> **适用人群**：Infor LN 开发者、实施顾问、二次开发工程师

---

## 📋 目录

- [一、4GL 语言基础](#一4gl-语言基础)
- [二、DAL 开发实战](#二dal-开发实战)
- [三、Extension 开发机制](#三extension-开发机制)
- [四、Public Interfaces 调用](#四public-interfaces-调用)
- [五、Session 开发技巧](#五session-开发技巧)
- [六、Report 开发技巧](#六report-开发技巧)
- [七、调试与排错](#七调试与排错)
- [八、性能优化](#八性能优化)
- [九、代码规范](#九代码规范)
- [十、学习资源](#十学习资源)

---

## 一、4GL 语言基础

### 1.1 数据类型（6 种核心类型）

| 类型 | 说明 | 示例 |
|------|------|------|
| `LONG` | 整数，32 位有符号 | `LONG i = 0` |
| `DOUBLE` | 浮点数，8 字节 IEEE 754 | `DOUBLE amount = 0.0` |
| `BOOLEAN` | 布尔值 | `BOOLEAN flag = TRUE` |
| `STRING` | 字符串（声明时指定长度） | `STRING name(30)` |
| `TABLE` | 表格变量（数组/临时表） | `TABLE t_temp` |
| `DOMAIN` | 域类型（引用数据字典） | `DOMAIN tcitem item_code` |

### 1.2 变量修饰符

```4gl
LONG g_counter                | 局部变量
EXTERN LONG g_counter          | 外部（全局）变量，可被其他程序访问
STATIC LONG last_value          | 静态变量，函数调用间保持值
CONST LONG max_retries = 3     | 常量
```

### 1.3 字符串操作

```4gl
| 拼接用 &（不是 +）
STRING result(60)
result = "Hello" & " " & "World"

| 获取长度
LONG char_count = strlen(s)          | 字符数
LONG byte_count = byte.len(s)        | 字节数（多字节安全）

| 截取子串
STRING sub = s(1;5)                   | 从第1位取5个字符

| 去空格
s = strip$(s)                         | 去首尾空格
s = ltrim$(s)                        | 去左空格
s = rtrim$(s)                        | 去右空格
```

> ⚠️ **常见陷阱**：字符串拼接用 `&`，不是 `+`。`+` 用于数值加法，对字符串会尝试隐式类型转换导致意外结果。

### 1.4 控制流

```4gl
| IF-THEN-ELSE
IF condition THEN
    | ...
ELSE
    | ...
ENDIF

| ON-CASE（推荐替代多层 IF-ELSE）
ON CASE variable
CASE 1:
    | ...
CASE 2, 3:    | 支持多值
    | ...
CASE DEFAULT:
    | ...
ENDCASE

| 循环
FOR i = 1 TO 10
    | ...
ENDFOR

WHILE condition
    | ...
ENDWHILE

REPEAT
    | ...
UNTIL condition
```

---

## 二、DAL 开发实战

### 2.1 DAL1 vs DAL2 对比

| 特性 | DAL1 | DAL2（推荐） |
|------|------|-------------|
| 新建 | `dal.new()` | `dal.new.object()` |
| 修改 | `dal.update()` | `dal.change.object()` + `dal.set.field()` + `dal.save.object()` |
| 删除 | `dal.delete()` | `dal.delete.object()` |
| 字段依赖 | ❌ 不支持 | ✅ 自动触发 |
| Hooks | 部分触发 | ✅ 完整触发 |
| 性能 | 稍快 | 略慢（功能更全） |

### 2.2 DAL2 标准工作流（Insert）

```4gl
#include "bic_dam.h"

FUNCTION LONG insert_record()
{
    LONG ret
    STRING dal.name(20)
    
    dal.name = "twhinh215"
    
    | Step 1: 开始新建
    ret = dal.new.object(dal.name)
    IF ret <> 0 THEN
        message("dal.new.object failed: %d", ret)
        RETURN ret
    ENDIF
    
    | Step 2: 设置字段
    dal.set.field("whinh215.item", "ITM000123")
    dal.set.field("whinh215.cwar", "WH001")
    dal.set.field("whinh215.sqty", 100.0)
    
    | Step 3: 保存
    ret = dal.save.object(dal.name)
    IF ret <> 0 THEN
        | 错误处理
        IF ret = DALHOOKERROR THEN
            message("Hook blocked the save")
        ENDIF
        RETURN ret
    ENDIF
    
    RETURN 0
}
```

### 2.3 DAL2 标准工作流（Update）

```4gl
FUNCTION LONG update_record()
{
    LONG ret
    STRING dal.name(20)
    
    dal.name = "twhinh215"
    
    | Step 1: 加锁（重要！）
    twhinh215.item = "ITM000123"
    twhinh215.cwar = "WH001"
    ret = db.bind(twhinh215, db.FIND.BY.KEYS, db.LOCK)
    IF ret <> 0 THEN
        IF ret = db.error.DBRECORDLOCKED THEN
            message("Record is locked by another user")
        ENDIF
        RETURN ret
    ENDIF
    
    | Step 2: 开始修改
    ret = dal.change.object(dal.name)
    IF ret <> 0 THEN
        db.release(twhinh215)
        RETURN ret
    ENDIF
    
    | Step 3: 设置要修改的字段
    dal.set.field("whinh215.sqty", 200.0)
    
    | Step 4: 保存
    ret = dal.save.object(dal.name)
    db.release(twhinh215)    | 别忘了释放锁！
    
    RETURN ret
}
```

### 2.4 `dal.save.object()` 返回值速查

| 返回值 | 含义 | 处理建议 |
|--------|------|----------|
| `0` | 成功 | 清理异常 |
| `DALHOOKERROR` | Hook 阻止了保存 | 检查 Hook 逻辑 |
| `DALNOSETPERM` | 无表级权限 | 检查用户权限配置 |
| `DALNOOBJPERM` | 无记录级权限 | 检查记录级授权 |
| `> 0` | 数据库错误 | 检查字段约束和引用完整性 |

> ⚠️ **关键陷阱**：`dal.change.object()` **不会加锁**！多人并发修改同一记录时必须手动加锁（用 `db.bind()` 或 `SELECT FOR UPDATE`）。

### 2.5 DAL Hook 执行顺序

```
dal.save.object() 触发顺序：
1. 检查表级权限
2. 对每个已设置字段：fieldname.make.valid()
3. 触发依赖字段的 field.update()
4. 检查记录级权限
5. 触发 method.is.allowed()
6. 触发字段级 Hooks
7. 触发 before.save.object()
8. 执行实际保存（INSERT 或 UPDATE）
9. 触发 after.save.object()
```

---

## 三、Extension 开发机制

### 3.1 为什么用 Extension

| 方式 | 升级影响 | 维护难度 | 推荐度 |
|------|---------|---------|--------|
| 直接修改标准 Script | ❌ 升级覆盖 | 高 | ❌ 不推荐 |
| User Exit（UE） | ⚠️ 部分保留 | 中 | ⚠️ 旧方案 |
| **Extension** | ✅ 不受影响 | 低 | ✅ **推荐** |

### 3.2 Extension 类型

| 类型 | 执行时机 | 用途 |
|------|---------|------|
| Before DAL | DAL 操作之前 | 字段校验、默认值 |
| After DAL | DAL 操作之后 | 联动更新其他表 |
| Before Logic | 标准逻辑之前 | 拦截/修改输入 |
| After Logic | 标准逻辑之后 | 补充处理 |

### 3.3 Extension 开发模板

```4gl
| Extension DLL: tdslsdllcustom
| 扩展点: After Save Sales Order Line

declaration:
    | 声明外部变量和函数

before.program:
    | 初始化逻辑（可选）

after.save.object:
    | 在 after.save.object Hook 中处理
    IF action = DAL_NEW THEN
        | 新建后逻辑
    ELIF action = DAL_UPDATE THEN
        | 修改后逻辑
    ENDIF
```

---

## 四、Public Interfaces 调用

### 4.1 什么是 Public Interfaces

Public Interfaces 是 LN 提供的标准业务功能方法，可在 Extension 中调用，实现标准功能的复用，**升级不受影响**。

### 4.2 常用 Public Interfaces

#### Common 模块

| 函数 | 说明 |
|------|------|
| `Common.ConvertAmount()` | 货币金额转换 |
| `Common.ConvertQuantity()` | 数量单位转换 |
| `Common.RoundAmount()` | 金额四舍五入 |
| `Common.GenerateFirstFreeNumber()` | 生成首个自由编号 |
| `Common.ConvertAmountToWords()` | 金额转文字 |

#### BusinessPartner 模块

| 函数 | 说明 |
|------|------|
| `BusinessPartner.GetGeneralData()` | 获取业务伙伴通用数据 |
| `BusinessPartner.GetShipToData()` | 获取送达方数据 |
| `BusinessPartner.GetPayByData()` | 获取付款方数据 |

#### Sales 模块

| 函数 | 说明 |
|------|------|
| `Sales.GetOrderSettings()` | 获取销售订单设置 |
| `Sales.CalculatePlannedDeliveryDate()` | 计算计划交货日期 |
| `SalesOrder.CreditCheck()` | 信用检查 |

### 4.3 调用语法模板

```4gl
| 声明函数原型
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

| 调用并处理异常
long ret
domain tcmcs.s999m oMsg mb
long oID

ret = Common.ConvertAmount( 575, amount, "USD", 1, date.to.utc(), "EUR", converted.amount, oMsg, oID )
IF ret = 0 THEN
    Exception.Delete(exception.id)
ELSE
    Exception.GetMessage( oID, 1, oMsg )
    message( "金额转换失败: " & oMsg )
    RAISE error
ENDIF
```

---

## 五、Session 开发技巧

### 5.1 Session 类型

| 类型 | 用途 | 说明 |
|------|------|------|
| `maint.session` | 数据维护 | 增删改查 |
| `multi-occ.session` | 多记录列表 | 带格子的主从结构 |
| `single-occ.session` | 单记录编辑 | 表单式 |
| `dialog.session` | 对话框 | 参数输入 |
| `print.session` | 报表打印 | 启动 Report |

### 5.2 常用 Section 顺序

```
declaration:        | 变量声明
before.program:     | 初始化
after.program:      | 清理
before.open.object: | 打开对象前
after.open.object:  | 打开对象后
before.close.object:| 关闭对象前
form.1:             | 表单逻辑
field.1:            | 字段级逻辑（when.field.changes 等）
choice.cont.process:| 按钮点击
```

---

## 六、Report 开发技巧

### 6.1 Report Section 顺序

```
before.program:     | 初始化变量
after.program:      | 清理资源
before.layout:      | 每页开始
after.layout:       | 每页结束
detail.1:           | 明细行（每条数据）
after.detail.1:     | 明细行后处理
header.1:           | 表头
footer.1:           | 表尾
```

### 6.2 报表分页技巧

```4gl
detail.1:
    BEFORE.SECTION:
        | 检查剩余行数，不足则分页
        IF r.report.line.remaining() < 5 THEN
            r.send.new.page()
        ENDIF
    AFTER.SECTION:
        | 每行后递增计数器
        line.count = line.count + 1
```

---

## 七、调试与排错

### 7.1 调试方法

| 方法 | 说明 |
|------|------|
| `message()` | 弹出消息框（最常用） |
| `put.var()` | 输出到调试日志 |
| `append.var()` | 追加到变量 |
| `sleep()` | 暂停执行（调试时用） |
| LN Debug 工具 | LN 自带的调试器 |

### 7.2 常见错误及解决

| 错误 | 原因 | 解决方案 |
|------|------|----------|
| `dal.save.object()` 返回 `DALHOOKERROR` | Hook 函数阻止保存 | 检查 DAL Hook 逻辑 |
| `db.error.DBRECORDLOCKED` | 记录被其他用户锁定 | 等待或提示用户 |
| `DALNOSETPERM` | 无表级权限 | 检查用户权限配置 |
| 字符串拼接结果异常 | 用了 `+` 而非 `&` | 改用 `&` 拼接 |
| `db.bind()` 找不到记录 | 主键值不正确 | 检查主键值 |

### 7.3 异常处理标准模板

```4gl
ret = SomePublicInterface( ..., oMsg, oID )
IF ret = 0 THEN
    Exception.Delete(exception.id)
ELSE
    Exception.GetMessage( oID, 1, oMsg )
    message( "错误: " & oMsg )
    RAISE error
ENDIF
```

---

## 八、性能优化

### 8.1 SQL 优化

```4gl
| ❌ 不推荐：逐行查询
SELECT twhinh215.*
FROM twhinh215
WHERE twhinh215.item = :item
SELECTDO
    | 逐行处理
ENDSELECT

| ✅ 推荐：批量处理
TABLE t_temp
SELECT twhinh215.item, twhinh215.cwar, SUM(twhinh215.sqty):total
FROM twhinh215
WHERE twhinh215.item = :item
GROUP BY twhinh215.item, twhinh215.cwar
HAVING SUM(twhinh215.sqty) > 0
SELECTDO
    | 批量处理
ENDSELECT
```

### 8.2 避免常见性能陷阱

| 陷阱 | 说明 | 建议 |
|------|------|------|
| 循环内 SELECT | 每次查询都访问数据库 | 使用 TABLE 变量缓存 |
| 不使用索引 | WHERE 条件未命中索引 | 确保查询字段有索引 |
| 过多的 `message()` | 频繁弹窗影响性能 | 调试后删除 |
| 未释放锁 | `db.bind()` 后忘记 `db.release()` | 始终配对使用 |

---

## 九、代码规范

### 9.1 命名约定

| 类型 | 约定 | 示例 |
|------|------|------|
| 函数 | 三个字母模块前缀 + 动词 | `tdsls.calculate.tax()` |
| 变量 | 小写 + 点号分隔 | `local.counter` |
| 常量 | 全大写 | `MAX_RETRY_COUNT` |
| DAL 对象 | 表名作为字符串 | `dal.name = "twhinh215"` |

### 9.2 注释规范

```4gl
| 4GL 使用 | 作为行注释符
| 函数说明写在函数定义之前
| 复杂逻辑添加内联注释
```

### 9.3 错误处理规范

```4gl
| ✅ 推荐：完整的错误处理
ret = dal.save.object(dal.name)
IF ret <> 0 THEN
    | 具体错误处理
    RETURN ret
ENDIF

| ❌ 不推荐：忽略返回值
dal.save.object(dal.name)
```

---

## 十、学习资源

### 官方资源

| 资源 | 说明 | 链接 |
|------|------|------|
| **Infor Documentation** | LN 官方文档（含 4GL 编程指南） | [docs.infor.com](https://docs.infor.com/) |
| **Infor U Campus** | 官方学习平台 | [eduportal.infor.com](https://eduportal.infor.com/) |
| **Public Interfaces 参考手册** | LN 10.8 PI & PE 参考指南 | [PDF](https://docs.infor.com/) |

### 第三方资源

| 资源 | 说明 | 链接 |
|------|------|------|
| **旺财学 Infor LN ERP** | 崔文远运营的中文技术公众号 | 微信搜索关注 |
| **FullOnBaan** | LN 技术知识库（英文） | [fullonbaan.com](https://fullonbaan.com/) |
| **CSDN Infor 标签** | 中文技术文章合集 | [搜索 "Infor LN"](https://blog.csdn.net/) |
| **知识星球** | 旺财学 Infor LN ERP 社群 | [加入](https://wx.zsxq.com/group/158585844512) |

### 在线社区

| 社区 | 说明 | 链接 |
|------|------|------|
| **Infor Community** | 官方社区（LN 开发板块） | [访问](https://www.infor.com/company/community) |
| **LinkedIn** | Infor 用户群组 | [搜索 "Infor LN"] |

---

*最后更新：2026-05-08*

> 💡 本页内容由 **Infor LN 4GL 编程开发助手** Skill 输出，基于 Infor LN 2604 官方编程指南和 Public Interfaces 参考手册。如有错误或补充，欢迎通过 [GitHub Issue](https://github.com/cuiwenyuan/infor-ecosystem-open-resources/issues/new) 反馈！
