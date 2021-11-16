Metaclasses
==

Klassen *sind* Objekte
===

Bevor man *metaclasses* verstehen kann muss man ein Verständnis dafür
entwickeln, was Klassen in in Python sind. Das Klassenkonzept in Python ist
etwas eigen und lehnt sich sehr an Smalltalk an.

In den meisten Sprachen ist eine Klasse nur ein Stück Code, welcher beschreibt,
wie eine Objekt erzeugt werden soll. In gewisser Weise trifft das auch auf
Python zu:

```python
    >>> class ObjectCreator(object):
    ...       pass
    ...

    >>> my_object = ObjectCreator()
    >>> print(my_object)
    <__main__.ObjectCreator object at 0x8974f2c>
```

In Python können Klassen jedoch mehr. Sie sind nämlich gleichzeitig *Objekte*:

> Eine Klasse, welche benutzt wird um Objekte zu erzeugen ist selbst ein Objekt.

Sobald man das Schlüsselwort `class` verwendet, führt Python diesen Code aus und
erzeugt *Objekt*. Die Anweisung

```python
    >>> class ObjectCreator(object):
    ...       pass
    ...
```

erzeugt dabei im Speicher ein Objekt mit dem Namen `ObjectCreator`.

> Dieses Objekt (die Klasse) ist selbst wiederum in der Lage Objekte (die
> Instanzen) zu erzeugen, weshalb es eine Klasse ist.

Trotzdem ist es auch weiterhin ein Objekt und deshalb:

- kann es einer Variable zugewiesen werden
- kann es kopiert werden
- können Attribute zugewiesen werden
- kann es einer Funktion als Parameter übergeben werden

z.B.:

```python
    >>> print(ObjectCreator) # Klassen können ausgedruckt werden, da sie Objekte sind
    <class '__main__.ObjectCreator'>
    >>> def echo(o):
    ...       print(o)
    ...
    >>> echo(ObjectCreator) # Klassen können als Parameter übergeben werden
    <class '__main__.ObjectCreator'>
    >>> print(hasattr(ObjectCreator, 'new_attribute'))
    False
    >>> ObjectCreator.new_attribute = 'foo' # Attribute können hinzugefügt werden
    >>> print(hasattr(ObjectCreator, 'new_attribute'))
    True
    >>> print(ObjectCreator.new_attribute)
    foo
    >>> ObjectCreatorMirror = ObjectCreator # Klassen können Variablen zugewiesen werden
    >>> print(ObjectCreatorMirror.new_attribute)
    foo
    >>> print(ObjectCreatorMirror())
    <__main__.ObjectCreator object at 0x8997b4c>
```

Klassen dynamisch erzeugen
===

Da Klassen, wie eben dargelegt, nur Objekte sind, können diese auch dynamisch
zur Programmlaufzeit erzeugt werden. Wie jedes andere Objekt auch.

Eine Möglichkeit ist eine Funktion zu schreiben, welche eine Klasse zurück gibt:

```python
    >>> def choose_class(name):
    ...     if name == 'foo':
    ...         class Foo(object):
    ...             pass
    ...         return Foo # gibt die Klasse zurück, nicht die Instanz
    ...     else:
    ...         class Bar(object):
    ...             pass
    ...         return Bar
    ...
    >>> MyClass = choose_class('foo')
    >>> print(MyClass) # die Funktion gibt die Klasse zurück, nicht die Instanz
    <class '__main__.Foo'>
    >>> print(MyClass()) # mit dieser Klasse können nun Objekte erzeugt werden
    <__main__.Foo object at 0x89c6d4c>
```

Das ist allerdings noch nicht sehr dynamisch, immerhin muss man nach wie vor die
ganze Klasse selbst schreiben.

Da Klassen auch Objekte sind, müssen diese durch irgendwas erzeugt werden.

Wenn man das Schlüsselwort `class` verwendet, erzeugt Python dieses Objekt
automatisch. Allerdings gibt es auch eine Möglichkeit (wie so oft in Python)
dies manuell zu tun.

