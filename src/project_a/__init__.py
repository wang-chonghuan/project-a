__all__ = ["build_status"]


def build_status(environment: str = "local") -> dict[str, str]:
    return {"service": "project-a", "environment": environment, "status": "ok"}
