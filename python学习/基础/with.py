"""
    执行EXPR，生成上下文管理器context_manager；
    获取上下文管理器的__exit()__方法，并保存起来用于之后的调用；
    调用上下文管理器的__enter__()方法；如果使用了as子句，则将__enter__()方法的返回值赋值给as子句中的VAR；
    执行BLOCK中的表达式；
    不管是否执行过程中是否发生了异常，执行上下文管理器的__exit__()方法，__exit__()方法负责执行“清理”工作，如释放资源等。如果执行过程中没有出现异常，或者语句体中执行了语句break/continue/return，则以None作为参数调用__exit__(None, None, None)；如果执行过程中出现异常，则使用sys.exc_info得到的异常信息为参数调用__exit__(exc_type, exc_value, exc_traceback)；
    出现异常时，如果__exit__(type, value, traceback)返回False，则会重新抛出异常，让with之外的语句逻辑来处理异常，这也是通用做法；如果返回True，则忽略异常，不再对异常进行处理。
"""


class DBManager(object):
    def __init__(self):
        print('__init__')

    def __enter__(self):
        print('__enter__')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')
        return True     # 忽略所有错误


def getInstance():
        return DBManager()


with getInstance() as dbManagerIns:
    x = 1/0
    print('with demo')


