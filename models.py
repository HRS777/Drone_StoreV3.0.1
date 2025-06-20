from sqlalchemy import Column, Integer, String, Float, Text  
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String(100), nullable=False)

class Drone(Base):
    __tablename__ = "drones"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    model = Column(String(100))
    image = Column(String(200), nullable=True)  # 存储图片路径
    price = Column(Float)  # 新增价格字段
    description = Column(Text)  # 新增介绍字段
