# 不会 Git 命令也能上传 GitHub

> 这是供用户自行操作的步骤，不代表仓库已经上传到你的个人 GitHub。

## 第 1 步：下载并解压项目

从发布页下载 `DirtyData-Killer-GitHub-Ready-v0.1.0.zip`，解压后打开**里面**的 `DirtyData-Killer` 文件夹：应该直接看到 `README.md`、`skills/`、`docs/`、`examples/`、`.github/` 等。

**注意：GitHub 的 Upload files 要上传的是文件/文件夹，不是直接把整个 ZIP 当成代码仓库。**

## 第 2 步：创建空仓库

1. 打开 https://github.com/new （先登录 GitHub）。
2. Repository name：`DirtyData-Killer`
3. Description：`中文 Excel/CSV 数据质量检查与智能清洗 Skill 开源项目`。
4. 选 `Public`。
5. **不要勾选新建 README、License 或 .gitignore**：压缩包里已带了。
6. 点击 `Create repository`。

## 第 3 步：上传所有内容

1. 在空仓库网页点击 `uploading an existing file`，或进入 `Add file → Upload files`。
2. 将解压后 `DirtyData-Killer/` **内部所有文件和文件夹**拖进去；包括以点开头的 `.github/`、`.gitignore`。
3. 确认 GitHub 上传列表显示 `README.md`、`skills/.../SKILL.md` 等，**没有多套一个 DirtyData-Killer/ 顶层目录**。
4. 填写 Commit message：`Initial release: DirtyData Killer v0.1.0`。
5. 点击提交（按钮可能显示 `Commit changes` / `Propose changes`）。

官方说明：https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository

## 第 4 步：发布 Release（可选）

1. 仓库主页 → `Releases` → `Create a new release`。
2. Tag 填 `v0.1.0`，标题 `DirtyData Killer v0.1.0 — 三个中文 Skill`。
3. Release Notes 可从 [CHANGELOG.md](../CHANGELOG.md) 复制。
4. 如需让用户方便下载单 Skill ZIP，可附加 `dist/` 中三个 ZIP 文件。
5. 发布后，用无痕浏览器打开仓库，确认 README 可见、路径正常。

## 如果上传后不对怎么办？

- README 没显示：检查它是不是被放到外层 `DirtyData-Killer/README.md`，而不是仓库根目录。
- `skills/` 不见了：多半只上传了 ZIP，需解压后上传目录内容。
- `.github/` 没有：电脑隐藏文件未选中，检查文件管理器“显示隐藏文件”。
- 不要将 `.env`、API Key、真实敏感表格上传到公共仓库。
