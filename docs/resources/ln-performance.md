---
title: "LN 数据库与性能调优 - Infor 生态第三方资源导航站"
description: "Infor LN 数据库与性能调优指南，涵盖 SQL vs Table.io 对比、索引策略、db.bind 详解、批量操作技巧和常见慢查询模式。"
---

# LN 数据库与性能调优

> LN 支持两种数据访问方式：4GL SQL 和 Table.io（3GL）。本指南分析两者性能差异，提供索引策略、批量操作和常见性能陷阱的解决方案。
>
> **前置阅读**：[LN 4GL 语言基础](ln-4gl-tips.md) | [LN DAL 完全指南](ln-dal-guide.md)

---

## 📋 目录

- [一、数据访问方式对比](#一数据访问方式对比)
- [二、SQL 语句基础](#二sql-语句基础)
- [三、索引策略](#三索引策略)
- [四、Table.io 操作](#四tableio-操作)
- [五、db.bind 详解](#五dbbind-详解)
- [六、批量操作技巧](#六批量操作技巧)
- [七、常见慢查询模式](#七常见慢查询模式)
- [八、事务管理](#八事务管理)
- [九、DAL 操作性能](#九dal-操作性能)
- [十、性能诊断方法](#十性能诊断方法)

---

## 一、数据访问方式对比

| 特性 | 4GL SQL | Table.io (3GL) |
|------|---------|----------------|
| **语法** | `SELECT ... FROM ... WHERE` | `db.row(...)` / `db.next(...)` |
| **性能** | 通常更快（数据库优化） | 灵活但可能较慢 |
| **灵活性** | 支持 JOIN、GROUP BY、HAVING | 逐行操作，适合复杂逻辑 |
| **缓存** | 数据库缓存 | 应用层缓存 |
| **锁定** | `FOR UPDATE` | `db.LOCK` 参数 |
| **推荐场景** | 批量查询、报表、简单 CRUD | 逐行处理、复杂业务逻辑 |

> **原则**：优先使用 SQL 处理批量数据，Table.io 处理需要逐行判断的复杂逻辑。

---

## 二、SQL 语句基础

### 2.1 SELECT 查询

```4gl
| 基本查询
select twhinh215.item, twhinh215.cwar, twhinh215.sqty
from twhinh215
where twhinh215.item = :item
selectdo
    | 处理每条记录
endselect

| 带排序
select twhinh215.*
from twhinh215
where twhinh215.item = :item
order by twhinh215._index1
selectdo
    | ...
endselect

| 聚合查询
select twhinh215.item, sum(twhinh215.sqty):total.qty, count(*):line.count
from twhinh215
where twhinh215.item = :item
group by twhinh215.item
selectdo
    message("Item: %s, Total: %f, Lines: %d", twhinh215.item, total.qty, line.count)
endselect

| 限制结果行数
select twhinh215.*
from twhinh215
where twhinh215.item = :item
as set with 1 rows
selectdo
    | 只取第一条
endselect
```

### 2.2 INSERT / UPDATE / DELETE

```4gl
| 插入
insert into twhinh215 (item, cwar, sqty)
values (:item, :cwar, :qty)

| 更新
update twhinh215
set twhinh215.sqty = :qty
where twhinh215.item = :item
and   twhinh215.cwar = :cwar

| 删除
delete from twhinh215
where twhinh215.item = :item
and   twhinh215.cwar = :cwar
```

### 2.3 子查询

```4gl
| EXISTS 子查询
select twhinh215.*
from twhinh215
where twhinh215.item = :item
and   exists(
    select twhinh200.cwar
    from twhinh200
    where twhinh200.item = twhinh215.item )
selectdo
    | ...
endselect

| IN 子查询
select twhinh215.*
from twhinh215
where twhinh215.item in (
    select tccom001.item from tccom001
    where tccom001.kitm = tcyesno.yes )
selectdo
    | ...
endselect
```

---

## 三、索引策略

### 3.1 LN 索引类型

| 索引类型 | 说明 | 用途 |
|----------|------|------|
| **主键索引** (`_index1`) | 主键字段组合 | 精确查找 |
| **辅助索引** (`_index2` ~ `_indexN`) | 其他字段组合 | 特定查询场景 |
| **唯一索引** | 确保字段唯一性 | 数据完整性 |

### 3.2 索引使用原则

| # | 原则 | 说明 |
|---|------|------|
| 1 | WHERE 条件优先使用索引 | 确保查询字段有对应索引 |
| 2 | 使用 `as set with N rows` | 限制结果集大小 |
| 3 | 避免 `SELECT *` | 只查询需要的字段 |
| 4 | 利用 ORDER BY 索引 | 避免排序操作 |
| 5 | 使用 `hint` 指定索引（必要时） | `from twhinh215 hint twhinh215._index2` |

### 3.3 检查索引使用

```4gl
| 使用 ORDER BY 与索引一致，避免数据库排序
select twhinh215.*
from twhinh215
where twhinh215.item = :item
order by twhinh215._index1    | 与主键索引一致
selectdo
    | ...
endselect
```

> **注意**：LN 的 `_index1` 通常对应主键，`_index2` 及之后是辅助索引。可以在 LN 数据字典中查看表的索引定义。

---

## 四、Table.io 操作

### 4.1 基本操作

```4gl
| 读取记录
twhinh215.item = "ITM000123"
twhinh215.cwar = "WH001"
ret = db.row(twhinh215, db.FIND.BY.KEYS)
if ret = 0 then
    message("Qty: %f", twhinh215.sqty)
else
    message("Not found")
endif

| 逐行遍历
ret = db.first(twhinh215, db.FIND.BY.KEYS)
while ret = 0
    | 处理每条记录
    ret = db.next(twhinh215, db.FIND.BY.KEYS)
endwhile

| 写入记录
twhinh215.item = "ITM000123"
twhinh215.cwar = "WH001"
twhinh215.sqty = 100.0
ret = db.insert(twhinh215, db.RETURN.ALL)

| 更新记录
twhinh215.sqty = 200.0
ret = db.update(twhinh215, db.RETURN.ALL)

| 删除记录
ret = db.delete(twhinh215, db.RETURN.ALL)
```

### 4.2 Table.io vs SQL 选择指南

| 场景 | 推荐 | 原因 |
|------|------|------|
| 批量查询 | SQL | 数据库一次返回，减少网络往返 |
| 逐行复杂逻辑 | Table.io | 每行可做条件判断和分支 |
| 聚合统计 | SQL | `SUM`/`COUNT`/`AVG` 在数据库层计算 |
| 简单查找 | 两者皆可 | Table.io 代码更简洁 |
| 需要加锁 | Table.io | `db.LOCK` 参数 |
| 多表关联 | SQL | `JOIN` 更高效 |

---

## 五、db.bind 详解

### 5.1 db.bind() 用途

`db.bind()` 将数据库记录绑定到表缓冲区，支持锁定和并发控制。

### 5.2 基本用法

```4gl
| 只读绑定（不加锁）
twhinh215.item = "ITM000123"
twhinh215.cwar = "WH001"
ret = db.bind(twhinh215, db.FIND.BY.KEYS)
| ret = 0: 找到记录

| 读写绑定（加锁）
ret = db.bind(twhinh215, db.FIND.BY.KEYS, db.LOCK)
| ret = db.error.DBRECORDLOCKED: 记录被锁定

| 释放绑定
db.release(twhinh215)
```

### 5.3 db.bind() 与 DAL 配合

```4gl
function long update_via_dal()
{
    long ret
    string dal.name(20)

    dal.name = "twhinh215"

    | 1. db.bind 加锁
    twhinh215.item = "ITM000123"
    twhinh215.cwar = "WH001"
    ret = db.bind(twhinh215, db.FIND.BY.KEYS, db.LOCK)
    if ret <> 0 then
        if ret = db.error.DBRECORDLOCKED then
            message("Record locked")
        endif
        return(ret)
    endif

    | 2. dal.change.object 通知 DAL
    ret = dal.change.object(dal.name)
    if ret <> 0 then
        db.release(twhinh215)
        return(ret)
    endif

    | 3. 修改字段
    dal.set.field("whinh215.sqty", 200.0)

    | 4. 保存
    ret = dal.save.object(dal.name)

    | 5. 释放（始终执行）
    db.release(twhinh215)
    return(ret)
}
```

### 5.4 db.bind() 错误码

| 返回值 | 常量 | 含义 |
|--------|------|------|
| `0` | — | 成功 |
| `e` (非零) | `db.error.DBRECORDLOCKED` | 记录被锁定 |
| `e` (非零) | `db.error.DBNOTFOUND` | 记录不存在 |
| `e` (非零) | `db.error.DBERROR` | 数据库错误 |

---

## 六、批量操作技巧

### 6.1 批量处理 vs 逐行处理

```4gl
| 不推荐：循环内逐行查询（N+1 问题）
for i = 1 to item.count
    select twhinh215.sqty
    from twhinh215
    where twhinh215.item = :item.array(i)
    as set with 1 rows
    selectdo
        total = total + twhinh215.sqty
    endselect
endfor

| 推荐：一次查询 + TABLE 变量缓存
table t_temp
select twhinh215.item, twhinh215.sqty
from twhinh215
where twhinh215.item in (:item.array)
selectdo
    t_temp(1, t_temp.MAX + 1).item = twhinh215.item
    t_temp(1, t_temp.MAX + 1).sqty = twhinh215.sqty
endselect

| 遍历缓存结果
long i
for i = 1 to t_temp.MAX
    total = total + t_temp(i).sqty
endfor
```

### 6.2 使用 HAVING 和 WHERE 过滤

```4gl
| 不推荐：查询所有数据后在 4GL 中过滤
table t_temp
select twhinh215.item, sum(twhinh215.sqty):total
from twhinh215
group by twhinh215.item
selectdo
    if total > 100 then
        | 处理
    endif
endselect

| 推荐：在 SQL 中用 HAVING 过滤
select twhinh215.item, sum(twhinh215.sqty):total
from twhinh215
group by twhinh215.item
having sum(twhinh215.sqty) > 100
selectdo
    | 只处理符合条件的
endselect
```

### 6.3 使用 TABLE 变量减少数据库访问

```4gl
| 将常用配置数据加载到 TABLE 变量
table t_warehouse

| 程序启动时一次性加载
select twhinh200.cwar, twhinh200.dsca
from twhinh200
selectdo
    t_warehouse(1, t_warehouse.MAX + 1).cwar = twhinh200.cwar
    t_warehouse(1, t_warehouse.MAX + 1).dsca = twhinh200.dsca
endselect

| 后续直接从 TABLE 变量查找，无需再查数据库
```

---

## 七、常见慢查询模式

### 7.1 性能反模式清单

| # | 反模式 | 问题 | 解决方案 |
|---|--------|------|----------|
| 1 | 循环内 SELECT | N+1 查询，每次访问数据库 | 一次查询 + TABLE 变量缓存 |
| 2 | 不使用索引 | 全表扫描 | 确保 WHERE 条件命中索引 |
| 3 | SELECT * | 传输不必要的数据 | 只查询需要的字段 |
| 4 | 函数调用频繁 | `message()` 弹窗影响性能 | 调试后删除，改用 `put.var()` |
| 5 | 未释放锁 | `db.bind()` 后忘记释放 | 始终配对 `db.release()` |
| 6 | 大事务 | 长事务锁定过多记录 | 拆分为小事务 |
| 7 | 字符串拼接循环 | 反复创建字符串 | 使用 TABLE 变量或 `sprintf$()` |
| 8 | 嵌套循环查询 | O(N*M) 复杂度 | 使用 JOIN 或哈希映射 |

### 7.2 优化示例

```4gl
| 反模式：嵌套循环查询（O(N*M)）
for i = 1 to order.count
    for j = 1 to item.count
        select twhinh215.sqty
        from twhinh215
        where twhinh215.item = :item.array(j)
        and   twhinh215.orno = :order.array(i)
        as set with 1 rows
        selectdo
            | ...
        endselect
    endfor
endfor

| 优化：JOIN 一次查询（O(N+M)）
select tdsls401.item, tdsls401.amnt(1)
from tdsls401
where tdsls401.orno in (:order.array)
selectdo
    | 一次查询完成
endselect
```

---

## 八、事务管理

### 8.1 事务控制

```4gl
| 显式事务
commit.transaction()    | 提交当前事务
rollback.transaction() | 回滚当前事务

| 嵌套事务
long savepoint
savepoint = db.savepoint("my_savepoint")
| ... 操作 ...
if error then
    db.rollback.to(savepoint)
endif
```

### 8.2 事务原则

| 原则 | 说明 |
|------|------|
| 事务尽可能短 | 减少锁定时间 |
| 避免用户交互 | 不要在事务中弹 `message()` 等待用户确认 |
| 及时释放锁 | `db.bind()` + `db.release()` 配对 |
| 合理使用 `commit.transaction()` | 长批量操作分批提交 |

---

## 九、DAL 操作性能

### 9.1 DAL1 vs DAL2 性能

| 操作 | DAL1 | DAL2 | 说明 |
|------|------|------|------|
| 简单 Insert | 快 | 稍慢 | DAL2 触发完整 Hook 链 |
| 简单 Update | 快 | 稍慢 | 同上 |
| 带字段依赖 | 不支持 | 自动 | DAL2 胜出 |
| UI 联动 | 不支持 | 自动 | DAL2 胜出 |

### 9.2 优化 DAL 调用

| 技巧 | 说明 |
|------|------|
| 减少 `dal.set.field()` 次数 | 只设置需要修改的字段 |
| 批量操作用 SQL | 大量数据时直接 SQL 更快 |
| 避免 `dal.find.object()` | 不需要读取数据时直接操作主键 |
| 检查字段依赖链 | 避免级联触发过多的 `field.update()` |

---

## 十、性能诊断方法

### 10.1 调试日志

```4gl
| 记录执行时间
long start.time, end.time, elapsed

start.time = utc.num()
| ... 需要测量的操作 ...
end.time = utc.num()
elapsed = end.time - start.time

put.var("perf_log", "Operation took %d ms", elapsed * 1000)
```

### 10.2 SQL 执行计划

```4gl
| 在数据库端检查执行计划
| SQL Server: 使用 SQL Server Management Studio
| Oracle: 使用 EXPLAIN PLAN

| 在 LN 中使用 explain 功能
select twhinh215.*
from twhinh215
where twhinh215.item = :item
explain    | 查看执行计划
```

### 10.3 常用诊断工具

| 工具 | 用途 |
|------|------|
| `put.var()` / `append.var()` | 4GL 级别的调试日志 |
| SQL Server Profiler | 数据库级别的查询分析 |
| LN Audit / Log | LN 内置的审计日志 |
| bshell 调试模式 | 单步执行和变量检查 |

---

*最后更新：2026-05-08*

> 💡 本页内容由 **Infor LN 4GL 编程开发助手** Skill 输出，基于 Infor LN 2604 官方编程指南。如有错误或补充，欢迎通过 [GitHub Issue](https://github.com/cuiwenyuan/infor-ecosystem-open-resources/issues/new) 反馈！
