from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict


class DeploymentSnowIncident(BaseModel):
    model_config = ConfigDict(extra="forbid")
    account: str
    assignment_group: Optional[str] = None
    category: Optional[str] = None
    contact_type: Optional[str] = None
    correlation_id: Optional[str] = None
    splunk_url: Optional[str] = None
    state: Optional[int] = None
    custom_fields: Optional[str] = None
    impact: Optional[int] = None
    short_description: Optional[str] = None
    subcategory: Optional[str] = None
    urgency: Optional[int] = None
    location: Optional[str] = None
    priority: Optional[int] = None
    ci_identifier: Optional[str] = None
    comments: Optional[str] = None