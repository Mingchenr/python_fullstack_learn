django_learn/          # 项目根目录
├── django_learn/      # 项目核心配置目录（和项目同名）
│   ├── __init__.py    # 空文件，标记为Python包
│   ├── asgi.py        # ASGI协议配置（部署异步服务用，新手暂不用）
│   ├── settings.py    # 项目全局配置（核心！必改）
│   ├── urls.py        # 根路由配置（所有请求的入口）
│   └── wsgi.py        # WSGI协议配置（部署同步服务用，后续部署会用）
├── user/              # 自定义应用（user模块，按业务拆分）
│   ├── __init__.py    # 空文件，标记为Python包
│   ├── admin.py       # 后台管理配置（注册模型到Admin后台）
│   ├── apps.py        # 应用配置（可自定义应用名称、初始化逻辑）
│   ├── migrations/    # 数据库迁移文件（自动生成，记录模型变更）
│   │   └── __init__.py
│   ├── models.py      # 数据模型（核心！定义数据库表结构）
│   ├── tests.py       # 单元测试（写测试用例，企业级项目必备）
│   ├── urls.py        # 应用路由配置（拆分根路由，解耦）
│   ├── views.py       # 视图函数（核心！处理请求、返回响应）
│   └── templates/     # 模板文件夹（存放HTML文件，前后端不分离用）
│       └── user/      # 按应用名拆分模板（避免多应用模板冲突）
│           └── list.html  # 具体模板文件
├── manage.py          # 项目管理脚本（核心！常用命令入口）
└── db.sqlite3         # 默认SQLite数据库文件（后续替换为MySQL）
