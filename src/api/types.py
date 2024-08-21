from typing import Optional
import strawberry
from datetime import datetime

@strawberry.type
class CategoryType:
    id: strawberry.ID
    description: str
    user_id: int
    updated: Optional[datetime] = None
    created: datetime = datetime.now()