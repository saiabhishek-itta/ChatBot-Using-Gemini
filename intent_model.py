import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Load the dataset
data_database = {
        "What are the family travel packages you are offering?",#1
        "Do you have any discounts on flights?",#3
        "Can you tell me about your hotel amenities?",#5
        "How can I cancel my booking?",#6
        "What time does the next flight to New York depart?",#9
        "What are all flights available from Hyderabad to Chennai?",
        "What is the price of a flight from Mumbai to Delhi?",
        "Which flights originate from Bangalore?",
        "What is the destination of flight with flight_id 101?",
        "List all flights priced below 5000.",
        "How many flights are there from Delhi to Mumbai?",
        "What are the details of the cheapest flight from Chennai to Kolkata?",
        "Which flights have a price greater than 7000?",
        "List all destinations that have flights from Hyderabad.",
        "What are the details of the flight with flight_id 202?",
        "What is the price of the most expensive flight from Mumbai?",
        "List all flights available from Pune.",
        "How many flights are available to Kolkata?",
        "What is the price of flights from Delhi?",
        "List all packages available for Goa.",
        "What is the price of a package to Manali?",
        "Which packages are of type 'honeymoon'?",
        "What are the details of the package with package_id 303?",
        "List all packages priced below 10000.",
        "What is the destination place for package_id 404?",
        "Which packages are available for Kerala?",
        "What is the price of the most expensive package to Goa?",
        "List all packages with 'adventure' type.",
        "How many packages are available to Ladakh?",
        "What are the details of the package with package_id 505?",
        "What is the price of the cheapest package to Andaman?",
        "List all packages available for Rajasthan.",
        "Which packages have a price greater than 15000?",
        "How many packages are available to Shimla?",
        "What is the price of packages to Jaipur?",
        "What are all hotels available in Mumbai?",
        "What is the price of a hotel in Goa?",
        "Which hotels are located in Delhi?",
        "What are the details of the hotel with hotel_id 606?",
        "List all hotels priced below 3000.",
        "How many hotels are there in Bangalore?",
        "What is the price of the most expensive hotel in Chennai?",
        "List all hotels available in Hyderabad.",
        "How many hotels are available in Kolkata?",
        "What are the details of the hotel with hotel_id 707?",
        "What is the price of the cheapest hotel in Pune?",
        "Which hotels have a price greater than 5000?",
        "List all hotels available in Jaipur.",
        "What is the name of the hotel with hotel_id 808?",
        "How many hotels are available in Manali?",
        "What are the details of the hotel with hotel_id 909?",
        "What is the price of hotels in Shimla?",
        "What are the current offers available on flights?",
        "What are the current offers available on packages?",
        "What are the details of the offer with offer_id 1010?",
        "What is the price of flight with flight_id X?",
        "Which operator runs the flight with flight_id X?",
        "What are the details of the package with package_id X?",
        "How much does the hotel with hotel_id X charge?",
        "What is the destination of the flight operated by Y?",
        "What is the price of package with package_id X?",
        "Which place is covered in the package with package_id X?",
        "What is the origin of flight with flight_id X?",
        "What are the details of the offer with offer_id X?",
        "What is the price of the hotel named X?",
        "Which hotel is located in place X?",
        "What packages are available in place X?",
        "What flights are available from origin X?",
        "What flights are available to destination X?",
        "Which flights are operated by Y?",
        "How much does the package to place X cost?",
        "What is the price of the package with package_type X?",
        "What hotels are available in place X?",
        "What is the price of a flight from origin X to destination Y?",
        "Which operator runs flights to destination X?",
        "What is the package_type of the package with package_id X?",
        "What details are provided for the hotel with hotel_id X?",
        "What are the offers available on packages?",
        "What are the offers available on hotels?",
        "What are the offers available on flights?",
        "What is the place covered in the package with package_id X?",
        "How much does a flight operated by Y cost?",
        "Which package covers the place X?",
        "What flights are available from origin X by operator Y?",
        "How much does a flight to destination X cost?",
        "What are the details of the flight operated by Y to destination X?",
        "What are the details of the package type X available in place Y?",
        "Which flight goes from origin X to destination Y and costs less than Z?",
        "Which hotel in place X charges less than Y?",
        "What are the details of the offer on flight with flight_id X?",
        "What are the details of the offer on package with package_id X?",
        "Which packages cost less than X?",
        "What are the details of the package type X in place Y?",
        "What flights are available from origin X on date Y?",
        "What hotels in place X have details containing Y?",
        "Which flights to destination X have prices less than Y?",
        "Which operator offers flights from origin X to destination Y?",
        "How much does a package of type X in place Y cost?",
        "What is the hotel name with hotel_id X?",
        "Which packages have details containing Y?",
        "What are the details of flight with flight_id X?",
        "How much does a hotel in place X cost?",
        "What are the details of the offer on hotel with hotel_id X?",
        "What packages are available for less than X dollars?",
        "Which flights are operated by Y and have prices less than Z?",
        "Book a flight from singapore to london"
}

