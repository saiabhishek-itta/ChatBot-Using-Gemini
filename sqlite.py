import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("travel.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

## create the table
tables_flights="""
CREATE TABLE flights (
    flight_id PRIMARY KEY,
    flight_operator TEXT,
    origin TEXT,
    destination TEXT,
    price DECIMAL
);
"""
tables_packages="""
CREATE TABLE packages (
    package_id PRIMARY KEY,
    package_type TEXT,
    place TEXT,
    details TEXT,
    price DECIMAL
 );
"""

tables_hotels="""
CREATE TABLE hotels (
    hotel_id PRIMARY KEY,
    hotel_name TEXT,
    place TEXT,
    details TEXT,
    price DECIMAL
 );
"""
tables_offers="""
CREATE TABLE offers (
    offer_id PRIMARY KEY,
    offer_on TEXT,
    details TEXT
 );
"""


cursor.execute(tables_flights)
cursor.execute(tables_packages)
cursor.execute(tables_hotels)
cursor.execute(tables_offers)
## Insert Some more records

cursor.execute('''
               INSERT INTO 
               flights (flight_id, flight_operator, origin, destination, price) 
               VALUES
               (1, 'Lufthansa', 'Singapore', 'London', 1200.00),
               (2, 'American Airlines', 'New York', 'Tokyo', 1500.00),
               (3, 'Emirites', 'Los Angeles', 'Sydney', 1800.00),
               (4, 'Ethihad', 'Paris', 'Dubai', 900.00),
               (5, 'Virgin Atlantic', 'Berlin', 'Cape Town', 1300.00),
               (6, 'Ethihad', 'Dubai', 'Paris', 1900.00);
               ''')


cursor.execute('''
               INSERT INTO 
               packages (package_id, package_type, place, details, price) 
               VALUES
               (1, 'Nature','Kerala', 'Includes flight and 3-star hotel', 1500.00),
               (2, 'Romantic','Rome', 'Includes flight, 5-star hotel, all meals, and private tours', 5000.00),
               (3, 'Adventure','Grand Canyon', 'Includes flight, camping gear, and guided adventure activities', 3000.00),
               (4, 'Family','Paris', 'Includes flight, hotel, and breakfast', 2000.00),
               (5, 'Family', 'Italy', 'Includes flight, 5-star hotel, breakfast, and guided tours', 3500.00);  
               ''')


cursor.execute('''
               INSERT INTO 
               hotels (hotel_id, hotel_name, place, details, price) 
               VALUES
               (1, 'Cassandra','Hyderabad', '3-star hotel', 1500.00),
               (2, 'Rotesri','Rome', '3-star hotel', 5000.00),
               (3, 'Advak','Boston', '3-star hotel', 3000.00),
               (4, 'Triaci','Paris', '3-star hotel', 2000.00),
               (5, 'Family Inn', 'Italy', '3-star hotel', 3500.00);  
               ''')


cursor.execute('''
               INSERT INTO 
               offers (offer_id, offer_on, details) 
               VALUES
               (1, 'Hotels','10% off upto $250 on bookings made over $2000'),
               (2, 'Hotels','Flat $150 for Bookings made using Chase Credit Card'),
               (3, 'Flights','Get 20% off on your return ticket for roundtrip bookings'),
               (4, 'Flights','Get free lounge access with southern airlines'),
               (5, 'Packages','10% off upto $1000 on bookings made over $5000'); 
               ''')


#cursor.execute('''Insert Into STUDENT values('Sudhanshu','Data Science','B',100)''')
#cursor.execute('''Insert Into STUDENT values('Darius','Data Science','A',86)''')
#cursor.execute('''Insert Into STUDENT values('Vikash','DEVOPS','A',50)''')
#cursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','A',35)''')

## Display ALl the records

'''print("The inserted records are")
data=cursor.execute(''Select * from STUDENT'')
for row in data:
    print(row)'''

## Commit your changes int he databse
connection.commit()
connection.close()