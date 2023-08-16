## Question set
**Set 3: Intermediate Level**

We'll continue with a **`Rides`** table / collection for this set of problems. The schema represents a list of rides one might find in a ride-hailing app like Uber. Each ride has an **`id`**, **`driver_id`**, **`passenger_id`**, **`start_location`**, **`end_location`**, **`distance`** (in miles), **`ride_time`** (in minutes), and **`fare`** (in dollars).

**MongoDB Schema:**

```
{
  "_id": ObjectId(),
  "driver_id": ObjectId(),
  "passenger_id": ObjectId(),
  "start_location": String,
  "end_location": String,
  "distance": Number,
  "ride_time": Number,
  "fare": Number
}

```

**SQL Schema:**

```
CREATE TABLE Rides (
    id INT PRIMARY KEY,
    driver_id INT,
    passenger_id INT,
    start_location VARCHAR(255),
    end_location VARCHAR(255),
    distance DECIMAL(5,2),
    ride_time DECIMAL(5,2),
    fare DECIMAL(6,2)
);

```

**Problem 26:**

- **Prerequisite**: Understand creating tables in SQL / collections in MongoDB
- **Problem**: Create a **`Rides`** table / collection with the fields defined above.

**Problem 27:**

- **Prerequisite**: Understand inserting data into SQL tables / MongoDB collections
- **Problem**: Insert five rows / documents into the **`Rides`** table / collection with data of your choice.

**Problem 28:**

- **Prerequisite**: Understand how to order data in SQL / MongoDB
- **Problem**: Write a query to fetch all rides, ordered by **`fare`** in descending order.

**Problem 29:**

- **Prerequisite**: Understand using math operations in SQL / MongoDB
- **Problem**: Write a query to calculate the total **`distance`** and total **`fare`** for all rides.

**Problem 30:**

- **Prerequisite**: Understand how to use the AVG function in SQL / MongoDB's aggregate functions
- **Problem**: Write a query to calculate the average **`ride_time`** of all rides.

**Problem 31:**

- **Prerequisite**: Understand using string patterns in SQL (LIKE clause) / using regex in MongoDB
- **Problem**: Write a query to fetch all rides whose **`start_location`** or **`end_location`** contains 'Downtown'.

**Problem 32:**

- **Prerequisite**: Understand how to use the COUNT function in SQL / MongoDB's aggregate functions
- **Problem**: Write a query to count the number of rides for a given **`driver_id`**.

**Problem 33:**

- **Prerequisite**: Understand data updating in SQL / MongoDB
- **Problem**: Write a query to update the **`fare`** of the ride with **`id`** 4.

**Problem 34:**

- **Prerequisite**: Understand using GROUP BY in SQL / MongoDB's aggregate functions
- **Problem**: Write a query to calculate the total **`fare`** for each **`driver_id`**.

**Problem 35:**

- **Prerequisite**: Understand data deletion in SQL / MongoDB
- **Problem**: Write a query to delete the ride with **`id`** 2.

We'll continue with the **`Rides`** table / collection from the previous set.

**Problem 36:**

- **Prerequisite**: Understand using the MAX and MIN functions in SQL / using sort and limit in MongoDB
- **Problem**: Write a query to find the ride with the highest and lowest **`fare`**.

**Problem 37:**

- **Prerequisite**: Understand using the GROUP BY clause in SQL / using aggregate in MongoDB
- **Problem**: Write a query to find the average **`fare`** and **`distance`** for each **`driver_id`**.

**Problem 38:**

- **Prerequisite**: Understand using HAVING clause in SQL / using match in MongoDB's aggregate pipeline
- **Problem**: Write a query to find **`driver_id`** that have completed more than 5 rides.

**Problem 39:**

- **Prerequisite**: Understand the use of INNER JOIN in SQL / Lookup in MongoDB
- **Problem**: Assuming there is another collection/table called **`Drivers`** with **`driver_id`** and **`name`** fields, write a query to find the name of the driver with the highest **`fare`**.

**Problem 40:**

- **Prerequisite**: Understand the concept of subqueries in SQL / using multiple stages in MongoDB's aggregate pipeline
- **Problem**: Write a query to find the top 3 drivers who have earned the most from fares. Return the drivers' ids and total earnings.

**Problem 41:**

