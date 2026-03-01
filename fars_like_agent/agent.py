"""Deprecated legacy module.

This project has been migrated to the multi-agent research workflow.
Use `fars_like_agent.orchestrator.WorkflowOrchestrator` instead.
"""

from .orchestrator import WorkflowOrchestrator

__all__ = ["WorkflowOrchestrator"]
