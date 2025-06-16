from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_events():
    return {
            # lists
            "items":[1,2,3,4,5],
            "message":"Events fetched successfully"
           }

@router.get("/{event_id}")
def get_event(event_id: int):
    return {
            # single row
            "event_id": event_id,
           }    