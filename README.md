# 动手学计算机视觉（D2CV）

> Dive into Computer Vision. 面向算法工程师的 PyTorch 计算机视觉教材。

[![CI](https://github.com/yuanchongbit/d2cv/actions/workflows/ci.yml/badge.svg)](https://github.com/yuanchongbit/d2cv/actions/workflows/ci.yml)
[![Deploy](https://github.com/yuanchongbit/d2cv/actions/workflows/publish.yml/badge.svg)](https://github.com/yuanchongbit/d2cv/actions/workflows/publish.yml)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/Text-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![Code: MIT-0](https://img.shields.io/badge/Code-MIT--0-blue.svg)](LICENSE-CODE)

**在线阅读**：https://yuanchongbit.github.io/d2cv/

## 这本书是什么

一本面向**有深度学习基础的算法工程师**的开源计算机视觉教材。用 PyTorch 一条技术栈，从图像与卷积讲到检测、分割、3D、生成、多模态与部署。

每章遵循同一套结构：

> 真实问题 → 原理与公式 → 从零实现 → 调库实现 → 实验与误差分析 → 工程坑 → 练习

与 [D2L](https://zh-v2.d2l.ai/) 的关系：继承其“可运行代码 + 从零实现”的教学法，但不重复深度学习基础；本书聚焦 CV 的完整链路和工程落地。

## 当前状态

项目处于 **v0.1 骨架阶段**：

- [x] 项目大纲与章节规划（27 章 + 6 个附录）
- [x] Quarto 书站与 GitHub Pages 部署
- [x] `d2cv` 工具包骨架与测试
- [x] CI（lint + pytest + 站点构建）
- [ ] 批次 1：第 1–8 章正文
- [ ] 批次 2–5 与全量 v1.0

完整的章节规划、受众、设计原则与里程碑见 [OUTLINE.md](OUTLINE.md)。

## 快速开始

### 环境

需要 Python 3.11+、[uv](https://docs.astral.sh/uv/)、[Quarto](https://quarto.org/)。

```bash
uv sync --extra dev
source .venv/bin/activate
```

安装 PyTorch 时如需指定 CPU/CUDA 版本，请先按 [PyTorch 官方说明](https://pytorch.org/get-started/locally/) 安装，再执行 `uv sync --extra dev`。

### 构建书站

```bash
quarto preview book
quarto render book
```

输出在 `book/_site/`。

### 运行测试

```bash
pytest
ruff check src tests
```

## 仓库结构

```text
book/            书稿（Quarto），每章一个目录
src/d2cv/        跨章复用的工具包
tests/           工具包单测
scripts/         重型训练、评测、导出脚本
experiments/     实验配置与结果规范
.github/         CI 与 GitHub Pages 部署
OUTLINE.md       全书大纲与写作计划
```

## 贡献

欢迎提 Issue 和 PR。开始之前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)、[STYLE_GUIDE.md](STYLE_GUIDE.md) 和 [TERMINOLOGY.md](TERMINOLOGY.md)。

## 许可

- 正文与图片：[CC BY-SA 4.0](LICENSE)
- 代码（包括 `src/d2cv`、`scripts`、`tests` 与章内代码）：[MIT-0](LICENSE-CODE)
