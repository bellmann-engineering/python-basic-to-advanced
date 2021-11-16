# Ableitung von der `type` Klasse
class UpperAttrMetaclass(type):
    # `__new__` ist die Methode, welche vor `__init__` aufgerufen wird, das
    # Objekt initialisiert und zurueck gibt.
    # `__new__` wird nur selten verwendet, es sei denn man moechte kontrollieren,
    # wie das Objekt erzeugt wird. Hier ist das zu erzeugende Objekt eine
    # Klasse, daher ueberschreiben wir `__new__` um es anzupassen
    # Der Parameter `metaclass_name` ist der Name der Klasse, ein
    # Standardparameter, uehnlich `self`
    def __new__(metaclass_name, class_name, class_parents, class_attrs):
        uppercase_attrs = {
            attr if attr.startswith("__") else attr.upper(): v
            for attr, v in class_attrs.items()
        }
        # Falsch: kein richtiges OOP
        # return type(class_name, class_parents, uppercase_attrs)
        # Besser:
        # return type.__new__(metaclass_name, class_name, class_parents, uppercase_attrs)
        # Am Besten (ermoeglicht richtige Vererbung):
        return super(UpperAttrMetaclass, metaclass_name).__new__(
                metaclass_name, class_name, class_parents, uppercase_attrs)

class Foo(object, metaclass=UpperAttrMetaclass):
    bar = 'bip'

def main():
    print(hasattr(Foo, 'bar'))
    # False
    print(hasattr(Foo, 'BAR'))
    # True
    print(Foo.BAR)
    # 'bip'


if __name__ == '__main__':
    main()
