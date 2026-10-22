# 贡献指南

感谢你愿意改进 D2CV。本书同时是教材和工程项目，内容、代码、图表、实验复现都欢迎贡献。

## 开始之前

- 先搜索已有 Issue，避免重复。
- 大改动（新增章节、调整全书结构）请先开 Issue 讨论。
- 小修复（错别字、失效链接、代码 bug）可以直接提 PR。

## 本地环境

```bash
uv sync --extra dev
source .venv/bin/activate
pytest
ruff check src tests
```

构建书站需要 [Quarto](https://quarto.org/)：

```bash
quarto preview book
quarto render book --no-execute
```

## 章节贡献

- 新章节从 `book/_quarto.yml` 的章节目录和现有章节页开始，保持统一结构。
- 章首注明学习目标、前置、预计时长、显存、数据集与“最后验证日期”。
- 代码必须可运行；重型训练放到 `scripts/`，正文展示关键片段。
- 关键数字必须有脚本、配置和硬件说明。
- 实验结果至少报告 3 个种子的均值与方差，或明确说明原因。
- 图表由脚本生成，源文件随章节提交。
- 代码或正文改动后先在本地运行 `quarto render book`，把更新后的 `book/_freeze/` 一并提交；线上发布使用冻结结果，不会重新执行全书。

## 代码贡献

- `src/d2cv/` 只放跨章复用代码；章节专用实现留在章节内。
- 库代码加类型标注，遵循 ruff 配置。
- 新增工具函数必须带测试。
- 不引入不必要的依赖；重依赖放到 optional extras。
- 不提交数据集、模型权重、ONNX/TensorRT 引擎。

## 写作规范

请阅读 [STYLE_GUIDE.md](STYLE_GUIDE.md) 和 [TERMINOLOGY.md](TERMINOLOGY.md)。重点：

- 中文优先，术语首次出现给英文。
- 不做无出处的性能断言。
- 公式符号统一，形状统一写成 `(N, C, H, W)`。
- 边界框默认 `xyxy`，其他格式在变量名中写明。
- 每章至少有一个“工程坑”小节。

## 提交与 PR

- 分支前缀：`feat/`、`fix/`、`docs/`、`exp/`。
- 提交信息用祈使句，例如 `add nms implementation and tests`。
- 一个 PR 只做一件事；章节 PR 附上构建截图或结果表。
- 提交前运行：

```bash
ruff check src tests
pytest
quarto render book --no-execute
```

## 章节状态

每个章节页标注状态：

- `草稿`：结构已定，内容写作中。
- `可运行`：代码从头到尾可执行，CI 通过。
- `已复现`：关键结果在指定硬件上复现。
- `已审校`：技术审校与语言审校完成。

## 行为准则

- 对事不对人，技术讨论保持具体、可验证。
- 不提交他人的未授权代码、数据或图片。
- 引用论文与开源项目时注明出处和许可。
- 涉及安全的内容只做防御性讨论，不提供可用于攻击的完整武器化代码。
