# Mini FARS-like Agent Starter

这是一个**可运行的最小骨架**，用于构建一个类似 FARS（Fact/Action/Reasoning/State 风格）的 agent 系统。

## 目标

- 把“问题求解”拆成可观测的步骤：
  1. **Plan**（规划）
  2. **Act**（调用工具）
  3. **Ground**（把结论绑定到证据）
  4. **Respond**（输出可追溯答案）
- 让系统天然支持：
  - 工具调用
  - 记忆检索
  - 证据引用
  - 可插拔 LLM

## 快速开始

```bash
python -m fars_like_agent.cli "比较上海和北京今天的天气并给出建议"
```

> 默认使用启发式 planner（无外部 API），用于演示流程。你可以替换 `LLMClient` 接入任意模型。

## 架构

- `fars_like_agent/agent.py`：主执行循环（plan → act → ground → respond）
- `fars_like_agent/planner.py`：任务分解与动作计划
- `fars_like_agent/tools.py`：工具注册表（示例：calculator、echo）
- `fars_like_agent/memory.py`：简单 memory + 检索
- `fars_like_agent/models.py`：统一数据结构
- `fars_like_agent/llm.py`：可替换 LLM 接口

## 下一步建议（向生产演进）

1. 增加真实检索工具（搜索/API/RAG）并记录证据 URL。
2. 增加“自检器”（consistency/faithfulness checker）。
3. 为每步状态落库（Postgres + object storage）。
4. 增加异步任务编排（Celery / Temporal / Arq）。
5. 引入评测集和离线回放（regression harness）。

