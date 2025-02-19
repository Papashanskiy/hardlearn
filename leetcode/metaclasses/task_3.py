# 6.2. Проверка соответствия атрибутов
# Вы можете использовать метакласс для проверки наличия определённых методов в классе.


class MetaClass(type):

    def __new__(mcs, name, bases, namespace):
        for k in namespace:
            if 'default_attribute' not in namespace:
                raise TypeError(
                    f'There are no default_attribute in class {name}')
        return super().__new__(mcs, name, bases, namespace)


class A(metaclass=MetaClass):
    pass
