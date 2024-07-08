import pandas as pd

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
        "What are the details of the offer with offer_id 1010?"
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
    "What are the top travel trends for the upcoming year?"
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


# Display the first few rows of the dataset
df = pd.DataFrame(data)
#print(df.head())



import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.model_selection import train_test_split

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

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['cleaned_question'], df['category'], test_size=0.2, random_state=42)




from sklearn.feature_extraction.text import TfidfVectorizer

# Convert text data to TF-IDF features
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)






from sklearn.linear_model import LogisticRegression

# Train a Logistic Regression model
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# Evaluate the model
y_pred = model.predict(X_test_tfidf)





from sklearn.metrics import classification_report, accuracy_score

# Print classification report
print(classification_report(y_test, y_pred))

# Print accuracy score
print('Accuracy:', accuracy_score(y_test, y_pred))






#To test
def classify_question(question):
    cleaned_question = preprocess_text(question)
    question_tfidf = vectorizer.transform([cleaned_question])
    category = model.predict(question_tfidf)[0]
    return category

# Example usage
question = "What are the family travel packages you are offering?"
print(classify_question(question))  # Output: "database"
