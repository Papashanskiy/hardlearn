# Чтобы создать свой метакласс, необходимо унаследоваться от type и переопределить специальные методы, такие как __new__ или __init__.


class MetaClass(type):

    def __new__(mcs, name, bases, namespace):
        namespace['default_attr'] = 1
        return super().__new__(mcs, name, bases, namespace)


class MyClass(metaclass=MetaClass):
    pass


obj = MyClass()
print(obj.default_attr)