Hierzu verwendet man die Funktion `type`, eben jene Funktion, mit der man auch
herausfinden kann, von welchem Typ ein Objekt ist:

```python
    >>> print(type(1))
    <type 'int'>
    >>> print(type("1"))
    <type 'str'>
    >>> print(type(ObjectCreator))
    <type 'type'>
    >>> print(type(ObjectCreator()))
    <class '__main__.ObjectCreator'>
```

Die `type` Funktion hat jedoch noch eine komplett andere Funktionalität. Mit ihr
ist es möglich Klassen dynamisch zu erzeugen. Die Beschreibung der Klasse wird
hierbei als Parameter übergeben. Der Rückgabewert ist dann die erzeugte Klasse.

`type` hat dabei die folgende Signatur:

```python
    type(name, bases, attrs)
```

- **`name`**: Klassenname
- **`bases`**: tuple mit den Basisklassen für Vererbung (kann leer sein)
- **`attrs`**: dictionary mit den Attributnamen und -werten


Zum Beispiel:

```python
    >>> class MyShinyClass(object):
    ...       pass
```

kann manuell folgendermaßen erzeugt werden:

```python
    >>> MyShinyClass = type('MyShinyClass', (), {}) # gibt ein Klassenobjekt zurück
    >>> print(MyShinyClass)
    <class '__main__.MyShinyClass'>
    >>> print(MyShinyClass()) # erzeugt eine Instanz der Klasse
    <__main__.MyShinyClass object at 0x8997cec>
```

`MyShinyClass` ist hier gleichzeitig der Klassenname als auch der Variablenname.
Diese können unterschiedlich sein, jedoch besteht kein Grund dazu die Dinge
unnötig zu verkomplizieren.

Möchte man Attribute setzen, übergibt man diese als dictionary, z.B.:

```python
    >>> class Foo(object):
    ...       bar = True
```

kann so erzeugt werden:

```python
    >>> Foo = type('Foo', (), {'bar':True})
```

und dann wie eine normale Klasse genutzt werden:

```python
    >>> print(Foo)
    <class '__main__.Foo'>
    >>> print(Foo.bar)
    True
    >>> f = Foo()
    >>> print(f)
    <__main__.Foo object at 0x8a9b84c>
    >>> print(f.bar)
    True
```

und natürlich kann von der Klasse auch abgeleitet werden:

```python
    >>>   class FooChild(Foo):
    ...         pass
```

wird zu:

```python
    >>> FooChild = type('FooChild', (Foo,), {})
    >>> print(FooChild)
    <class '__main__.FooChild'>
    >>> print(FooChild.bar) # bar is inherited from Foo
    True
```

Möchte man Klassenmethoden hinzufügen, muss man zuerst eine Funktion mit
passender Signatur erstellen:

```python
    >>> def echo_bar(self):
    ...       print(self.bar)
    ...
```

Nun kann diese Funktion als Klassenattribut gesetzt und genutzt werden:

```python
    >>> FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})
    >>> hasattr(Foo, 'echo_bar')
    False
    >>> hasattr(FooChild, 'echo_bar')
    True
    >>> my_foo = FooChild()
    >>> my_foo.echo_bar()
    True
```

Weitere Methoden können dynamisch zur Laufzeit der Klasse zugewiesen werden,
ganz so wie bei Klassenobjekten auch:

```python
    >>> def echo_bar_more(self):
    ...       print('yet another method')
    ...
    >>> FooChild.echo_bar_more = echo_bar_more
    >>> hasattr(FooChild, 'echo_bar_more')
    True
```

Man erkennt bereits, worauf dies hinausläuft: In Python sind Klassen Objekte,
welche dynamisch zur Laufzeit erzeugt werden können.

Auf diese Weise geht auch Python vor, wenn man das Schlüsselwort `class`
verwendet. Dabei wird zur Erzeugung eine sogenannte Metaklasse (*metaclass*)
genutzt.

Was sind jetzt eigentlich Metaklassen?
===

