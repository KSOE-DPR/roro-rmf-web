# generated by datamodel-codegen:
#   filename:  interrupt_task_request.json

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class TaskInterruptionRequest(BaseModel):
    type: str = Field(
        ..., description="Indicate that this is a task interruption request"
    )
    task_id: str = Field(..., description="Specify the task ID to interrupt")
    labels: Optional[List[str]] = Field(
        None, description="Labels to describe the purpose of the interruption"
    )
