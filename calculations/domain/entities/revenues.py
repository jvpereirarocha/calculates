from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from calculations.adapters.types.basic_types import AccountUUID, PersonUUID, RevenueUUID
from calculations.domain.entities.accounts import Account

from calculations.domain.entities.models import BaseModel


@dataclass
class Revenue(BaseModel):
    id: Optional[RevenueUUID] = None
    description: Optional[str] = None
    value: Optional[float] = None
    date_of_receivment: Optional[datetime] = None
    account_id: Optional[AccountUUID] = None
    category: Optional[str] = None