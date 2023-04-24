
#  wondering what you need to wear on a hiking trip? HERE is your answer

When you run this program, it will prompt you to enter an action: "add", "delete", "update", or "quit". If you enter "add", it will prompt you to enter the generic name and function of a new clothing item, add it to the Clothing table, and print its ID. If you enter "delete", it will prompt you to enter the ID of a clothing item to delete, remove it from the Clothing table, and print its ID. If you enter "update", it will prompt you to enter the ID of an item to update, and prompt you through an edit.

Run this program in the terminal command line by typing in the command and pressing Enter:
python3 app.py

To interact with the "add", "delete", and "update" functions from the command line, you can run the main.py file in the command line using the following command:


This will start the program and prompt you with the message: "What would you like to do? (add/delete/update): ".

You can then enter one of the three actions: "add", "delete", or "update".

If you enter "add", you will be prompted to enter the generic name (like 'shoes', 'pants' etc) and the function of the clothing (like 'upper all-weather outer layer' for a rain jacket). Once you enter these values, a new Clothing object will be created and added to the table.

If you enter "delete", you will be prompted to enter the ID of the clothing to delete. If the clothing exists in the database, it will be deleted.

If you enter "update", you will be prompted to enter the ID of the clothing to update, and then the new function for the clothing. If the clothing exists in the database, its function will be updated.

After each action is completed, the program will return you to the main prompt and wait for your next action. If you enter any other input, the program will exit.



This application recommends outdoor clothing based on temperature ranges at a location.

It uses SQLAlchemy to create a db schema with two tables, Clothing and Ranges. They each have a many-to-many relationship via the Recommendations join table.  Each Clothing item can be recommended for multiple Ranges and each Range can 'recommend' multiple Clothing items.

The models.py file shows Ranges and Clothing classes with attributes defined as columns. 

The join table is defined as a table object - hence, the two foreign key columns.

Instances of the Ranges and Clothing classes are created and then added to the database via the 'session' object.... the instances represent the comvination of clothing items and temperature ranges the application recommends to the user.