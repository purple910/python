# 安装markdown
pip install markdown
# 生成数据库表
python manage.py migrate
# 创建超级管理员的用户名和密码
python manage.py createsuperuser
# 把model转换成中间件
python manage.py makemigrations