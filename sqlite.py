import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("travel.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

## create the table
tables_flights="""
CREATE TABLE flights (
    flightid PRIMARY KEY,
    origin TEXT,
    destination TEXT,
    cost DECIMAL
);
"""
tables_packages="""
CREATE TABLE packages (
    packageid PRIMARY KEY,
    package_type TEXT,
    details TEXT,
    cost DECIMAL
 );
"""
tables_holidays="""
CREATE TABLE holidays (
    holidayid PRIMARY KEY,
    region TEXT,
    details TEXT,
    cost DECIMAL
 );
"""
cursor.execute(tables_flights)
cursor.execute(tables_packages)
cursor.execute(tables_holidays)
## Insert Some more records

cursor.execute('''
               INSERT INTO 
               flights (flightid, origin, destination, cost) 
               VALUES
               (1, 'Singapore', 'London', 1200.00),
               (2, 'New York', 'Tokyo', 1500.00),
               (3, 'Los Angeles', 'Sydney', 1800.00),
               (4, 'Paris', 'Dubai', 900.00),
               (5, 'Berlin', 'Cape Town', 1300.00);
               ''')


cursor.execute('''
               INSERT INTO 
               packages (packageid, package_type, details, cost) 
               VALUES
               (1, 'Economy', 'Includes flight and 3-star hotel', 1500.00),
               (2, 'Luxury', 'Includes flight, 5-star hotel, all meals, and private tours', 5000.00),
               (3, 'Adventure', 'Includes flight, camping gear, and guided adventure activities', 3000.00),
               (4, 'Standard', 'Includes flight, hotel, and breakfast', 2000.00),
               (5, 'Deluxe', 'Includes flight, 5-star hotel, breakfast, and guided tours', 3500.00);  
               ''')


cursor.execute('''
               INSERT INTO 
               holidays (holidayid, region, details, cost) 
               VALUES
               (1, 'Asia', 'Cultural tour including visits to Tokyo, Seoul, and Beijing', 4000.00),
               (2, 'Africa', 'Safari holiday package including visits to Kenya, Tanzania, and South Africa', 6000.00),
               (3, 'South America', 'Exploration tour including visits to Brazil, Argentina, and Peru', 4500.00),
               (4, 'Europe', 'Family holiday package including visits to Paris, Rome, and Barcelona', 5000.00);
               ''')



#cursor.execute('''Insert Into STUDENT values('Sudhanshu','Data Science','B',100)''')
#cursor.execute('''Insert Into STUDENT values('Darius','Data Science','A',86)''')
#cursor.execute('''Insert Into STUDENT values('Vikash','DEVOPS','A',50)''')
#cursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','A',35)''')

## Disspaly ALl the records

'''print("The inserted records are")
data=cursor.execute(''Select * from STUDENT'')
for row in data:
    print(row)'''

## Commit your changes int he databse
connection.commit()
connection.close()