# Напишите метакласс, который отслеживает создание экземпляров классов.


class MetaClass(type):

    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)
        cls.cnt = 0

    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        cls.cnt += 1
        return instance


class MyClass(metaclass=MetaClass):
    pass


a = MyClass()
b = MyClass()

print(MyClass.cnt)
