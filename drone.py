from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
import os, shutil, uuid

from database import SessionLocal
import crud, schemas

router = APIRouter()

IMAGE_DIR = "static/images/drones"
os.makedirs(IMAGE_DIR, exist_ok=True)
def get_db():
    db = SessionLocal()
    try:
        yield db
        db.commit()   # 在 yield 后加上 commit 确保事务提交
    except Exception as e:
        db.rollback() # 出现异常时回滚
        print(f"数据库操作异常: {e}")  # 打印异常到控制台
        raise e
    finally:
        db.close()

@router.get("/drones", response_model=list[schemas.DroneOut])
def get_all_drones(db: Session = Depends(get_db)):
    return crud.get_drones(db)

@router.get("/drones/{drone_id}", response_model=schemas.DroneOut)
def get_drone(drone_id: int, db: Session = Depends(get_db)):
    drone = crud.get_drone_by_id(db, drone_id)
    if not drone:
        raise HTTPException(status_code=404, detail="无人机未找到")
    return drone

@router.post("/drones", response_model=schemas.DroneOut)
async def create_drone(
    name: str = Form(...),
    model: str = Form(...),
    price: float | None = Form(None),              # 新增字段
    description: str | None = Form(None),
    image: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    ext = os.path.splitext(image.filename)[1].lower()
    if ext not in [".png", ".jpg", ".jpeg"]:
        raise HTTPException(status_code=400, detail="图片格式只支持 png/jpg/jpeg")

    unique_filename = f"{uuid.uuid4().hex}{ext}"
    file_path = os.path.join(IMAGE_DIR, unique_filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    drone = schemas.DroneCreate(name=name, model=model,price=price,
        description=description,)
    new_drone = crud.add_drone(db, drone, f"/static/images/drones/{unique_filename}")
    print("新增无人机数据：", new_drone)
    return new_drone

@router.put("/drones/{drone_id}", response_model=schemas.DroneOut)
async def update_drone(
    drone_id: int,
    name: str = Form(...),
    model: str = Form(...),
    price: Optional[float] = Form(None),
    description: Optional[str] = Form(None),
    image: UploadFile | None = File(None),
    db: Session = Depends(get_db)
):
    db_drone = crud.get_drone_by_id(db, drone_id)
    if not db_drone:
        raise HTTPException(status_code=404, detail="无人机未找到")

    if image:
        ext = os.path.splitext(image.filename)[1].lower()
        if ext not in [".png", ".jpg", ".jpeg"]:
            raise HTTPException(status_code=400, detail="图片格式只支持 png/jpg/jpeg")

        unique_filename = f"{uuid.uuid4().hex}{ext}"
        file_path = os.path.join(IMAGE_DIR, unique_filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

        old_image_path = "." + db_drone.image
        if os.path.exists(old_image_path):
            os.remove(old_image_path)

        image_path = f"/static/images/drones/{unique_filename}"
    else:
        image_path = db_drone.image

    drone_data = schemas.DroneCreate(name=name, model=model, price=price, description=description)

    updated_drone = crud.update_drone(db, drone_id, drone_data, image_path)

    return updated_drone

@router.delete("/drones/{drone_id}")
def delete_drone(drone_id: int, db: Session = Depends(get_db)):
    drone = crud.get_drone_by_id(db, drone_id)
    if not drone:
        raise HTTPException(status_code=404, detail="无人机未找到")

    image_path = "." + drone.image
    if os.path.exists(image_path):
        os.remove(image_path)

    crud.delete_drone(db, drone_id)
    return {"message": f"删除无人机 {drone_id} 成功"}
