from fastapi import APIRouter

router = APIRouter(prefix="/schedule", tags=["Schedule"])

@router.get("/")
def get_schedule():
    return {"message": "Schedule endpoint working"}
