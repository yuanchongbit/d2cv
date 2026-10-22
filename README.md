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

与 [D2L](https://zh-v2.d2l.ai/) 的关系：本书深受 D2L 启发，参考了其“可运行代码 + 从零实现”的教学法。作者本人正是通过 D2L 入门深度学习，并长期受益于其清晰的讲解与开源精神，在此向 D2L 作者团队和社区致以诚挚的感谢。本书是独立作品，与 D2L 团队无隶属关系；内容上不重复深度学习基础，聚焦 CV 的完整链路和工程落地。

## 当前状态

**v1.0 初稿**：27 章正文与 6 个附录已全部写完，站点可构建、可部署。

- [x] 项目大纲与章节规划（27 章 + 6 个附录）
- [x] Quarto 书站与 GitHub Pages 部署
- [x] `d2cv` 工具包、测试与 CI
- [x] 第 1–24 章正文（分类、检测、分割、3D、生成、多模态、部署、鲁棒性）
- [x] 第 25–27 章正文（自动驾驶感知、3D 视觉、从复现到发表）
- [x] 附录 A–F（数学、环境、数据集与指标、术语、文献、调试）
- [ ] 全书技术审校与 v1.0 正式发布

每章包含可运行代码、实验输出、工程坑、练习与延伸阅读。依赖较重或需要外部数据的单元标记为 `#| eval: false`，正文会说明运行条件。

完整的章节规划、受众、设计原则与里程碑见 [OUTLINE.md](OUTLINE.md)。

## 快速开始

### 环境

需要 Python 3.11+、[uv](https://docs.astral.sh/uv/)、[Quarto](https://quarto.org/)。

```bash
uv sync --extra dev --extra book
source .venv/bin/activate
```

安装 PyTorch 时如需指定 CPU/CUDA 版本，请先按 [PyTorch 官方说明](https://pytorch.org/get-started/locally/) 安装，再执行 `uv sync --extra dev`。

### 构建书站

```bash
QUARTO_PYTHON="$PWD/.venv/bin/python" quarto preview book
QUARTO_PYTHON="$PWD/.venv/bin/python" quarto render book
```

输出在 `book/_site/`。`QUARTO_PYTHON` 用于确保 Quarto 使用项目虚拟环境，而不是系统 Python。

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
