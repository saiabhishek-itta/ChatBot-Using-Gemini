import joblib
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')



# Load the model and vectorizer
model = joblib.load('logistic_regression_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Define your preprocess_text function if needed
def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [word for word in tokens if word.isalnum() and word not in stopwords.words('english')]
    return ' '.join(tokens)


def classify_question(question):
    cleaned_question = preprocess_text(question)
    question_tfidf = vectorizer.transform([cleaned_question])
    category = model.predict(question_tfidf)[0]
    return category

def classify_cleaned_question(question_tfidf):
    category = model.predict(question_tfidf)[0]
    return category

# Example usage
if __name__ == "__main__":
    question = "What is capital of new york"
    category = classify_question(question)
    print(category)
