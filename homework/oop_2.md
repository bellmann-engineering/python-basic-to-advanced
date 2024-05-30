__Aufgabe 3:__

1. Erstelle eine Klasse BankAccount mit den Eigenschaften account_number, balance und owner. Definiere einen Konstruktor __init__, der diese Eigenschaften initialisiert.
2. Definiere eine Methode deposit(amount), die den angegebenen Betrag zum Kontostand hinzufügt.
3. Definiere eine Methode withdraw(amount), die den angegebenen Betrag vom Kontostand abzieht, wenn genügend Guthaben vorhanden ist, und eine entsprechende Meldung ausgibt, wenn nicht.
4. Erstelle ein Objekt account1 der Klasse BankAccount mit der Kontonummer 123456789, einem Anfangsguthaben von 1000 und dem Besitzer "Lisa Schmidt".
5. Führe eine Einzahlung von 500 auf das Konto account1 durch und gib den neuen Kontostand aus.
6. Führe eine Abhebung von 200 auf das Konto account1 durch und gib den neuen Kontostand aus.
7. Führe eine Abhebung von 1500 auf das Konto account1 durch und gib den neuen Kontostand aus.

__Aufgabe 4:__

1. Erstelle eine Unterklasse SavingsAccount der Klasse BankAccount mit der zusätzlichen Eigenschaft interest_rate. Definiere auch einen Konstruktor __init__, der zusätzlich zur Initialisierung der Eigenschaften der Elternklasse auch den Zinssatz initialisiert.
2. Definiere eine Methode apply_interest(), die die Zinsen zum Kontostand hinzufügt, basierend auf dem Zinssatz.
3. Erstelle ein Objekt savings1 der Klasse SavingsAccount mit der Kontonummer 987654321, einem Anfangsguthaben von 2000, dem Besitzer "Thomas Müller" und einem Zinssatz von 1.5% (0.015).
4. Rufe die Methode apply_interest() für das Konto savings1 auf und gib den neuen Kontostand aus.
5. Erstelle eine Unterklasse CheckingAccount der Klasse BankAccount mit der zusätzlichen Eigenschaft transaction_fee. Definiere auch einen Konstruktor __init__, der zusätzlich zur Initialisierung der Eigenschaften der Elternklasse auch die Transaktionsgebühr initialisiert.
6. Überschreibe die Methoden deposit(amount) und withdraw(amount) in der Klasse CheckingAccount, um die Transaktionsgebühr bei jeder Einzahlung und Abhebung zu berücksichtigen.
7. Erstelle ein Objekt checking1 der Klasse CheckingAccount mit der Kontonummer 1122334455, einem Anfangsguthaben von 1500, dem Besitzer "Eva Becker" und einer Transaktionsgebühr von 2.
8. Führe eine Einzahlung von 300 auf das Konto checking1 durch und gib den neuen Kontostand aus.
9. Führe eine Abhebung von 100 auf das Konto checking1 durch und gib den neuen Kontostand aus.
