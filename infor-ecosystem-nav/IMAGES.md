# 添加产品图片指南

本文件说明如何为 Infor 产品生态系统导航站添加产品图片。

## 需要的图片

请在 `docs/assets/images/` 目录下添加以下图片：

### 核心产品图片

| 文件名 | 产品 | 建议尺寸 | 格式 |
|---------|------|----------|------|
| `infor-ln.png` | Infor LN | 200x200 px | PNG (透明背景) |
| `infor-m3.png` | Infor M3 | 200x200 px | PNG (透明背景) |
| `cloudsuite-industrial.png` | CloudSuite Industrial | 200x200 px | PNG (透明背景) |

### 技术平台图片

| 文件名 | 平台 | 建议尺寸 | 格式 |
|---------|------|----------|------|
| `infor-os.png` | Infor OS | 200x200 px | PNG (透明背景) |
| `coleman-ai.png` | Coleman AI | 200x200 px | PNG (透明背景) |
| `birst.png` | Birst Analytics | 200x200 px | PNG (透明背景) |
| `ion.png` | ION | 200x200 px | PNG (透明背景) |
| `mingle.png` | Ming.le | 200x200 px | PNG (透明背景) |

### 通用图片

| 文件名 | 用途 | 建议尺寸 | 格式 |
|---------|------|----------|------|
| `logo.png` | 网站 Logo | 100x100 px | PNG (透明背景) |
| `favicon.ico` | 网站图标 | 32x32 px | ICO |

## 如何获取图片

### 方案 1：从 Infor 官网下载

1. 访问 https://www.infor.com/
2. 右键点击产品 Logo
3. 选择"图片另存为..."
4. 保存到 `docs/assets/images/` 目录

### 方案 2：截图产品页面

1. 访问产品官方页面
2. 截取产品 Logo 或图标
3. 使用图片编辑工具去除背景
4. 保存为 PNG 格式

### 方案 3：使用 Infor 媒体资源

1. 访问 Infor 媒体资源页面（需要登录）
2. 下载官方产品图片
3. 保存到项目目录

## 图片优化建议

### 文件大小

- 建议每张图片 < 50KB
- 使用图片压缩工具（如 TinyPNG）

### 文件命名

- 使用小写字母
- 使用连字符分隔单词
- 例如：`infor-ln.png`, `cloudsuite-industrial.png`

### 备用文本

在 Markdown 文件中，使用 `alt` 属性提供图片描述：

```markdown
![Infor LN Logo](../../assets/images/infor-ln.png)
```

即使图片缺失，用户也能看到描述文本。

## 无图片时的显示效果

如果图片文件不存在，MkDocs 会显示：

```
[Infor LN Logo]
```

用户仍然可以理解内容。

## 测试图片显示

本地运行网站后，检查图片是否显示正常：

```bash
mkdocs serve
```

访问 http://127.0.0.1:8000/ 并检查产品详情页面。

---

**💡 提示**：您可以先部署网站（无图片），后续再逐步添加图片。网站功能不受影响。
