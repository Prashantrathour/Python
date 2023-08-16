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