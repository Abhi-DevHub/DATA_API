from fastapi import APIRouter
from .schemas import EventSchemas, EventListSchemas

router = APIRouter()

@router.get("/")
def read_events() -> EventListSchemas:
    return EventListSchemas(
        items=[EventSchemas(id=i) for i in range(1, 6)],
        message="Events fetched successfully"
    )

@router.get("/{event_id}", response_model=EventSchemas)
def get_event(event_id: int):
    return EventSchemas(id=event_id)