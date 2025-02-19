# Создайте метакласс, который добавляет определённый префикс ко всем методам класса.


class MetaClass(type):

    def __new__(mcs, name, bases, namespace):
        prefixed_namespace = {}
        for k in namespace:
            if callable(namespace[k]):
                prefixed_namespace[f'pro_{k}'] = namespace[k]
            else:
                prefixed_namespace[k] = namespace[k]
        return super().__new__(mcs, name, bases, prefixed_namespace)


class A(metaclass=MetaClass):

    def foo(self):
        print('Hello world!')


a = A()

a.pro_foo()
