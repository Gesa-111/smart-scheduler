from fastapi import APIRouter

router = APIRouter(
    prefix="/planner",
    tags=["Planner"]
)

@router.post("/generate")
def generate_schedule(subjects: list[str]):
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
    ]

    schedule = {}

    for i, day in enumerate(days):
        schedule[day] = subjects[i % len(subjects)]

    return schedule
