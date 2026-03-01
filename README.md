# New Project: FARS-like 自动化研究系统（多智能体）

> 这是**新项目入口**。旧的单回合 demo agent 不再作为主流程维护。

## 你需要先知道的 5 件事

1. **项目目标**：自动完成研究流程（创意 → 规划 → 实验 → 写作）。
2. **执行方式**：通过一个工作流编排器串联 4 个专业 agent。
3. **状态管理**：使用状态机控制生命周期，支持失败态。
4. **数据落盘**：每个项目在 workspace 下持久化阶段产物。
5. **当前边界**：实验执行仍为模拟，后续替换为真实任务系统（Celery/Ray/K8s）。

## 快速运行

```bash
python -m fars_like_agent.cli "自动化研究系统中的证据约束" --project-id project_001 --workspace workspace
```

## 运行产物

执行后将在 `workspace/projects/<project_id>/` 生成：

- `hypothesis.json`
- `plan.json`
- `experiments/results/results.json`
- `paper/draft.md`
- `metadata.json`

## 核心目录

- `fars_like_agent/agents/`：四类专业 agent
- `fars_like_agent/orchestrator/`：状态机与工作流编排
- `fars_like_agent/filesystem/`：项目文件系统管理
- `tests/test_workflow.py`：端到端骨架测试

## 下一步（建议优先级）

1. Ideation 接入 arXiv/Semantic Scholar。
2. Experiment 接入异步任务队列 + GPU 调度。
3. Writing 增加引用管理与格式化输出（Markdown/LaTeX）。
4. 增加阶段审查器（LLM-as-a-Judge）。

更多上手信息见 `NEW_PROJECT_GUIDE.md`。
