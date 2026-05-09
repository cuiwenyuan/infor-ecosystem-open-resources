---
title: "LN 二次开发实战集锦 - Infor 生态开放资源导航站"
description: "Infor LN 二次开发实战技巧集锦，涵盖 Session/Report 开发模板、常用内置函数速查表、SSRS 报表集成和 UI 定制技巧。"
---

# LN 二次开发实战集锦

> 本页汇集 LN 二次开发中的常见实战技巧和代码模板，涵盖 Session 开发、Report 开发、常用函数和 UI 定制。
>
> **前置阅读**：[LN 4GL 语言基础](ln-4gl-tips.md) | [LN DAL 完全指南](ln-dal-guide.md)

---

## 📋 目录

- [一、Session 开发模板](#一session-开发模板)
- [二、Report 开发模板](#二report-开发模板)
- [三、常用内置函数速查表](#三常用内置函数速查表)
- [四、字符串函数速查](#四字符串函数速查)
- [五、日期时间函数速查](#五日期时间函数速查)
- [六、数学函数速查](#六数学函数速查)
- [七、UI 定制技巧](#七ui-定制技巧)
- [八、SSRS 报表集成](#八ssrs-报表集成)
- [九、进程间通信](#九进程间通信)
- [十、常见开发场景](#十常见开发场景)

---

## 一、Session 开发模板

### 1.1 Session 类型

| 类型 | 代码 | 用途 | 说明 |
|------|------|------|------|
| 数据维护 | `maint.session` | 增删改查 | 带格子的主从结构 |
| 多记录 | `multi-occ.session` | 多记录列表 | 多行数据网格 |
| 单记录 | `single-occ.session` | 单记录编辑 | 表单式 |
| 对话框 | `dialog.session` | 参数输入 | 模态对话框 |
| 打印 | `print.session` | 报表打印 | 启动 Report |

### 1.2 标准模板（数据维护 Session）

```4gl
declaration:
    table twhinh215    | 主表
    table twhinh210    | 从表（header）

    | 外部变量
    extern domain tcitem g.item    | 全局变量（来自其他 Session）
    long g.total.qty

before.program:
    | 初始化
    g.total.qty = 0
    | 导入全局变量
    import("g.item", g.item)

after.program:
    | 清理
    g.total.qty = 0

| === 主表 Section ===
before.open.object.set:
    | 打开对象前设置默认值
    twhinh215.item = g.item

after.open.object.set:
    | 打开对象后
    | 可查询补充数据

before.close.object:
    | 关闭对象前
    | 可做最终校验

| === 从表 Section ===
form.1:
    | 表单级逻辑
    if twhinh215.item = "" then
        attr.input = false    | 禁用从表字段
    endif

field.twhinh215.item:
    when.field.changes:
        | 物料变更后联动
        twhinh215.cwar = ""
        twhinh215.sqty = 0

field.twhinh215.sqty:
    check.input:
        | 数量校验
        if twhinh215.sqty <= 0 then
            set.input.error("tddel00101")    | 引用错误消息
        endif

    after.input:
        | 输入后联动
        g.total.qty = 0
        select sum(twhinh215.sqty):g.total.qty
        from twhinh215
        where twhinh215.orno = :twhinh210.orno
        selectdo
        endselect
        display("g.total.qty")

| === 按钮处理 ===
choice.cont.process:
    on.choice:
        | 标准处理按钮
        execute(first.set)

choice.user.0:    | 自定义按钮
    on.choice:
        | 自定义逻辑
        my_custom_function()

| === 函数定义 ===
functions:
    function void my_custom_function()
        | ...
    endfunction
```

### 1.3 多记录 Session 特殊处理

```4gl
| 获取当前行号
long current.occ
current.occ = occ.num

| 获取总行数
long total.occ
total.occ = occ.max

| 标记行
mark.occurrence(current.occ)    | 标记当前行
unmark.occurrence(current.occ)  | 取消标记

| 遍历已标记行
for i = 1 to marked.occurrences
    get.occurrence(i)
    | 使用 marked 主表缓冲区中的数据
    message("Marked: %s %s", marked.item, marked.cwar)
endfor

| 在 UI 中刷新
refresh()

| 修改特定行
for i = 1 to occ.max
    get.occurrence(i)
    if twhinh215.sqty > 1000 then
        twhinh215.sqty = 1000
        modify.occurrence(i)
    endif
endfor
```

---

## 二、Report 开发模板

### 2.1 Report Section 顺序

```
before.program:       | 初始化变量
after.program:        | 清理资源
before.layout:        | 每页开始
after.layout:         | 每页结束
header.1:             | 表头
before.detail.1:      | 明细行前处理
detail.1:             | 明细行（每条数据）
after.detail.1:       | 明细行后处理
footer.1:             | 表尾
after.report:         | 报表末尾
```

### 2.2 标准 Report 模板

```4gl
declaration:
    table twhinh215
    long page.line.count
    long total.qty
    long total.lines
    domain tcamnt grand.total

before.program:
    page.line.count = 0
    total.qty = 0
    total.lines = 0
    grand.total = 0

| 从 Session 接收参数
| r.report.xxx 接收 Session 传递的变量

before.layout:
    | 每页开始时的逻辑
    page.line.count = 0

after.layout:
    | 每页结束时的逻辑（如页脚汇总）
    r.print.line("小计: " & str$(grand.total))

detail.1:
    before.section:
        | 检查是否需要分页
        if r.report.line.remaining() < 5 then
            r.send.new.page()
        endif

    after.section:
        | 累计统计
        total.qty = total.qty + twhinh215.sqty
        grand.total = grand.total + twhinh215.amnt(1)
        total.lines = total.lines + 1
        page.line.count = page.line.count + 1

header.1:
    before.section:
        | 表头输出前的处理

after.report:
    | 报表末尾输出汇总
    r.print.line("================================")
    r.print.line("总行数: " & str$(total.lines))
    r.print.line("总数量: " & str$(total.qty))
    r.print.line("总金额: " & str$(grand.total))
```

### 2.3 Report 与 Session 的数据传递

```4gl
| Session 中启动 Report
| 通过 form fields 传递参数
export("whinh215.item", whinh215.item)
export("whinh215.cwar", whinh215.cwar)

| Report 中接收参数
declaration:
    domain tcitem r.item
    domain tccwar r.cwar

before.program:
    import("whinh215.item", r.item)
    import("whinh215.cwar", r.cwar)
```

---

## 三、常用内置函数速查表

### 3.1 数据类型转换

| 函数 | 说明 | 示例 |
|------|------|------|
| `lval(s)` | 字符串转数值 | `lval("123")` → 123 |
| `str$(v)` | 数值转字符串 | `str$(123)` → "123" |
| `sprintf$(fmt, ...)` | 格式化字符串 | `sprintf$("%.2f", 123.456)` → "123.46" |
| `val(s)` | 字符串转 long | `val("100")` → 100 |
| `double.cvt(s)` | 字符串转 double | `double.cvt("123.45")` |
| `num.to.date(l)` | UTC 数值转日期 | `num.to.date(utc.num())` |
| `date.to.num(d)` | 日期转 UTC 数值 | `date.to.num(date.str.to.date("20260508"))` |

### 3.2 输入与消息

| 函数 | 说明 |
|------|------|
| `message(fmt, ...)` | 弹出消息框（最多 ~80 字符） |
| `put.var(name, fmt, ...)` | 输出到调试日志文件 |
| `append.var(name, fmt, ...)` | 追加到日志文件 |
| `ask.enum(desc, enumval, def)` | 弹出选择框 |
| `ask.enum.desc(desc, ...)  ` | 带描述的枚举选择 |
| `set.input.error(msg.code)` | 设置输入错误提示 |
| `set.synchronized.dialog(dialog)` | 设置同步对话框 |
| `curr.key()` | 获取当前 Session 的主键值 |

---

## 四、字符串函数速查

| 函数 | 说明 | 示例 |
|------|------|------|
| `len(s)` | 字符数 | `len("Hello")` → 5 |
| `byte.len(s)` | 字节数（多字节安全） | `byte.len("你好")` → 4 |
| `strip$(s)` | 去首尾空格 | `strip$("  hi  ")` → "hi" |
| `ltrim$(s)` | 去左空格 | |
| `rtrim$(s)` | 去右空格 | |
| `lower$(s)` | 转小写 | |
| `upper$(s)` | 转大写 | |
| `shiftl$(s, n)` | 左移 n 位 | |
| `shiftr$(s, n)` | 右移 n 位 | |
| `pos(s, sub)` | 查找子串位置 | `pos("Hello", "ll")` → 3 |
| `rpos(s, sub)` | 从右查找 | |
| `kw1(s)` | 提取第一个词 | |
| `edit$(s)` | 编辑字符串（替换/删除） | `edit$("aXbYc", "XY", "12")` → "a1b2c" |
| `s$(num, width)` | 数值转定宽字符串 | `s$(42, 6)` → "    42" |
| `sprintf$(fmt, ...)` | 格式化 | `sprintf$("%06d", 42)` → "000042" |
| `isspace(s)` | 是否全是空格 | |
| `isDigit(s)` | 是否全是数字 | |

---

## 五、日期时间函数速查

| 函数 | 说明 |
|------|------|
| `utc.num()` | 当前 UTC 时间戳 |
| `utc.date()` | 当前日期（long，格式 YYYYMMDD） |
| `utc.time()` | 当前时间（long，格式 HHMMSS） |
| `date.num()` | 当前日期数值 |
| `num.to.date(l)` | UTC 数值转日期字符串 |
| `date.to.num(d)` | 日期字符串转 UTC 数值 |
| `date.to.utc()` | 日期转 UTC |
| `num.to.date$(l)` | 数值转日期字符串 "YYYYMMDD" |
| `date.str.to.date(s)` | 日期字符串转日期类型 |
| `year(d)` | 取年份 |
| `month(d)` | 取月份 |
| `day(d)` | 取日期 |
| `week.day(d)` | 星期几（1=周一） |
| `date.add.days(d, n)` | 加减天数 |
| `date.add.weeks(d, n)` | 加减周数 |
| `date.add.months(d, n)` | 加减月数 |
| `date.add.years(d, n)` | 加减年数 |
| `diff.days(d1, d2)` | 两日期差（天） |
| `date.cpy(d)` | 复制日期 |

---

## 六、数学函数速查

| 函数 | 说明 |
|------|------|
| `abs(x)` | 绝对值 |
| `ceil(x)` | 向上取整 |
| `floor(x)` | 向下取整 |
| `round(x, n)` | 四舍五入（n 位小数） |
| `trunc(x)` | 截断小数 |
| `sqrt(x)` | 平方根 |
| `pow(x, y)` | x 的 y 次方 |
| `exp(x)` | e 的 x 次方 |
| `log(x)` | 自然对数 |
| `log10(x)` | 以 10 为底对数 |
| `max(x, y)` | 最大值 |
| `min(x, y)` | 最小值 |
| `mod(x, y)` | 取模 |
| `random(x)` | 随机数（0 ~ x-1） |
| `pi()` | 圆周率 |

---

## 七、UI 定制技巧

### 7.1 字段控制

```4gl
form.1:
    | 基于条件控制字段可用性
    if twhinh215.item = "" then
        attr.input = false    | 禁用输入
    else
        attr.input = true     | 启用输入
    endif
```

### 7.2 字段默认值

```4gl
| 方式一：在 before.open.object.set 中
before.open.object.set:
    twhinh215.sqty = 0
    twhinh215.stun = tcyesno.yes

| 方式二：在 when.field.changes 中联动
field.twhinh215.item:
    when.field.changes:
        | 物料改变后设置默认仓库
        select twhinh200.cwar
        from twhinh200
        where twhinh200.item = :twhinh215.item
        and   twhinh200.defa = tcyesno.yes
        as set with 1 rows
        selectdo
            twhinh215.cwar = twhinh200.cwar
        endselect
```

### 7.3 动态按钮

```4gl
| 隐藏/显示按钮
if some.condition then
    enable.commands("user.0")    | 启用自定义按钮
else
    disable.commands("user.0")   | 禁用自定义按钮
endif
```

### 7.4 导入/导出变量

```4gl
| 导出给其他 Session
export("my.var.name", some.value)

| 从其他 Session 导入
import("my.var.name", local.var)
```

---

## 八、SSRS 报表集成

### 8.1 LN 与 SSRS 集成方式

| 方式 | 说明 |
|------|------|
| **LN 原生报表** | 使用 LN Report Designer |
| **SSRS 集成** | 通过 Infor Reporting Services 调用 SSRS |
| **直接 SQL** | SSRS 直接查询 LN 数据库 |

### 8.2 SSRS 报表开发要点

| 要点 | 说明 |
|------|------|
| 数据源 | LN 数据库（SQL Server） |
| 存储过程 | 可调用 LN 存储过程获取数据 |
| 参数传递 | Session 导出参数，SSRS 接收 |
| 多语言 | 使用 LN 语言代码切换报表语言 |
| 部署 | 上传到 Infor Reporting Services |

---

## 九、进程间通信

### 9.1 启动其他 Session

```4gl
| 启动 Session（同步）
zoom.to$("tdsls4100m000", "", "")

| 启动 Session（异步）
start.session("tdsls4100m000", "", "")

| 启动 Session 并传递参数
zoom.to$("ticst0101m000", "whinh215.item", str$(whinh215.item))
```

### 9.2 调用外部程序

```4gl
| 执行 shell 命令
shell("notepad.exe", 0)

| 执行 4GL 函数
ret = run.prog("my.program", argv)
```

---

## 十、常见开发场景

### 10.1 自动生成编号

```4gl
| 使用 Common PI 生成编号
extern long Common.GenerateFirstFreeNumber(
    domain tccmp, domain tcser, ref domain tcser,
    ref domain tcmcs.s999m, ref long )

long ret
domain tcser new.number
domain tcmcs.s999m oMsg mb
long oID

ret = Common.GenerateFirstFreeNumber(
    575, "ORD", new.number, oMsg, oID )
if ret = 0 then
    Exception.Delete(exception.id)
    twhinh215.orno = new.number
endif
```

### 10.2 数据校验模板

```4gl
function boolean validate_order()
    boolean valid
    valid = true

    | 校验物料
    if twhinh215.item = "" then
        set.input.error("tccom00101")
        valid = false
    endif

    | 校验数量
    if twhinh215.sqty <= 0 then
        set.input.error("tddel00101")
        valid = false
    endif

    | 校验仓库
    if twhinh215.cwar = "" then
        set.input.error("twhinh20101")
        valid = false
    endif

    return(valid)
endfunction
```

### 10.3 复制记录模板

```4gl
function long copy_order(domain tcorno from.order, domain tcorno to.order)
    long ret
    string dal.name(20)
    table t_lines

    dal.name = "tdsls400"

    | 读取源订单
    tdsls400.orno = from.order
    ret = dal.find.object(dal.name)
    if ret <> 0 then
        return(ret)
    endif

    | 复制订单头
    ret = dal.copy.object(dal.name)
    if ret <> 0 then
        return(ret)
    endif

    | 修改目标订单号
    dal.set.field("tdsls400.orno", to.order)

    | 保存订单头
    ret = dal.save.object(dal.name)
    if ret <> 0 then
        return(ret)
    endif

    return(0)
endfunction
```

---

## 相关资源

| 资源 | 说明 |
|------|------|
| [LN 4GL 语言基础](ln-4gl-tips.md) | 语法和基础概念 |
| [LN DAL 完全指南](ln-dal-guide.md) | DAL 开发详解 |
| [LN Extension 开发实战](ln-extension-guide.md) | Extension 开发指南 |
| [LN Public Interfaces 速查](ln-pi-reference.md) | PI 函数列表 |
| [LN 数据库与性能调优](ln-performance.md) | 性能优化技巧 |

---

*最后更新：2026-05-08*

> 💡 本页内容由 **Infor LN 4GL 编程开发助手** Skill 输出，基于 Infor LN 2604 官方编程指南。如有错误或补充，欢迎通过 [GitHub Issue](https://github.com/cuiwenyuan/infor-ecosystem-open-resources/issues/new) 反馈！
