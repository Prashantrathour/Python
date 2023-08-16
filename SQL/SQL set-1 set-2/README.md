## Questions 
**Problem 1:**

- **Prerequisite**: Understand creating tables in SQL / collections in MongoDB
- **Problem**: Create a **`Customers`** table / collection with the following fields: **`id`** (unique identifier), **`name`**, **`email`**, **`address`**, and **`phone_number`**.

**Problem 2:**

- **Prerequisite**: Understand inserting data into SQL tables / MongoDB collections
- **Problem**: Insert five rows / documents into the **`Customers`** table / collection with data of your choice.

**Problem 3:**

- **Prerequisite**: Understand basic data fetching in SQL / MongoDB
- **Problem**: Write a query to fetch all data from the **`Customers`** table / collection.

**Problem 4:**

- **Prerequisite**: Understand how to select specific fields in SQL / MongoDB
- **Problem**: Write a query to select only the **`name`** and **`email`** fields for all customers.

**Problem 5:**

- **Prerequisite**: Understand basic WHERE clause in SQL / MongoDB's find method
- **Problem**: Write a query to fetch the customer with the **`id`** of 3.

**Problem 6:**

- **Prerequisite**: Understand using string patterns in SQL (LIKE clause) / using regex in MongoDB
- **Problem**: Write a query to fetch all customers whose **`name`** starts with 'A'.

**Problem 7:**

- **Prerequisite**: Understand how to order data in SQL / MongoDB
- **Problem**: Write a query to fetch all customers, ordered by **`name`** in descending order.

**Problem 8:**

- **Prerequisite**: Understand data updating in SQL / MongoDB
- **Problem**: Write a query to update the **`address`** of the customer with **`id`** 4.

**Problem 9:**

- **Prerequisite**: Understand how to limit results in SQL / MongoDB
- **Problem**: Write a query to fetch the top 3 customers when ordered by **`id`** in ascending order.

**Problem 10:**

- **Prerequisite**: Understand data deletion in SQL / MongoDB
- **Problem**: Write a query to delete the customer with **`id`** 2.

**Problem 11:**

- **Prerequisite**: Understand how to count rows / documents in SQL / MongoDB
- **Problem**: Write a query to count the number of customers.

**Problem 12:**

- **Prerequisite**: Understand how to skip rows / documents in SQL / MongoDB
- **Problem**: Write a query to fetch all customers except the first two when ordered by **`id`** in ascending order.

**Problem 13:**

- **Prerequisite**: Understand filtering with multiple conditions in SQL / MongoDB
- **Problem**: Write a query to fetch all customers whose **`id`** is greater than 2 and **`name`** starts with 'B'.

**Problem 14:**

- **Prerequisite**: Understand how to use OR conditions in SQL / MongoDB
- **Problem**: Write a query to fetch all customers whose **`id`** is less than 3 or **`name`** ends with 's'.

**Problem 15:**

- **Prerequisite**: Understand how to use NULL checks in SQL / MongoDB
- **Problem**: Write a query to fetch all customers where the **`phone_number`** field is not set or is null.
**Set 2: Beginner Level - Advanced**

We will be using a **`Restaurants`** table / collection for this set of problems. The schema represents a list of restaurants like one might find in a delivery app like Zomato. Each restaurant has an **`id`**, **`name`**, **`cuisine_type`** (e.g., Italian, Chinese), **`location`**, **`average_rating`**, and **`delivery_available`** (a boolean indicating if delivery is available).

**MongoDB Schema:**

```
{
  "_id": ObjectId(), 
  "name": String,
  "cuisine_type": String,
  "location": String,
  "average_rating": Number,
  "delivery_available": Boolean
}
```

**SQL Schema:**

```
CREATE TABLE Restaurants (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    cuisine_type VARCHAR(100),
    location VARCHAR(255),
    average_rating DECIMAL(3,2),
    delivery_available BOOLEAN
);

```

**Problem 16:**

- **Prerequisite**: Understand creating tables in SQL / collections in MongoDB
- **Problem**: Create a **`Restaurants`** table / collection with the fields defined above.

**Problem 17:**

- **Prerequisite**: Understand inserting data into SQL tables / MongoDB collections
- **Problem**: Insert five rows / documents into the **`Restaurants`** table / collection with data of your choice.

**Problem 18:**

