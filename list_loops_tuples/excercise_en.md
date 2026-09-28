### Task: Lists, Loops and Tuples

The goal is to write a console program that accepts user input. The user of the program is asked for the parameters of a vehicle.
These include:
 * Manufacturer
 * Model name
 * HP
 * Number of seats
 * Top speed


```text
+------------------------------------------------------+
|  $ python vehicles.py                                |
+------------------------------------------------------+
|                                                      |
|  === Vehicle entry ===                               |
|                                                      |
|  Manufacturer   : Volkswagen                         |
|  Model name     : ID3                                |
|  HP             : 200                                |
|  Number of seats: 4                                  |
|  Top speed (km/h): 220                               |
|                                                      |
|  Vehicle saved.                                      |
|  Enter another vehicle? (y/n): y                     |
|                                                      |
|  === Vehicle entry ===                               |
|                                                      |
|  Manufacturer   : Audi                               |
|  Model name     : _                                  |
|                                                      |
+------------------------------------------------------+
```


Once a vehicle has been entered completely, the user should be asked whether they want to enter another vehicle.

The values (manufacturer, model name, ...) should be stored as appropriate data types in a tuple. The tuples in turn are stored in a list.
The resulting structure looks like this: `vehicles = [('Volkswagen', 'ID3', 200, 4, 220), ('Audi', ... )]`

When the user decides they have entered enough vehicles, all vehicles are printed in tabular form.

Steps:
1. Write a loop for the vehicle input.
2. Validate the entered values (manufacturer and model name are strings; HP, number of seats and top speed are numbers).
3. Extend the validation with a plausibility check (HP greater than 30 and less than 300, at least 2 seats, ...).
4. Store the values in a tuple.
5. Store the tuples in a list.
6. Print the list in a presentable way.

Bonus task:
Make sure that only cars from the brands Volkswagen, Audi, Skoda and Porsche can be entered.

Note: Storing the data in a database or text file is not required. The data is only kept for the runtime of the program.

Bonus task:
Move as many operations as possible into functions to make the program more readable and maintainable.
