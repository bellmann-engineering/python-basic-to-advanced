# ACHTUNG: Funktioniert nur mir Python 2!

# die gleiche Signatur wie `type`
def upper_attr(class_name, class_bases, class_attrs):
    """
      Return a class object, with the list of its attribute turned
      into uppercase.
    """

    # veraendert jedes Attribut, welches nicht mit '__' startet
    uppercase_attrs = {
        attr if attr.startswith("__") else attr.upper(): v
        for attr, v in class_attrs.items()
    }

    # `type` erzeugt weiterhin die Klasse
    return type(class_name, class_bases, uppercase_attrs)

# Ab Python 3 funktioniert das modul-weite setzen von __metaclass__ *nicht* mehr
# wird von allen Klassen in diesem Modul genutzt
__metaclass__ = upper_attr

class Foo():
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
