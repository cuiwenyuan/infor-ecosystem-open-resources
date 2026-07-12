---
title: "开源项目 - 开发者资源中心"
description: "Infor 官方和社区开源项目汇总，包括 GitHub 仓库、示例代码和开发框架。"
---

# Infor 开源项目

> Infor 官方开源仓库和社区项目汇总，遵循 Apache-2.0 开源协议。

---

## 🏢 Infor 官方开源（GitHub: infor-cloud）

### XtendM3 扩展开发框架

| 项目 | Star | Fork | 最后更新 | 简介 | 链接 |
|------|-------|------|---------|------|------|
| **xtendm3** | 9 | 8 | 2026-02 | XtendM3 核心框架 | [GitHub](https://github.com/infor-cloud/xtendm3) |
| **xtendm3-extension-examples** | 3 | 1 | 2020-06 | 扩展示例集合 | [GitHub](https://github.com/infor-cloud/xtendm3-extension-examples) |
| **xtendm3-sdk-java** | 12 | 8 | 2024-10 | XtendM3 Java SDK | [GitHub](https://github.com/infor-cloud/xtendm3-sdk-java) |
| **xtendm3-maven-plugin** | 2 | 7 | 2024-10 | XtendM3 Maven 插件 | [GitHub](https://github.com/infor-cloud/xtendm3-maven-plugin) |
| **acme-corp-extensions** | 1 | 5 | 2023-08 | 版本控制示例仓库 | [GitHub](https://github.com/infor-cloud/acme-corp-extensions) |

### API 与 SDK 项目

| 项目 | Star | Fork | 最后更新 | 简介 | 链接 |
|------|-------|------|---------|------|------|
| **ion-api-sdk** | 96 | 33 | 2023-05 | ION API Gateway Java SDK | [GitHub](https://github.com/infor-cloud/ion-api-sdk) |
| **m3-h5-sdk** | 43 | 27 | 2026-03 | M3 HTML5 SDK | [GitHub](https://github.com/infor-cloud/m3-h5-sdk) |
| **infor-mobile-sdk** | 16 | 4 | 2023-03 | Infor 移动端开发 SDK | [GitHub](https://github.com/infor-cloud/infor-mobile-sdk) |

### 其他官方项目

| 项目 | Star | Fork | 最后更新 | 简介 | 链接 |
|------|-------|------|---------|------|------|
| **cloud-store** | 1 | 1 | 2024-03 | 云存储相关 | [GitHub](https://github.com/infor-cloud/cloud-store) |
| **supply-chain-insights** | 8 | 7 | - | 供应链洞察工具 | [GitHub](https://github.com/infor-cloud/supply-chain-insights) |
| **lemur** | 2 | 345 | 2023-10 | Lemur 证书管理器（Netflix fork） | [GitHub](https://github.com/infor-cloud/lemur) |

- **官方组织主页**：[github.com/infor-cloud](https://github.com/infor-cloud)

---

## 🌐 社区开源项目

### LN 相关项目

| 项目 | 简介 | 链接 |
|------|--------|------|
| **maharhoshi/InforLN** | Infor ERP LN 相关代码和工具 | [GitHub](https://github.com/maharhoshi/InforLN) |
| **pavanthota97/INFOR-LN** | Infor LN 开发示例 | [GitHub](https://github.com/pavanthota97/INFOR-LN) |
| **shubham225/infor-ln-devtools** | VS Code 扩展（LN 构件管理） | [GitHub](https://github.com/shubham225/infor-ln-devtools) |
| **cuiwenyuan/infor-bw-dotnet-baanlib** | .NET (C#) 开源库，封装 Baan/Infor LN 的 OLE 自动化对象（`Baan.Application.*`），以链式 API 调用 LN 4GL DLL 函数；多目标 .NET Framework 4.6.2+ 与 .NET 6/8/10（Windows），NuGet 包名 `Wangcaisoft.DotNet.BaanWindowsLib`，MIT 许可 | [GitHub](https://github.com/cuiwenyuan/infor-bw-dotnet-baanlib) |

### M3 相关项目

| 项目 | 简介 | 链接 |
|------|--------|------|
| **社区 M3 扩展示例** | M3 用户贡献的扩展示例 | [GitHub 搜索](https://github.com/search?q=infor+m3&type=repositories) |

### ION 集成相关项目

| 项目 | 简介 | 链接 |
|------|--------|------|
| **ION API 客户端示例** | 社区贡献的 ION API 调用示例 | [GitHub 搜索](https://github.com/search?q=infor+ion+api&type=repositories) |

### 📦 社区精选：Wangcaisoft.DotNet.BaanWindowsLib

由本仓库维护者开源的 **.NET (C#) Infor LN / Baan 集成库**，封装 `Baan.Application.*` OLE 自动化对象，以链式 API 调用 LN 4GL DLL 函数；多目标 .NET Framework 4.6.2+ 与 .NET 6 / 8 / 10（Windows 平台），采用 MIT 许可。

**安装（NuGet）**

```bash
dotnet add package Wangcaisoft.DotNet.BaanWindowsLib
```

**适用场景**

- 在 .NET 程序中自动化登录 LN / Baan 并调用 4GL DLL 函数、读写表数据
- 与现有 C# 业务系统集成（报表触发、数据同步、批量作业）
- 替代旧版 `Baan.Application.*` COM 直接调用，获得强类型与链式 API 体验

> 链式 API 的具体方法签名与示例以仓库 [README](https://github.com/cuiwenyuan/infor-bw-dotnet-baanlib) 为准（截至收录时 NuGet 包页尚未发布，包名已保留为 `Wangcaisoft.DotNet.BaanWindowsLib`）。

---

## 🛠️ 开发框架与工具

### XtendM3 开发环境搭建

```bash
# 1. 安装 XtendM3 CLI
npm install -g @infor/xtendm3-cli

# 2. 创建扩展项目
xtendm3 create my-extension
cd my-extension

# 3. 安装依赖
npm install

# 4. 本地开发
npm run dev

# 5. 打包部署
npm run build
```

### ION API SDK 使用

```java
// Java 示例：使用 ION API SDK 调用 Infor LN API
import com.infor.ionapi.sdk.IonApiClient;

public class IonApiExample {
    public static void main(String[] args) {
        IonApiClient client = new IonApiClient.Builder()
            .baseUrl("https://your-tenant.infor.com")
            .clientId("your-client-id")
            .clientSecret("your-client-secret")
            .build();
        
        // 调用 LN API
        String response = client.get("/api/v1/items/10001");
        System.out.println(response);
    }
}
```

---

## 🔗 相关资源

- [ION API 开发](ion-api.md) - API Gateway 文档和 SDK
- [Extension 开发](extensions.md) - XtendM3 和 LN Extension
- [LN 4GL 代码库](ln-4gl-snippets.md) - 4GL 代码示例
- [Infor Developer Portal](https://developer.infor.com/) - 官方开发者门户

---

> 如果发现更多 Infor 相关开源项目，欢迎 [提交](../submission-guide.md)！

**最后更新**：2026-07-12
