from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import crud, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.get("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = crud.verify_user(db, username, password)
    if user:
        return {"status": "ok", "message": "登录成功", "user_id": user.id}
    else:
        return {"status": "error", "message": "账号或密码错误"}
