---
title: "Extension 开发资源 - 开发者资源中心"
description: "Infor Extension 开发资源汇总，包括 XtendM3（M3）、LN Extension、官方指南和示例代码。"
---

# Extension 开发资源

> Infor Extension 开发框架资源汇总，支持 M3（XtendM3）和 LN Extension Modeler。

---

## 🔧 Infor M3 - XtendM3

### 官方资源

| 资源名称 | 简介 | 链接 |
|---------|--------|------|
| **XtendM3 (GitHub)** | M3 云扩展开发框架，安全、现代、高可用 | [GitHub](https://github.com/infor-cloud/xtendm3) |
| **XtendM3 示例仓库** | 官方扩展示例集合 | [GitHub](https://github.com/infor-cloud/xtendm3-extension-examples) |
| **XtendM3 Java SDK** | XtendM3 Java SDK | [GitHub](https://github.com/infor-cloud/xtendm3-sdk-java) |
| **XtendM3 Maven 插件** | XtendM3 Maven 构建插件 | [GitHub](https://github.com/infor-cloud/xtendm3-maven-plugin) |
| **XtendM3 官方文档** | 安装、配置、开发指南 | [文档](https://infor-cloud.github.io/xtendm3/docs/) |
| **XtendM3 - Infor Developer Portal** | 开发者门户中的 XtendM3 导入指南 | [访问](https://developer.infor.com/import/xtendm3) |
| **Acme Corp Extensions** | 版本控制示例仓库（公开模板） | [GitHub](https://github.com/infor-cloud/acme-corp-extensions) |

### XtendM3 扩展示例

```javascript
// XtendM3 示例：在 M3 中创建扩展
// 文件：extensions/ExampleExtension.js

const { Extension, Before } = require('@infor/xtendm3');

class ExampleExtension extends Extension {
  @Before('M3API', 'MMS001MI', 'AddItem')
  async beforeAddItem(context) {
    const { request, session } = context;
    
    // 自定义验证逻辑
    if (request.data.ITNO.length < 5) {
      throw new Error('Item number must be at least 5 characters');
    }
    
    // 修改请求数据
    request.data.ITNO = request.data.ITNO.toUpperCase();
    
    return request;
  }
}

module.exports = ExampleExtension;
```

- **更多示例**：[XtendM3 示例文档](https://infor-cloud.github.io/xtendm3/docs/examples)

---

## 🔧 Infor LN - Extension Modeler

### 官方资源

| 资源名称 | 简介 | 链接 |
|---------|--------|------|
| **Infor LN Extension Modeler 指南** | 使用 Extension Modeler 扩展 LN 功能 | [查看文档](https://docs.infor.com/ln/latest/en-us/lnesolh/lnstudextdg_cl/cover.html) |
| **LN Extension 开发实战** | Extension 开发实战指南 | [查看](../resources/ln-extension-guide.md) |
| **LN 4GL 开发技巧** | DAL2 / Extension / Public Interfaces | [查看](../resources/ln-4gl-tips.md) |

### LN Extension 示例

```4gl
| LN Extension 示例：在采购订单行保存前验证
| 文件：ln-extension/po-line-validate.ext

function extern short before.save.po.line()
{
  | 获取当前行数据
  string item = whinp001.item
  double qty = whinp001.qty.ordered
  
  | 自定义验证：检查最小订购量
  if qty < 1.0 then
    message.error("订购数量必须大于等于 1")
    retval = -1  | 阻止保存
    return(retval)
  endif
  
  | 调用自定义 DAL 函数
  long result = dal.call.function("custom.validate.item", item)
  if result != 0 then
    message.error("物料验证失败：" + dal.get.error.message())
    retval = -1
    return(retval)
  endif
  
  retval = 0  | 允许保存
  return(retval)
}
```

---

## 📖 开发指南

### M3 Extension 开发流程

1. **安装 XtendM3 SDK**
   - 参考：[Installation instructions XtendM3 SDK and Github](https://community.infor.com/discussion/25087/installation-instructions-xtendm3-sdk-and-github/p1)
   
2. **创建扩展项目**
   ```bash
   xtendm3 create my-extension
   cd my-extension
   npm install
   ```

3. **编写扩展逻辑**
   - 使用 JavaScript/TypeScript
   - 支持 Before/After 钩子
   - 支持 M3 API 调用

4. **测试和部署**
   - 本地测试：使用 M3 H5 SDK
   - 部署：通过 Infor OS Portal

### LN Extension 开发流程

1. **打开 LN Extension Modeler**
   - 工具路径：LN → 开发工具 → Extension Modeler

2. **创建扩展**
   - 选择目标 Session 或 Report
   - 选择扩展点（Before/After/Save/Delete 等）

3. **编写 4GL 代码**
   - 使用标准 4GL 语法
   - 可以调用 DAL 函数和 Public Interfaces

4. **部署扩展**
   - 打包为 .pac 文件
   - 使用 LN Package Manager 安装

---

## 🔗 相关资源

- [ION API 开发](ion-api.md) - API 集成开发
- [LN 4GL 代码库](ln-4gl-snippets.md) - 4GL 代码示例
- [开源项目](open-source.md) - Infor 官方开源仓库
- [Stack Overflow 精选](so-qna.md) - 扩展开发问答

---

> 欢迎提交更多 Extension 开发资源！请查看 [资源提交规范](../submission-guide.md)。

**最后更新**：2026-05-11
