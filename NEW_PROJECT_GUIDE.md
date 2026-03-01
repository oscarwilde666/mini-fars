# 新项目上手指南

## 一、架构概览

- **IdeationAgent**：根据 research direction 产出假设。
- **PlanningAgent**：把假设拆成实验计划与资源需求。
- **ExperimentAgent**：执行实验（当前为模拟执行）。
- **WritingAgent**：根据结果生成论文草稿。
- **WorkflowOrchestrator**：编排阶段、写入事件、统一落盘。
- **StateMachine**：限制状态转移，避免非法流程。
- **ProjectManager**：创建目录并保存 JSON/文本产物。

## 二、开发时最常改的文件

- Agent 逻辑：`fars_like_agent/agents/*.py`
- 工作流流程：`fars_like_agent/orchestrator/workflow.py`
- 状态定义：`fars_like_agent/orchestrator/state_machine.py`
- 文件落盘策略：`fars_like_agent/filesystem/project_manager.py`

## 三、如何验证改动

```bash
python -m pytest -q
python -m fars_like_agent.cli "你的研究方向" --project-id demo --workspace /tmp/fars_ws
```

重点检查：
- 是否生成完整产物文件。
- `metadata.json` 的 `events` 是否完整。
- `state` 是否为 `COMPLETED`。

## 四、当前限制

- 没有真实文献检索。
- 没有真实训练/推理任务调度。
- 没有人工审核入口和 Web Dashboard。

## 五、建议协作方式

- 每新增一个能力，先加一个 workflow 测试。
- 使用固定 `project_id` 与 `tmp_path`，保证测试可复现。
- 每个 agent 的输入输出保持 JSON 兼容，便于后续服务化。