*Metaclasses* sind das "Zeug" welches eine Klasse erzeugt.

Da in Python Klassen definiert werden um ein Objekt zu erzeugen, jedoch diese
Klassen wiederum *selbst* Objekte sind benötigen wir etwas, dass Klassenobjekte
erzeugen kann.

Genau das sind *Metaclasses*, die Klassen der Klassen. Man kann sich das so
vorstellen:

```python
    MyClass = MetaClass() # erzeuge ein Klassenobjekt..
    my_object = MyClass() # .. welches wiederum ein Objekt erzeugen kann
```

Wir hatten bereits `type` behandelt:

```python
    MyClass = type('MyClass', (), {})
```

Das funktioniert, weil `type` eine Metaklasse ist. Tatsächlich ist `type` die
Metaklasse, die allen Klassen in Python zu Grunde liegt.

Alles, wirklich *alles* in Python ist ein Objekt, seien es Integers, Strings,
Funktionen oder Klassen. Dies wird ersichtlich, wenn man das `__class__`
überprüft:

```python
    >>> age = 35
    >>> age.__class__
    <type 'int'>
    >>> name = 'bob'
    >>> name.__class__
    <type 'str'>
    >>> def foo(): pass
    >>> foo.__class__
    <type 'function'>
    >>> class Bar(object): pass
    >>> b = Bar()
    >>> b.__class__
    <class '__main__.Bar'>
```

Was ist jetzt aber die Klasse von `__class__`?

```python
    >>> age.__class__.__class__
    <type 'type'>
    >>> name.__class__.__class__
    <type 'type'>
    >>> foo.__class__.__class__
    <type 'type'>
    >>> b.__class__.__class__
    <type 'type'>
```

Eine Metaklasse ist also der Code, welche Klassenobjekte generiert, man könnte
auch "Class Factory" sagen wenn man möchte.

Die standardmäßige Metaklasse zur Objekterzeugung in Python ist `type`,
allerdings kann man auch seine eigene Metaklasse implementieren.

Metaklassen bei Klassendefinition anpassen
===

Bei Python Version *2* gibt es das das `__metaclass__` Attribut, mit dem die
Metaklasse gesetzt werden kann:

```python
    class Foo(object):
        __metaclass__ = something...
        [...]
```

Bei Python Version *3* wurde die Syntax leicht geändert in Hinblick auf ein
*keyword* argument:

```python
    class Foo(object, metaclass=something):
        ...
```

Außerdem können zusätzlich noch Attribute über Argumente zugewiesen werden:

```python
    class Foo(object, metaclass=something, kwarg1=value1, kwarg2=value2):
        ...
```

Setzt man nun die Metaklasse einer Klasse neu, wird diese genutzt, um das
Klassenobjekt zu erzeugen. Jedoch ist das nicht ganz ohne Fallstricke.

Noch bevor das Klassenobjekt im Speicher angelegt wird, sucht Python nach der
`__metaclass__` in der Klassendefinition. Wird diese nicht gefunden, wird `type`
verwendet.

Bei Ableitungen, z.B.:

```python
    class Foo(Bar):
        pass
```

passiert folgendes:

Zuerst wird nach der `__metaclass__` in `Foo` gesucht und bei Erfolg zur
Erzeugung des Klassenobjekts genutzt.

Wird die `__metaclass__` nicht gefunden, sucht Python auf **Modulebene** nach
einer `__metaclass__`.

Ist das nicht erfolgreich wird `Bar`'s Metaklasse verwendet. Zu beachten ist
hierbei jedoch, dass `__metaclass__` von `Bar` nicht vererbt wird,
`Bar.__class__` jedoch schon!

Was kann man nun als `__metaclass__` nutzen?

Prinzipiell alles, was eine Klasse erzeugen kann, prinzipiell immer ähnlich zu
`type` mit der Signatur `type(name, bases, attrs)`.

Angepasste Metaklassen
===

Der Hauptzweck einer Metaklasse ist die automatische Veränderung einer Klasse
bei ihrer Erzeugung.

