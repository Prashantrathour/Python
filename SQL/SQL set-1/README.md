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