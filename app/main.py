from fastapi import FastAPI

from app.routes import schedule
from app.routes import sessions
from app.routes import progress
from app.routes import planner
from app.routes import users

app = FastAPI(
    title="Study Scheduler API",
    version="0.1.0",
    description="Backend API for Study Scheduler"
)

# Register routes
app.include_router(schedule.router)
app.include_router(sessions.router)
app.include_router(progress.router)
app.include_router(planner.router)
app.include_router(users.router)


@app.get("/")
def home():
    return {
        "message": "Study Scheduler API Running",
        "status": "online"
    }
