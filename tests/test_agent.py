from fars_like_agent import WorkflowOrchestrator


def test_package_exports_new_workflow_entrypoint():
    assert WorkflowOrchestrator is not None
