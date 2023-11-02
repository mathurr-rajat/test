# implementation of Singleton design pattern

class Singleton:
    _instance = None

    @staticmethod
    def getinstance():
        if Singleton._instance is None:
            Singleton()
        return Singleton._instance

    def __init__(self):
        # Singleton.getinstance()
        if Singleton._instance is not None:
            raise Exception("Singleton class object already exists")
        else:
            Singleton._instance = self


s1 = Singleton.getinstance()
print(s1)

s2 = Singleton.getinstance()
print(s2)

s3 = Singleton()
print(s3)