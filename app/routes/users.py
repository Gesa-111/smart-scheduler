from fastapi import APIRouter
from app.database import get_db
from app.auth import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/users", tags=["Users"])


# REGISTER
@router.post("/register")
def register(username: str, email: str, password: str):
    db = get_db()
    cursor = db.cursor()

    hashed = hash_password(password)

    cursor.execute(
        "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
        (username, email, hashed)
    )

    db.commit()

    return {"message": "User created successfully"}


# LOGIN
@router.post("/login")
def login(username: str, password: str):
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    user = cursor.fetchone()

    if not user:
        return {"error": "User not found"}

    if not verify_password(password, user["password"]):
        return {"error": "Wrong password"}

    token = create_access_token({"user_id": user["id"]})

    return {"access_token": token, "token_type": "bearer"}
