
##### Technical Description
- [Outdoors App](#OA)
1. [Description](#Description)
1. [Routes](#Routes)
1. [Misc](#Misc)


### [Description](#Description)
<a name="OA--Description"></a><a name="Description"></a>
<details>
This application recommends outdoor clothing based on temperature ranges at a location.

It uses SQLAlchemy to create a db schema with two tables, Clothing and Ranges. They each have a many-to-many relationship via the Recommendations join table.  Each Clothing item can be recommended for multiple Ranges and each Range can 'recommend' multiple Clothing items.

The models.py file shows Ranges and Clothing classes with attributes defined as columns. 

The join table is defined as a table object - hence, the two foreign key columns.

Instances of the Ranges and Clothing classes are created and then added to the database via the 'session' object.... the instances represent the comvination of clothing items and temperature ranges the application recommends to the user.
</details>

[Back to Top](#table-of-contents)

### [Routes](#Routes)
<a name="OA--Routes"></a><a name="Routes"></a>

'/' (Welcome Message): Returns a welcome message for users interested in outdoor adventures.

'/ranges' (Temperature Ranges): Queries the database for all temperature ranges and returns them in JSON format.

'/clothing' (Clothing Items): Queries the database for all clothing items and returns them in JSON format.

'/clothing/int:clothing_id/ranges' (Clothing with Ranges): Takes a clothing item ID as a parameter, retrieves the item from the database, and returns its associated temperature ranges in JSON format.

[Back to Top](#table-of-contents)

### [Misc](#Misc)
<a name="OA--Misc"></a><a name="Misc"></a>

**Database**
The application uses an SQLite database named 'outdoors.db' with two tables:

* Ranges: Stores information about temperature ranges, including range_name, min_temp, and max_temp.

* Clothing: Stores information about clothing items, including generic_name and function, with a many-to-many relationship with the Ranges table.

**Usage**
Visit the following routes in your browser or through API requests:

Welcome Message: http://localhost:5000/

Temperature Ranges: http://localhost:5000/ranges

Clothing Items: http://localhost:5000/clothing



Clothing with Ranges (replace {clothing_id} with the desired ID): http://localhost:5000/clothing/{clothing_id}/ranges
