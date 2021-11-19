def uppercase(attrs):
    tmp = dict()
    for attr, v in attrs.items():
        if not attr.startswith("__"):
            tmp[attr.upper()] = v
    return tmp

# die gleiche Signatur wie `type`
def upper_attr(class_name, class_bases, class_attrs):
    """
      Return a class object, with the list of its attribute turned
      into uppercase.
    """

    # veraendert jedes Attribut, welches nicht mit '__' startet
    # uppercase_attrs = {
    #     attr if attr.startswith("__") else attr.upper(): v
    #     for attr, v in class_attrs.items()
    # }
    uppercase_attrs = uppercase(class_attrs)

    # `type` erzeugt weiterhin die Klasse
    # Implementierung der Funktionalitaet von `type` in reinem Python nicht
    # moeglich!
    return type(class_name, class_bases, uppercase_attrs)

# Ab Python 3 funktioniert das modul-weite setzen von __metaclass__ *nicht* mehr
# Python 2: wird von allen Klassen in diesem Modul genutzt
# __metaclass__ = upper_attr

# Python 2
# class Foo():
#     __metaclass__ = upper_attr
#     pass

# Python 3
class Foo(object, metaclass=upper_attr):
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
