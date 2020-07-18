class MusicPlayer(object):
    # 第一个被创建的引用
    instance = None

    def __new__(cls, *args, **kwargs):
        # 类属性是否为None
        if cls.instance is None:
            # 调用父类方法,为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 返回类属性保存的对象引用
        return cls.instance


music1 = MusicPlayer()
print(music1)
music2 = MusicPlayer()
print(music2)
