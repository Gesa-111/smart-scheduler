from fastapi import APIRouter
from app.database import get_db

router = APIRouter(prefix="/progress", tags=["Progress"])

@router.get("/")
def get_progress():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(*) AS total FROM study_sessions")
    total = cursor.fetchone()["total"]

    cursor.execute(
        "SELECT COUNT(*) AS completed FROM study_sessions WHERE completed = TRUE"
    )
    completed = cursor.fetchone()["completed"]

    percentage = 0

    if total > 0:
        percentage = round((completed / total) * 100, 2)

    return {
        "total_sessions": total,
        "completed_sessions": completed,
        "completion_percentage": percentage
    }
