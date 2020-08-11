# 创建工程
# django-admin startproject mysite
# cd mysite
# 运行项目
# python manage.py runserver

# 创建组件
# python manage.py startapp helloapp
# helloapp --> views.py
# mysite --> urls.py
# 访问 http://127.0.0.1:8000/index/

# 创建组件
# python manage.py startapp hello2app
# 放置自己的模板
# hello2app --> templates
# hello2app --> views.py
# 创建本地路由
# hello2app --> urls.py (自己创建)
# 修改全局路由
# mysite --> urls.py
# 添加自己的模板
# mysite --> settings.py ('DIRS': [os.path.join(BASE_DIR, 'hello2app/templates')])
# 访问 http://127.0.0.1:8000/index2/
