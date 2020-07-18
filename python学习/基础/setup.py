from distutils.core import setup

setup(
    name="包名",
    version="1.0.0",
    description="描述",
    long_description="完整描述信息",
    author="作者",
    author_email="邮件",
    url="主页",
    py_modules=["模块名"], requires=['PIL']
)

# python3 setup.py build
# python3 setup.py sdist
