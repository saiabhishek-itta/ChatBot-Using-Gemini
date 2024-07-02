from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Example dataset
queries = [
    ("What is the capital of France?", "general"),
    ("Get student data with marks 123", "database"),
    ("What is the population of Japan?", "general"),
    ("Get the section of the student named John.", "database"),
    ("Who is the president of the United States?", "general"),
    ("Find all students in class 10A.", "database"),
    ("What is the boiling point of water?", "general"),
    ("Retrieve the marks of students in section C.", "database"),
    ("Who painted the Mona Lisa?", "general"),
    ("List the names of students who scored less than 50 marks.", "database"),
    ("What is the capital of Italy?", "general"),
    ("Get the class of the student with marks 95.", "database"),
    ("When was the Declaration of Independence signed?", "general"),
    ("Find the section of students named Emma.", "database"),
    ("What is the largest planet in our solar system?", "general"),
    ("Retrieve the names of students in class 12B.", "database"),
    ("Who discovered penicillin?", "general"),
    ("List the marks of students in section A.", "database"),
    ("What is the speed of light?", "general"),
    ("Get the section of the student with marks 88.", "database"),
    ("Who wrote 1984?", "general"),
    ("Find all students with marks above 75.", "database"),
]

# Split dataset
X, y = zip(*queries)
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train classifier
clf = SVC()
clf.fit(X_train, y_train)

# Function to classify query
def classify_query(query):
    query_vec = vectorizer.transform([query])
    return clf.predict(query_vec)[0]

print(classify_query('Find all students with marks above 75'))