data_general = {
    "What is famous in hyderabad?",
    "What is the currency in France?",#2
    "What is the weather like in Paris?",#4
    "What are the popular tourist spots in Spain?",#7
    "What are the visa requirements for Japan?",#8
    "What is the exchange rate for USD to EUR?",#10
    "What are the top tourist attractions in Paris?",
    "What is the best time to visit Japan for cherry blossoms?",
    "How do I apply for a tourist visa to the USA?",
    "What are the most popular destinations in Italy?",
    "What is the best way to travel around Europe?",
    "What are the must-see places in New York City?",
    "How can I find cheap flights to Bali?",
    "What are the best travel apps for planning a trip?",
    "What should I pack for a week-long trip to the beach?",
    "What are the top things to do in London?",
    "How can I stay safe while traveling solo?",
    "What are the best family-friendly destinations in the world?",
    "What are the travel restrictions for visiting Australia?",
    "What are the top ski resorts in the Alps?",
    "What are the best places to visit in South America?",
    "How can I find budget accommodations in Tokyo?",
    "What are the best road trip routes in the USA?",
    "What are the must-try foods in Thailand?",
    "How can I get around in a foreign country without speaking the language?",
    "What are the top hiking trails in New Zealand?",
    "What are the best places to visit in Africa?",
    "What travel insurance options are available for international trips?",
    "What are the top things to do in Dubai?",
    "How do I find the best local experiences while traveling?",
    "What are the best destinations for a honeymoon?",
    "What are the top cultural festivals around the world?",
    "How can I travel sustainably?",
    "What are the best beach destinations in the Caribbean?",
    "What are the most scenic train journeys in the world?",
    "How can I avoid tourist traps while traveling?",
    "What are the best places to visit in India?",
    "How can I find vegetarian or vegan food while traveling?",
    "What are the top attractions in Barcelona?",
    "What are the best travel tips for visiting China?",
    "What are the best islands to visit in Greece?",
    "How can I make the most of a layover in a new city?",
    "What are the best travel accessories for long flights?",
    "What are the top adventure travel destinations?",
    "What are the best destinations for wildlife safaris?",
    "How can I find reliable travel reviews?",
    "What are the top things to do in Sydney?",
    "What are the best ways to save money while traveling?",
    "What are the best destinations for a winter vacation?",
    "What are the top museums to visit in Europe?",
    "How can I deal with travel delays and cancellations?",
    "What are the best travel credit cards for rewards?",
    "What are the must-see landmarks in Rome?",
    "What are the best places to visit in Southeast Asia?",
    "How can I stay healthy while traveling abroad?",
    "What are the top travel trends for the upcoming year?",
    "What are the top tourist attractions in Paris?",
    "How can I get from the airport to my hotel in New York City?",
    "What are the best restaurants in Tokyo?",
    "How much does a taxi cost from the airport to downtown London?",
    "What are the visa requirements for traveling to Australia?",
    "Are there any travel advisories for visiting Brazil?",
    "What is the best time of year to visit Bali?",
    "How do I book a train ticket from Rome to Florence?",
    "What are the best family-friendly activities in Orlando?",
    "How can I find cheap flights to Madrid?",
    "What are the COVID-19 travel restrictions for Germany?",
    "How do I get from the train station to my hotel in Amsterdam?",
    "What are the best hotels in Dubai?",
    "What is the exchange rate for USD to EUR?",
    "How can I rent a car in Los Angeles?",
    "What are the best hiking trails in Switzerland?",
    "How do I get a local SIM card in India?",
    "What are the must-try foods in Bangkok?",
    "What are the best beaches in the Caribbean?",
    "How can I find guided tours in Egypt?",
    "What are the customs regulations for bringing goods into Canada?",
    "How do I find public transportation options in Singapore?",
    "What are the best shopping districts in Milan?",
    "How can I stay safe while traveling in Mexico?",
    "What are the top luxury resorts in the Maldives?",
    "How do I find budget accommodations in Barcelona?",
    "What are the best nightlife spots in Berlin?",
    "How can I get travel insurance for my trip to South Africa?",
    "What are the best historical sites in Greece?",
    "How do I navigate the subway system in Tokyo?",
    "What are the best festivals to attend in India?",
    "How do I book a ferry ride in the Greek Islands?",
    "What are the best day trips from Paris?",
    "How can I find pet-friendly hotels in San Francisco?",
    "What are the best ways to travel around Australia?",
    "How do I find English-speaking tour guides in China?",
    "What are the best museums in London?",
    "How can I get from one island to another in Hawaii?",
    "What are the best adventure activities in New Zealand?",
    "How do I get tickets for a Broadway show in New York?",
    "What are the best spa resorts in Thailand?",
    "How can I access emergency services in a foreign country?",
    "What are the best ways to experience local culture in Morocco?",
    "How do I find accessible travel options in Europe?",
    "What are the best wine regions to visit in France?",
    "How can I find travel deals and discounts?",
    "What are the best romantic destinations in Italy?",
    "How do I handle language barriers while traveling?",
    "What are the best scenic drives in the United States?",
    "How can I avoid tourist traps while traveling?"
}

data = {
    'question': [],
    'category': []
}

# Add questions from data_database with category 'database'
for question in data_database:
    data['question'].append(question)
    data['category'].append('database')

# Add questions from data_general with category 'general'
for question in data_general:
    data['question'].append(question)
    data['category'].append('general')

df = pd.DataFrame(data)
#print(df.head())

nltk.download('punkt')
nltk.download('stopwords')

# Preprocessing function
def preprocess_text(text):
    # Tokenize text
    tokens = word_tokenize(text.lower())
    # Remove stop words
    tokens = [word for word in tokens if word.isalnum() and word not in stopwords.words('english')]
    return ' '.join(tokens)

# Apply preprocessing to the dataset
df['cleaned_question'] = df['question'].apply(preprocess_text)
X_train=df['cleaned_question']
y_train=df['category']

# Convert text data to TF-IDF features and fit into logistic regression model
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# Save the model and vectorizer
joblib.dump(model, 'logistic_regression_model.pkl')
joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')







#To test, We use this generated pkl files in intent_classification
'''def classify_question(question):
    cleaned_question = preprocess_text(question)
    question_tfidf = vectorizer.transform([cleaned_question])
    category = model.predict(question_tfidf)[0]
    return category
question = "What are the family travel packages you are offering?"
print(classify_question(question))'''
