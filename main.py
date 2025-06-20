from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session


import models
from database import engine, SessionLocal
from drone import router as drone_router  # 导入你写的无人机模块路由

# 创建数据库表（如果尚未创建）
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# 跨域配置，允许所有源访问（开发时用，生产环境可适当收紧）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 挂载静态文件目录，访问 /static 路径即可访问 static 文件夹
app.mount("/static", StaticFiles(directory="static"), name="static")

# 依赖注入数据库会话
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 登录接口示例（可根据实际调整）
@app.get("/login")
async def login(username: str, password: str, db: Session = Depends(get_db)):
    from crud import verify_user  # 避免循环导入，放这里
    user = verify_user(db, username, password)
    if not user:
        raise HTTPException(status_code=401, detail="用户名或密码错误")
    return {"result": "success"}

# 注册无人机相关路由（所有 /drones 路由都放在 drone_router 里）
app.include_router(drone_router)

# 测试用接口，查看图片是否可访问
from fastapi.responses import HTMLResponse

@app.get("/test-image", response_class=HTMLResponse)
async def test_image():
    html_content = """
    <html>
        <head><title>图片测试</title></head>
        <body>
            <h1>无人机图像测试</h1>
            <img src='/static/images/drones/drone1.png' width='300'/>
            <img src='/static/images/drones/drone2.png' width='300'/>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)
