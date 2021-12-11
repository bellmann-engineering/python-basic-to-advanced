# Was ist Unit-Testing?

Beim Unit-Test wird einen Teil des Codes isoliert. Die einzelnen Codes werden auf Funktionalitäten überprüft. Die Tests validieren das Verhalten und die Funktion des Codes.

Unit-Tests werden in der Regel in der Entwicklungsphase durchgeführt. Diese Tests werden normalerweise von Entwicklern durchgeführt, können aber in der Praxis von Qualitätsmanagern durchgeführt werden.

Einige Entwickler sind der Meinung, dass diese Tests Zeitverschwendung sind und vermeiden diese ganz und sind im Glauben, dass die Zeit effektiver verwendet werden kann.


# Warum das nicht so ist?

Durch die Durchführung werden Fehler früh erkannt – Fehler, die ohne Unit-Test erst in fortgeschritteneren Phasen wie System-, Integrations- oder sogar Beta-Test erkannt werden würden.

Die regelmäßige Durchführung von Unit-Tests bedeutet letztlich Zeit- und Kostenersparnis.


# Vorteile:


Wenn Sie sich noch nicht sicher sind, warum Sie Unit-Testing in Ihren Alltag als Entwickler einbinden sollten, gibt es hier einige Gründe die dafür sprechen:

- Der Unit-Test zeigt, ob die Codelogik angemessen ist und funktioniert.
- Es verbessert die Lesbarkeit des Codes. Entwicklern verstehen dadurch den Quellcode schneller und Änderungen sind leichter zu implementieren.
- Unit-Tests sind auch als Projektdokumentation geeignet.
- Die Tests werden in wenigen Millisekunden durchgeführt, so dass Sie Hunderte von Tests in sehr kurzer Zeit durchführbar sind.
- Der Unit-Test ermöglicht es Entwicklern, eine mangelhafte Codeänderung früh genug zu überarbeiten und sicherzustellen, dass alle Elemente ordnungsgemäß funktionieren. Zu diesem Zweck werden für alle Funktionen und Methoden Testfälle geschrieben, so dass Fehler einer Codeänderung schnell identifiziert und behoben werden.
- Die endgültige Qualität des Codes wird sich verbessern, da aufgrund kontinuierlicher Tests der Code fehlerfrei und qualitativ hochwertig sein wird.
- Da Unit Testing den Code in Elemente unterteilt, können Abschnitte getestet werden, ohne auf die Fertigstellung einzelner Bausteine warten zu müssen.



# Struktur-Prinzip eines eines Tests:
    
    # Wir müssen das Paket 'inittest' importieren
    # Es gibt verschiedene Test-Framework
    
    import unittetst

    # Anschließend wrapt man seine tests in einer Klasse
    # Die Klasse muss von 'unittest.TestCaste' erben, damit sie später erkannt wird.
    
    class MyTest(unittest.TestCase):
        
    
        #Innerhalb der Test-Definition werden die Tes-Methoden geschrieben
        #Zwei der Methoden sind sehr wichtig: 'setUp'(wird vor jedem Test aufgerufen) 'tearDown'(wird nach jedem Test aufgerufen)
        
        def setUp(self):
            print('setUp MyTest')

        def test_A(self):
            print('test_A')

        def test_B(self):
            print('test_B')

        def test_C(self):
            print('test_C')

        def tearDown(self):
            print('tearDown')

        # Wenn man den Test ausführt, dann wird Python alle Methoden suchen, die mit 'test' anfangen im Namen und die ausführen.
        # Die Ausführung: Es wird zuerst 'setUp' aufgerufen, dann 'test_A', dann 'tearDown'. 
        # Dann wird wieder 'setUp' auferufen, dann 'test_B', dann 'tearDown usw. 


# Ausgabe

        Ran 3 tests in 0.003s

        OK

        setUp MyTest
        test_A
        tearDown
        setUp MyTest
        test_B
        tearDown
        setUp MyTest
        test_C
        tearDown

        Process finished with exit code 0