- **Prerequisite**: Understand how to order data in SQL / MongoDB
- **Problem**: Write a query to fetch all restaurants, ordered by **`average_rating`** in descending order.

**Problem 19:**

- **Prerequisite**: Understand filtering with multiple conditions in SQL / MongoDB
- **Problem**: Write a query to fetch all restaurants that offer **`delivery_available`** and have an **`average_rating`** of more than 4.

**Problem 20:**

- **Prerequisite**: Understand how to use NULL checks in SQL / MongoDB
- **Problem**: Write a query to fetch all restaurants where the **`cuisine_type`** field is not set or is null.

**Problem 21:**

- **Prerequisite**: Understand how to count rows / documents in SQL / MongoDB
- **Problem**: Write a query to count the number of restaurants that have **`delivery_available`**.

**Problem 22:**

- **Prerequisite**: Understand using string patterns in SQL (LIKE clause) / using regex in MongoDB
- **Problem**: Write a query to fetch all restaurants whose **`location`** contains 'New York'.

**Problem 23:**

- **Prerequisite**: Understand how to use the AVG function in SQL / MongoDB's aggregate functions
- **Problem**: Write a query to calculate the average **`average_rating`** of all restaurants.

**Problem 24:**

- **Prerequisite**: Understand how to limit results in SQL / MongoDB
- **Problem**: Write a query to fetch the top 5 restaurants when ordered by **`average_rating`** in descending order.

**Problem 25:**

- **Prerequisite**: Understand data deletion in SQL / MongoDB
- **Problem**: Write a query to delete the restaurant with **`id`** 3.







**create table**

- `CREATE TABLE employee (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    salary DECIMAL(10, 2),
    department VARCHAR(50)
    );`

**INSERT DATA**
  - `INSERT INTO employee (id,name, email, salary, department) VALUES (1,'John Doe', 'john@example.com', 50000.00, 'HR'), (2,'Jane Smith'  'jane@example.com', 60000.00, 'Finance'),(3,'Michael Johnson', 'michael@example.com', 75000.00, 'IT');`

**fetch all data**
- `SELECT * from employee`
- `SELECT name,email FROM employee`
- `SELECT name,email FROM employee WHERE id==3`
- `SELECT * FROM employee WHERE name LIKE 'a%';` start with a name

- Write a query to fetch all customers, ordered by name in descending order.
  - `SELECT * FROM employee ORDER BY name DESC;` order by name descending
  - `UPDATE employee SET address = 'NEWYORK' WHERE id = 4;`
  - `SELECT TOP 3 * FROM employee ORDER BY salary DESC` select top 3 we can also use LIMIT 3
  - `DELETE customer WHERE id=3`
  - `SELECT COUNT(*) AS total_count FROM employee`
  - `SELECT * FROM employee ORDER by id ASC OFFSET 2 ROWS` skip two rows where id in ascending
  - `SELECT * FROM employee WHERE id >2 AND name LIKE 'b%'`
  - `SELECT * FROM employee WHERE id >3 AND name LIKE '%s'`
  - `SELECT * FROM employee WHERE address is NULL`

## next set-2

- `CREATE TABLE Restaurants (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    cuisine_type VARCHAR(100),
    location VARCHAR(255),
    average_rating DECIMAL(3,2),
    delivery_available BIT
    );`

- `INSERT INTO Restaurants (id, name, cuisine_type, location, average_rating, delivery_available)
    VALUES
    (1, 'The Food Haven', 'Italian', '123 Main St', 4.5, 1),
    (2, 'Spice Delight', 'Indian', '456 Oak Ave', 4.0, 1),
    (3, 'Sushi Palace', 'Japanese', '789 Elm Rd', 4.8, 0),
    (4, 'Burger Joint', 'American', '555 Maple Ln', 3.7, 1),
    (5, 'Thai Garden', 'Thai', '987 Pine Blvd', 4.2, 1);
    `
- `SELECT * FROM Restaurants ORDER BY average_rating ASC`
- `SELECT * FROM Restaurants  WHERE cuisine_type is NULL;`
- `SELECT COUNT(*) AS available FROM Restaurants  WHERE delivery_available=1;`
- `SELECT * FROM Restaurants  WHERE  location LIKE %NEW YORK%;`
- `SELECT AVG(average_rating) AS average FROM Restaurants  `
- `SELECT  TOP 5 * FROM Restaurants ORDER BY average_rating DESC`
- `DELETE * FROM Restaurants WHERE id=3`