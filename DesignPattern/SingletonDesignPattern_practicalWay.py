# Even if you called this class in another files, object will be same
# no duplicate object
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


s1 = Singleton()
print(s1)

s2 = Singleton()
print(s2)