Üblicherweise macht man das bei APIs, bei denen man Klassen erzeugen möchte, die
zum aktuellen Kontext passen.

Metaklassen sind deshalb relativ komplex, weil man üblicherweise etwas
involviertere Dinge damit macht, die auf Introspektion aufbauen, Vererbung
manipulieren oder mit Variablen wie `__dict__` arbeiten.

An und für sich sind Metaklassen relativ simpel, den sie machen nichts weiter
als:

- Abfangen der Erzeugung der Klasse
- Modifikation der Klasse
- Rückgabe der modifizierten Klasse

Warum eine Metaklasse Klasse nutzen anstelle einer Funktion?
===

Mehrere Gründe sprechen dafür:

- Die Intention ist klar. Z.B. bei `UpperAttrMetaclass(type)` weiß man was
  passiert
- Man OOP nutzen. Metaklassen können von Metaklassen erben, Methoden
  überschreiben und selbst wiederum Metaklassen nutzen
- Unterklassen einer Klasse sind Instanzen der angegebenen Metaklasse, jedoch
  nicht bei einer Metaklassen-Funktion
- Strukturierter Code. Metaklassen sind üblicherweise kompliziert und aufwendig,
  daher ist es sinnvoll mehrere Methoden anzulegen und diese in einer Klasse zu
  gruppieren
- Die Methoden `__new__`, `__init__` und `__call__` können überschrieben und
  genutzt werden.
- Es heißt nicht umsonst Meta**klasse** ;)

Warum sollte man überhaupt Metaklassen nutzen?
===

Üblicherweise eigentlich gar nicht:

> Metaclasses are deeper magic that 99% of users should never worry about it.
> If you wonder whether you need them, you don't (the people who actually need
> them to know with certainty that they need them and don't need an explanation
> about why).

  *Python Guru Tim Peters*

Der klassische Anwendungsfall für Metaklassen sind APIs. Ein typisches Beispiel
dazu ist die Django ORM. Dort ist es möglich etwas in der nachfolgenden zu
definieren:

```python
    class Person(models.Model):
        name = models.CharField(max_length=30)
        age = models.IntegerField()
```

Wenn man jedoch folgenden Code ausführt:

```python
    person = Person(name='bob', age='35')
    print(person.age)
```

wird ein `int` zurück gegeben, der sogar direkt aus einer Datenbank stammen
kann.

Dies ist möglich, weil `models.Model` eine `__metaclass__` definiert, welche die
einfache Definition von `Person` in einen komplexen Datenbankaufruf wandelt.

Django lässt dadurch etwas komplexes sehr simpel erscheinen, indem es eine eine
einfache API anbietet und Metaklassen nutzt, um den komplexen Code im
Hintergrund zu verstecken.

Zum Schluss
==

Wie bereits gesagt, ist alles in Python eine Klasse und entweder eine Instanz
einer Klasse oder einer Metaklasse. Außer `type`. `type` ist eine eigene
Metaklasse, die sich nicht ohne weiteres in purem Python reproduzieren lässt.
Die tatsächliche Implementierung "cheatet" ein bisschen.

Außerdem sind Metaklassen ziemlich kompliziert. Für einfache
Klassenmanipulationen gibt es zwei andere Techniken, die einfacher und weniger
fehlerbehaftet sind:

- [monkey patching](http://en.wikipedia.org/wiki/Monkey_patch)
- class decorators

Die meiste Zeit ist man besser damit beraten diese zu nutzen anstelle von
Metaklassen. Die allermeiste Zeit braucht man Klassenmanipulation jedoch
überhaupt nicht.

Übung 1
==

Schreibe ein Funktion, die für alle Klassen auf Modulebene die Namen aller
Attribute in Großbuchstaben umwandelt.

Übung 2
==

Schreibe eine Metaklasse, welche dieselbe Funktion wie in Übung 1 erfüllt,
jedoch nur für eine Klasse, welche von ihr ableitet.
