### Task: Lists, Loops and Tuples

The goal is to write a console program that accepts user input. The user of the program is asked for the parameters of a vehicle.
These include:
 * Manufacturer
 * Model name
 * HP
 * Number of seats
 * Top speed

```text
+-----------------------------------------------------------------------+
| PROBLEMS (1)    OUTPUT    DEBUG CONSOLE    TERMINAL                   |
|                                            ========                   |
+-----------------------------------------------------------------------+
|                                                                       |
| Manufacturer: Audi                                                    |
| Model name: A3                                                        |
| HP: 200                                                               |
| Seats: 4                                                              |
| Top speed: 200                                                        |
| Add another vehicle? (y/n): n                                         |
| +--------------+--------------+-----+-----------------+-----------+  |
| | Manufacturer | Vehicle name | HP  | Number of seats | Top speed |  |
| +--------------+--------------+-----+-----------------+-----------+  |
| |     Audi     |      A3      | 200 |        4        |    200    |  |
| +--------------+--------------+-----+-----------------+-----------+  |
| PS C:\Users\kai> _                                                    |
+-----------------------------------------------------------------------+
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

Hint: Use the [`prettytable`](https://pypi.org/project/prettytable/) library for the tabular output.
