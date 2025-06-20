# Drone_StoreV3.0.1
实现前后端交互
 🚁 Drone Store 无人机应用商店

一个基于 **HarmonyOS ArkTS 前端 + FastAPI 后端 + MySQL 数据库** 的无人机信息展示与交互管理平台，支持参数设置、图像展示、游戏互动等功能，已实现完整前后端数据同步和开源部署。

---

 🌟 项目亮点

- ✅ 鸿蒙 HarmonyOS ArkTS 前端，支持动态 UI 与组件化开发
- ✅ 后端基于 FastAPI 框架，接口响应快速、结构清晰
- ✅ 支持无人机商品展示、参数配置、图片查看、新闻浏览等多种功能
- ✅ 实现后端图像上传、JSON 数据传输、RESTful API 交互
- ✅ 附带跳跃类小游戏，增强趣味性
- ✅ 项目已部署成功，支持本地运行与开源学习

---

 📱 应用截图

> 示例界面（建议上传后替换以下图片链接）

| 首页 | 商品详情 | 参数设置 | 小游戏 |
|------|----------|----------|--------|
| ![](docs/screenshots/home.png) | ![](docs/screenshots/detail.png) | ![](docs/screenshots/settings.png) | ![](docs/screenshots/game.png) |

---

## 🧩 功能模块

| 功能 | 描述 |
|------|------|
| 首页 Tabs | 展示商店、战争模拟、新闻三页切换 |
| 无人机列表 | 获取后端所有无人机数据，支持刷新 |
| 产品详情页 | 查看单个无人机完整信息与图像 |
| 参数设置 | 可滑动设置飞行高度、速度、避障开关等 |
| 新闻页面 | 嵌入 WebView 展示实时无人机新闻资讯 |
| 小游戏页面 | 控制无人机跳跃，避免障碍，显示得分 |

---

 🛠 技术栈

| 层级 | 技术 |
|------|------|
| 前端 | HarmonyOS ArkTS + ArkUI |
| 后端 | FastAPI (Python 3.10+) |
| 数据库 | MySQL |
| 数据交互 | HTTP + JSON |
| 状态管理 | @State, Router, ForEach |
| 资源加载 | FastAPI 静态目录 `/static/images/` |

---

🚀 快速运行

前端运行

> 需安装 DevEco Studio 3.1+，配置好 HarmonyOS SDK

```bash
# 打开 entry 模块，真机或模拟器运行
后端运行
需安装 Python3.10+，并配置好 MySQL 数据库和图片目录

bash
复制
编辑
# 安装依赖
pip install -r requirements.txt

# 启动服务
uvicorn main:app --reload
MySQL 初始化
sql
复制
编辑
CREATE DATABASE drone_db;
-- 创建表结构后，运行 main.py 会自动建表
🌐 项目结构说明
bash
复制
编辑
.
├── backend/
│   ├── main.py          # FastAPI 启动入口
│   ├── crud.py          # 数据库操作封装
│   ├── database.py      # DB连接配置
│   ├── models.py        # SQLAlchemy 模型
│   ├── schemas.py       # Pydantic 数据结构
│   ├── routers/         # 接口路由模块
│   └── static/images/   # 图像存储路径
└── entry/               # ArkTS 鸿蒙前端模块
📦 接口文档
访问 Swagger 文档：
👉 http://localhost:8000/docs
支持自动调试所有 GET / POST / PUT / DELETE 接口。

📚 展望与优化
🔐 增加用户登录权限与认证（JWT）

🌍 接入地图与无人机位置模拟

📊 图表统计无人机参数与使用趋势

☁️ 支持上传用户图片/视频至云端

📄 开源协议
本项目采用 MIT License 协议，欢迎学习与二次开发，转载请注明来源。

🤝 致谢
感谢 HarmonyOS、FastAPI、Pydantic、MySQL 等开源技术的强大支持！
