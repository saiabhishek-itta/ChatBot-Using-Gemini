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
               (6, 'Air France', 'Paris', 'New York', 870.00),
               (7, 'British Airways', 'London', 'Los Angeles', 1300.00),
               (8, 'Singapore Airlines', 'Singapore', 'San Francisco', 1450.00),
               (9, 'Qatar Airways', 'Doha', 'London', 1250.00),
               (10, 'Cathay Pacific', 'Hong Kong', 'Vancouver', 1150.00),
               (11, 'Turkish Airlines', 'Istanbul', 'New York', 1000.00),
               (12, 'ANA', 'Tokyo', 'San Francisco', 1350.00),
               (13, 'KLM', 'Amsterdam', 'Cape Town', 1200.00),
               (14, 'Aeromexico', 'Mexico City', 'Madrid', 900.00),
               (15, 'Etihad Airways', 'Abu Dhabi', 'Sydney', 1420.00),
               (16, 'Alitalia', 'Rome', 'New York', 920.00),
               (17, 'Swiss', 'Zurich', 'Bangkok', 1280.00),
               (18, 'Air Canada', 'Toronto', 'Tokyo', 1320.00),
               (19, 'Iberia', 'Madrid', 'Chicago', 960.00),
               (20, 'Thai Airways', 'Bangkok', 'Melbourne', 1180.00),
               (21, 'Delta', 'New York', 'Paris', 850.00),
               (22, 'Emirates', 'Dubai', 'Sydney', 1400.00),
               (23, 'Qantas', 'Melbourne', 'Tokyo', 1100.00),
               (24, 'United Airlines', 'Chicago', 'Berlin', 950.00);
               ''')


cursor.execute('''
               INSERT INTO 
               packages (package_id, package_type, place, details, price) 
               VALUES
               (1, 'Nature','Kerala', 'Includes flight and 3-star hotel', 1500.00),
               (2, 'Romantic','Rome', 'Includes flight, 5-star hotel, all meals, and private tours', 5000.00),
               (3, 'Adventure','Grand Canyon', 'Includes flight, camping gear, and guided adventure activities', 3000.00),
               (4, 'Family','Paris', 'Includes flight, hotel, and breakfast', 2000.00),
               (5, 'Family', 'Italy', 'Includes flight, 5-star hotel, breakfast, and guided tours', 3500.00),
               (6, 'Romantic', 'Venice', 'Includes flight and gondola rides', 3700.00),
               (7, 'Adventure', 'New Zealand', 'Includes flight and extreme sports activities', 3400.00),
               (8, 'Family', 'Disneyland', 'Includes flight and 3-star hotel with park passes', 3000.00),
               (9, 'Nature', 'Yellowstone', 'Includes flight and cabin stay', 2000.00),
               (10, 'Romantic', 'Maldives', 'Includes flight and overwater villa', 4500.00),
               (11, 'Adventure', 'Patagonia', 'Includes flight and trekking activities', 3100.00),
               (12, 'Family', 'London', 'Includes flight and 4-star hotel with city tour', 3300.00),
               (13, 'Nature', 'Banff', 'Includes flight and lodge stay', 2700.00),
               (14, 'Romantic', 'Santorini', 'Includes flight and sunset cruise', 3800.00),
               (15, 'Adventure', 'Iceland', 'Includes flight and glacier hiking', 3600.00),
               (16, 'Family', 'Sydney', 'Includes flight and 4-star hotel with zoo tickets', 3400.00),
               (17, 'Nature', 'Bali', 'Includes flight and beach resort stay', 2900.00),
               (18, 'Romantic', 'Kyoto', 'Includes flight and traditional ryokan stay', 3200.00),
               (19, 'Adventure', 'Nepal', 'Includes flight and mountain climbing expedition', 3500.00),
               (20, 'Family', 'Dubai', 'Includes flight and 5-star hotel with desert safari', 4200.00),
               (21, 'Nature', 'Galapagos Islands', 'Includes flight and eco-cruise', 4400.00),
               (22, 'Romantic', 'Prague', 'Includes flight and river cruise', 3000.00),
               (23, 'Romantic', 'Paris', 'Includes flight and 5-star hotel', 4000.00),
               (24, 'Adventure', 'Swiss Alps', 'Includes flight and adventure activities', 3200.00),
               (25, 'Family', 'Orlando', 'Includes flight and 4-star hotel with theme park tickets', 2800.00),
               (26, 'Nature', 'Amazon Rainforest', 'Includes flight and eco-lodge stay', 2500.00);  
               ''')


cursor.execute('''
               INSERT INTO 
               hotels (hotel_id, hotel_name, place, details, price) 
               VALUES
               (1, 'Cassandra','Hyderabad', '3-star hotel', 1500.00),
               (2, 'Rotesri','Rome', '3-star hotel', 5000.00),
               (3, 'Advak','Boston', '3-star hotel', 3000.00),
               (4, 'Triaci','Paris', '3-star hotel', 2000.00),
               (5, 'Family Inn', 'Italy', '3-star hotel', 3500.00),
               (6, 'Sunny Skies', 'Barcelona', '3-star hotel with rooftop pool', 2500.00),
               (7, 'Desert Oasis', 'Dubai', '5-star luxury resort', 5000.00),
               (8, 'Forest Haven', 'Vancouver', '3-star hotel near the forest', 2000.00),
               (9, 'Seaside Resort', 'Sydney', '4-star hotel by the beach', 3200.00),
               (10, 'Historic Inn', 'Rome', '3-star hotel in historic district', 1800.00),
               (11, 'Skyline Hotel', 'Tokyo', '4-star hotel with skyline views', 3700.00),
               (12, 'Countryside Lodge', 'Edinburgh', '3-star lodge in the countryside', 2100.00),
               (13, 'Harbor View', 'San Francisco', '4-star hotel with harbor views', 3400.00),
               (14, 'Urban Retreat', 'London', '5-star luxury hotel', 4700.00),
               (15, 'Lakefront Hotel', 'Geneva', '4-star hotel by the lake', 3900.00),
               (16, 'Cultural Hub', 'Istanbul', '3-star hotel in cultural center', 1900.00),
               (17, 'Tropical Escape', 'Honolulu', '4-star hotel with tropical gardens', 3600.00),
               (18, 'Business Central', 'Shanghai', '4-star hotel in business district', 3800.00),
               (19, 'Winter Wonderland', 'Zurich', '5-star hotel with winter activities', 4800.00),
               (20, 'Island Getaway', 'Maldives', '5-star resort on a private island', 5500.00),
               (21, 'City Comfort', 'Berlin', '3-star hotel with modern amenities', 2300.00),
               (22, 'Royal Stay', 'Bangkok', '5-star hotel with royal service', 4600.00),
               (23, 'Ocean Breeze', 'Miami', '4-star beachfront hotel', 3500.00),
               (24, 'Mountain Retreat', 'Aspen', '3-star hotel with mountain views', 2200.00),
               (25, 'City Lights', 'New York', '4-star hotel in the city center', 4000.00),
               (26, 'The Grand Palace', 'Paris', '5-star hotel with city views', 4500.00);
               ''')


cursor.execute('''
               INSERT INTO 
               offers (offer_id, offer_on, details) 
               VALUES
               (1, 'Hotels','10% off upto $250 on bookings made over $2000'),
               (2, 'Hotels','Flat $150 for Bookings made using Chase Credit Card'),
               (3, 'Flights','Get 20% off on your return ticket for roundtrip bookings'),
               (4, 'Flights','Get free lounge access with southern airlines'),
               (5, 'Packages','10% off upto $1000 on bookings made over $5000'),
               (6, 'Car Rentals', '15% off on rentals above $300'),
               (7, 'Flights', '20% off on round trip bookings'),
               (8, 'Travel Insurance', 'Buy one, get one free on travel insurance'),
               (9, 'Hotels', 'Free breakfast on stays longer than 3 nights'),
               (10, 'Packages', '25% off on all-inclusive packages to Europe'),
               (11, 'Cruises', '50% off on second passenger for Mediterranean cruises'),
               (12, 'Flights', '10% cashback on all flight bookings'),
               (13, 'Car Rentals', 'Free upgrade on premium car rentals'),
               (14, 'Hotels', 'Stay 2 nights, get the 3rd night free'),
               (15, 'Travel Insurance', '10% discount on annual travel insurance plans'),
               (16, 'Packages', 'Early bird discount of 20% on summer packages'),
               (17, 'Cruises', 'Kids travel free on selected cruises'),
               (18, 'Flights', 'Earn double miles on international flights'),
               (19, 'Car Rentals', '5% off on rentals with a credit card'),
               (20, 'Hotels', 'Late checkout at no additional cost'),
               (21, 'Packages', 'Free airport transfers on select packages'),
               (22, 'Cruises', 'Free onboard credit of $100 per cabin'),
               (23, 'Travel Insurance', 'Complimentary COVID-19 coverage with your travlr travel insurance'),
               (24, 'Flights', '15% off on business class tickets'),
               (25, 'Car Rentals', '10% off for first-time customers'),
               (26, 'Hotels', 'Room upgrade on stays longer than 5 nights'); 
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