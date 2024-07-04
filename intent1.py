import pandas as pd

# Load the dataset
df = pd.read_csv('questions.csv')

# Display the first few rows of the dataset
print(df.head())



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




def classify_question(question):
    cleaned_question = preprocess_text(question)
    question_tfidf = vectorizer.transform([cleaned_question])
    category = model.predict(question_tfidf)[0]
    return category

# Example usage
question = "What are the family travel packages you are offering?"
print(classify_question(question))  # Output: "database"
