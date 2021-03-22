# coding=utf8

# -------------------------------------------------------------------
# 定义一个单例模式
# -------------------------------------------------------------------

class Singleton():
    def __new__(self):
        if hasattr(self, '__instance'):
            return self
        else:
            self.__instance = super().__new__(self)


if __name__ == '__main__':
    first_instance = Singleton()
    sencond_instance = Singleton()

    print(id(first_instance), id(sencond_instance))
    