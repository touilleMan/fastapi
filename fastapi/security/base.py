from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fastapi.openapi.models import SecurityBase as SecurityBaseModel


class SecurityBase:
    model: SecurityBaseModel
    scheme_name: str
