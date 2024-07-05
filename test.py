# main.py

from intent1 import classify_question

# Create the model using the function from model.py
model = classify_question("What are the family travel packages you are offering?")

# Now you can use the model as needed
print(model)
