# 6.1. Автоматическая регистрация классов
# Допустим, вы хотите автоматически регистрировать все созданные классы в реестре.

class MetaClass(type):
    register = {}

    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        mcs.register[name] = cls
        return cls


class Base(metaclass=MetaClass):
    pass


class A(Base):
    pass


class B(Base):
    pass


print(MetaClass.register)
