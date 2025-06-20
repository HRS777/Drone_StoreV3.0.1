from sqlalchemy.orm import Session
import models, schemas
from typing import Optional

def verify_user(db: Session, username: str, password: str) -> Optional[models.User]:
    return db.query(models.User).filter(
        models.User.username == username,
        models.User.password == password
    ).first()

def get_drones(db: Session):
    return db.query(models.Drone).all()

def add_drone(db: Session, drone: schemas.DroneCreate, image_path: str):
    new_drone = models.Drone(
        name=drone.name,
        model=drone.model,
        price=drone.price,           # 新增
        description=drone.description, # 新增
        image=image_path
    )
    db.add(new_drone)
    db.commit()
    db.refresh(new_drone)
    return new_drone

def get_drone_by_id(db: Session, drone_id: int):
    return db.query(models.Drone).filter(models.Drone.id == drone_id).first()

def update_drone(db: Session, drone_id: int, drone: schemas.DroneCreate, image_path: str | None = None):
    db_drone = db.query(models.Drone).filter(models.Drone.id == drone_id).first()
    if db_drone:
        db_drone.name = drone.name
        db_drone.model = drone.model
        db_drone.price = drone.price           # 新增
        db_drone.description = drone.description 
        if image_path is not None:
            db_drone.image = image_path
        db.commit()
        db.refresh(db_drone)
    return db_drone

def delete_drone(db: Session, drone_id: int):
    db_drone = db.query(models.Drone).filter(models.Drone.id == drone_id).first()
    if db_drone:
        db.delete(db_drone)
        db.commit()
    return db_drone
