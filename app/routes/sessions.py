from fastapi import APIRouter, Header, HTTPException
from app.database import get_db
from app.auth import SECRET_KEY
from jose import jwt

router = APIRouter(prefix="/sessions", tags=["Sessions"])


def get_user_from_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload["user_id"]
    except:
        return None


# GET SESSIONS (protected)
@router.get("/")
def get_sessions(authorization: str = Header(None)):
    user_id = get_user_from_token(authorization)

    if not user_id:
        raise HTTPException(status_code=401, detail="Unauthorized")

    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM study_sessions WHERE user_id=%s", (user_id,))
    return cursor.fetchall()


# CREATE SESSION (protected)
@router.post("/")
def create_session(day: str, subject: str, topic: str, authorization: str = Header(None)):
    user_id = get_user_from_token(authorization)

    if not user_id:
        raise HTTPException(status_code=401, detail="Unauthorized")

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO study_sessions (day, subject, topic, user_id) VALUES (%s, %s, %s, %s)",
        (day, subject, topic, user_id)
    )

    db.commit()

    return {"message": "Session created"}
