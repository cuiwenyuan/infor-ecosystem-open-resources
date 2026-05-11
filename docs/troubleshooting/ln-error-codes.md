---
title: "LN/Baan 错误代码 - 故障排查"
description: "Infor LN/Baan 常见错误代码速查，包括 1306、2050、RAISEERROR 等常见错误的解决方案。"
---

# Infor LN / Baan 错误代码

> LN/Baan 常见错误代码速查手册（社区贡献，仅供参考）。

---

## 常见错误代码索引

| 错误代码 | 严重度 | 简介 | 链接 |
|----------|--------|------|------|
| **1306** | ❌ 错误 | 记录被锁定（record is locked） | [查看](#1306) |
| **2050** | ❌ 错误 | 表或视图不存在 | [查看](#2050) |
| **1012** | ⚠️ 警告 | 记录不存在 | [查看](#1012) |
| **250** | ❌ 错误 | 意外错误（unexpected error） | [查看](#250) |
| **100** | ⚠️ 警告 | 通用错误 | [查看](#100) |
| **RAISERROR** | ❌ 错误 | DAL 错误处理 | [查看](#raiseerror) |

---

## 错误代码详解

### 1306 - Record is locked

**产品**：Infor LN / Baan IV / Baan V  
**严重度**：❌ 错误  
**描述**：尝试访问或锁定已被其他用户/进程锁定的记录。

**原因**：
- 其他用户正在编辑同一条记录
- 前一个事务未提交或回滚
- 程序异常退出导致锁未释放
- 死锁（deadlock）情况

**解决方案**：
1. 等待其他用户释放锁（通常 1-5 分钟）
2. 使用 `Close Sessions` 会话清理工具
3. 数据库层面：kill 锁定进程（需 DBA 协助）
4. 检查代码：确保 `dal.update()`, `dal.new()`, `dal.delete()` 后有 `dal.commit()` 或 `dal.rollback()` 

**代码示例（避免锁）**：
```4gl
dal.define.table({
  table: "tiitm001",
  lock: dal.LOCK.SHARED  | 使用共享锁，不是独占锁
})
dal.set.where("tiitm001._index1 = :item")
dal.select.do({
  on.NOTFOUND: | 记录不存在 |
  on.SUCCESS:
    | 尽快完成操作，释放锁
    dal.update.table("tiitm001", {...})
    dal.commit()  | 立即提交，释放锁
})
```

**参考**：
- [Infor LN 错误参考指南](https://docs.infor.com/ln/10.5/en-us/lnolh/help/tt/errors/overview.html)
- [Stack Overflow - Baan 1306 错误](https://stackoverflow.com/questions/tagged/baan)

---

### 2050 - Table or view does not exist

**产品**：Infor LN  
**严重度**：❌ 错误  
**描述**：DAL 操作中引用的表或视图在数据库中不存在。

**原因**：
- 表名拼写错误
- 表未在当前公司（company）中创建
- 缺少相应的许可（table not licensed）
- 数据库 schema 未同步

**解决方案**：
1. 检查表名拼写（区分大小写）
2. 使用 `Create Tables` 会话（tccma1215m000）创建表
3. 检查公司设置：`:c` 命令查看当前公司
4. 运行 `synchronize tables` 同步数据库 schema

**代码示例（安全访问）**：
```4gl
| 先检查表是否存在
if not dal.table.exists("tiitm001") then
  message.error("表 tiitm001 不存在，请先创建")
  retval = -1
  return(retval)
endif

dal.define.table({table: "tiitm001", lock: dal.LOCK.SHARED})
| ...
```

**参考**：
- [Infor LN Enterprise Server 错误消息](https://docs.infor.com/ln/10.5/en-us/lnolh/help/tt/errors/overview.html)

---

### 1012 - Record does not exist

**产品**：Infor LN / Baan  
**严重度**：⚠️ 警告  
**描述**：`dal.select.do` 或 `dal.get.first()` 未找到匹配记录。

**原因**：
- 表中没有匹配条件的记录
- `where` 条件过于严格
- 表中确实没有数据

**解决方案**：
1. 检查 `where` 条件是否正确
2. 使用 `on.NOTFOUND` 处理记录不存在的情况
3. 如果是必需记录，先创建再查询

**代码示例**：
```4gl
dal.define.table({table: "tiitm001", lock: dal.LOCK.SHARED})
dal.set.where("tiitm001._index1 = :item")
dal.select.do({
  on.NOTFOUND:
    message.warning("物料 " + item + " 不存在")
    retval = -1
  on.SUCCESS:
    | 处理记录
    retval = 0
})
return(retval)
```

---

### 250 - Unexpected error

**产品**：Infor LN / Baan  
**严重度**：❌ 错误  
**描述**：意外的系统错误，通常由底层系统问题引起。

**原因**：
- 数据库死锁
- 磁盘空间不足
- 内存不足
- 网络中断（远程数据库）

**解决方案**：
1. 检查数据库日志（通常位于 `$BSE/log/`）
2. 检查磁盘空间：`df -h`（Linux）或资源管理器（Windows）
3. 重启 LN 服务（需管理员权限）
4. 联系系统管理员

---

### RAISEERROR - DAL 错误处理

**产品**：Infor LN  
**严重度**：❌ 错误（可自定义）  
**描述**：DAL 函数中通过 `raise.error()` 主动抛出错误。

**原因**：
- 业务逻辑验证失败
- 数据完整性检查失败
- 自定义错误处理

**解决方案**：
1. 在调用 DAL 函数后检查返回值
2. 使用 `dal.get.error.message()` 获取错误信息
3. 在 UI 中显示友好的错误消息

**代码示例**：
```4gl
long result = dal.call.function("tiitm001.check.availability", item, qty)
if result != 0 then
  string err.msg = dal.get.error.message()
  message.error("库存检查失败：" + err.msg)
  return(-1)
endif
```

**参考**：
- [DAL 完全指南](../resources/ln-dal-guide.md)
- [Infor LN DAL2 开发详解](https://docs.infor.com/)

---

## 其他常见错误

| 错误代码 | 简介 | 常见原因 | 解决方案 |
|----------|------|----------|----------|
| **104** | 权限不足 | 用户没有表的读写权限 | 联系管理员分配权限 |
| **204** | 重复记录 | 唯一索引冲突 | 检查是否已存在相同记录 |
| **1001** | 字段值超出范围 | 数据长度/类型不匹配 | 检查输入数据格式 |
| **3201** | 公司不存在 | 指定的公司编号无效 | 使用 `:c` 查看可用公司 |

---

## 调试技巧

### 启用 4GL 调试日志

```bash
# 设置调试级别
export tt.DEBUG_LEVEL=5

# 运行程序，查看调试输出
${BSE}/bin/bnwrt -C "run.program:ttadv9999m000"
```

### 查看 LN 日志

```bash
# 应用日志
tail -f $BSE/log/ln.log

# 数据库日志
tail -f $BSE/log/db.log
```

---

## 贡献

欢迎提交更多 LN/Baan 错误代码和解决方案！请查看 [资源提交规范](../submission-guide.md)。

**最后更新**：2026-05-11
