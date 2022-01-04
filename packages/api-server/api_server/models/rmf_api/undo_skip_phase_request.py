# generated by datamodel-codegen:
#   filename:  undo_skip_phase_request.json

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class UndoPhaseSkipRequest(BaseModel):
    type: Optional[str] = Field(
        None, description="Indicate that this is a request to undo a phase skip request"
    )
    for_task: Optional[str] = Field(None, description="Specify the relevant task ID")
    for_tokens: Optional[List[str]] = Field(
        None,
        description="A list of the tokens of skip requests which should be undone. The skips associated with each token will be discarded.",
        min_items=1,
    )
    labels: Optional[List[str]] = Field(
        None, description="Labels describing this request"
    )
