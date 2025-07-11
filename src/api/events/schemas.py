from pydantic import BaseModel
from typing import List
class EventSchemas(BaseModel):
    id:int

class EventListSchemas(BaseModel):
    items: List[EventSchemas]
    message: str = "Events fetched successfully"

#{"id":12}