- **Prerequisite**: Understand date and time functions in SQL / MongoDB
- **Problem**: Assuming there's a **`ride_date`** field of date type in the **`Rides`** table / collection, write a query to find all rides that happened in the last 7 days.

**Problem 42:**

- **Prerequisite**: Understand the concept of NULL values and how to handle them in SQL / MongoDB
- **Problem**: Write a query to find all rides where the **`end_location`** is not set.

**Problem 43:**

- **Prerequisite**: Understand the use of complex mathematical operations in SQL / MongoDB
- **Problem**: Write a query to calculate the fare per mile for each ride and return the ride ids and their fare per mile, ordered by fare per mile in descending order.

**Problem 44:**

- **Prerequisite**: Understand the use of multiple JOINs in SQL / multiple Lookups in MongoDB
- **Problem**: Assuming there's another collection/table **`Passengers`** with **`passenger_id`** and **`name`** fields, write a query to return a list of all rides including the driver's name and passenger's name.

**Problem 45:**

- **Prerequisite**: Understand how to alter table schemas in SQL / adding and modifying fields in MongoDB documents
- **Problem**: Write a query to add a **`tip`** field to the **`Rides`** table / collection.


## Answer
**CREATE RIDE TABLE**
- `CREATE TABLE Rides (
    id INT PRIMARY KEY,\n
    driver_id INT,
    passenger_id INT,
    start_location VARCHAR(255),
    end_location VARCHAR(255),
    distance DECIMAL(5,2),
    ride_time DECIMAL(5,2),
    fare DECIMAL(6,2)
);
`
- `INSERT INTO Rides (id, driver_id, passenger_id, start_location, end_location, distance, ride_time, fare)
VALUES
    (1, 101, 201, 'Start A', 'End A', 10.5, 25.5, 15.75),
    (2, 102, 202, 'Start B', 'End B', 8.2, 18.3, 12.50),
    (3, 103, 203, 'Start C', 'End C', 15.0, 32.0, 20.00),
    (4, 104, 204, 'Start D', 'End D', 6.5, 14.7, 9.25),
    (5, 105, 205, 'Start E', 'End E', 3.8, 8.1, 6.50);
`
            - `SELECT * FROM Rides ORDER BY fare ASC`
            - `SELECT AVG(ride_time)as avg_ride_time FROM Rides`
            - `SELECT * FROM Rides WHERE start_location LIKE '%DOWNTOWN%' or end_location LIKE %DOWNTOWN%`
            - `SELECT COUNT(*) FROM Rides WHERE driver_id=105`
            - `UPDATE Rides SET fare=34.00 WHERE id=1`
            - `SELECT driver_id, SUM(fare) AS total_fare FROM Rides GROUP BY driver_id;`
            - `DELETE FROM Rides WHERE id=2`
## Set-4
   - `SELECT  max(fare),min(fare) FROM Rides`
   - `SELECT  AVG(fare)as avg_fare,AVG(distance)as avg_distance FROM Rides GROUP BY driver_id`            
   - `SELECT driver_id, COUNT(*) AS total_rides
        FROM Rides
        GROUP BY driver_id
        HAVING COUNT(*) > 5;`Write a query to find driver_id that have completed more than 5 rides
   - `SELECT d.name
       FROM Drivers d
       JOIN Rides r ON d.driver_id = r.driver_id
       WHERE r.fare = (SELECT MAX(fare) FROM Rides);
`    
   - `SELECT TOP 3 d.driver_id, SUM(r.fare) AS total_earnings
       FROM Drivers d
       JOIN Rides r ON d.driver_id = r.driver_id
       GROUP BY d.driver_id
       ORDER BY total_earnings DESC;`       
   - `SELECT * FROM Rides WHERE ride_date BETWEEN DATE_SUB(CURRENT_DATE, INTERVAL 7 DAY) AND CURRENT_DATE;`
   - ` SELECT * FROM Rides WHERE end_location IS NULL AND start_location IS NULL`
   - `SELECT id AS ride_id,fare / distance AS fare_per_mile FROM Rides ORDER BY fare_per_mile DESC;`
   - `SELECT
    Rides.id AS ride_id,
    Drivers.name AS driver_name,
    Passengers.name AS passenger_name
FROM Rides
JOIN Drivers ON Rides.driver_id = Drivers.driver_id
JOIN Passengers ON Rides.passenger_id = Passengers.passenger_id;`
  - `ALTER TABLE Rides ADD tip DECIMAL(6, 2);`