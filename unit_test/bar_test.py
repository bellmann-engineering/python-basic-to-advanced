import unittest

from bar import Bar

class BarTest(unittest.TestCase):

    #setUp-Methode in der immer eine neue Instanz der Klasse Bar erzeugt
    def setUp(self):
        self.bar = Bar()

    #Überprüfen, ob der Wert richtig initialisiert worden ist.
    def test_init(self):
        self.assertEqual(self.bar.a, 42)

    #Überprüfen ob ein bestimmter Fehler geworfen wird.
    #Wird der wuenschwert-Methode 0 übergebe, so erwarten wir einen ValueError
    def test_divistnul(self):
        with self.assertRaises(ValueError):
            self.bar.wunschwert(0)

if __name__ == '__main__':
    unittest.main()