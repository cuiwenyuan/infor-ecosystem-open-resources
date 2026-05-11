# 图片资源命名规范

## 目录结构

```
docs/assets/images/
├── consultants/     # 顾问公司 Logo
├── products/        # Infor 产品 Logo
├── tools/          # 工具/插件图标
└── screenshots/    # 产品截图
```

## 命名规范

### 顾问公司 Logo
- 格式：`consultant-[公司英文名小写-removed-special-chars].png`
- 示例：`consultant-delotte.png`, `consultant-pwc.png`
- 尺寸：建议 200x100px，透明背景 PNG

### 产品 Logo
- 格式：`product-[产品名小写-removed-special-chars].png`
- 示例：`product-infor-ln.png`, `product-sap-s4hana.png`
- 尺寸：建议 100x100px

### 工具图标
- 格式：`tool-[工具名小写-removed-special-chars].png`
- 示例：`tool-workato.png`, `tool-novacura.png`

## 使用方法

在 Markdown 文件中引用图片：

```markdown
![公司名称](../../assets/images/consultants/consultant-xxx.png){ width=150 }
```

## 注意事项

1. 优先使用公司官方 Logo（从官网获取）
2. 图片文件大小不超过 100KB
3. 使用 PNG 格式（支持透明背景）
4. 如果无法获取 Logo，使用公司首字母作为占位符
