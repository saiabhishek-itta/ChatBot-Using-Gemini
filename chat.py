from dotenv import load_dotenv
from intent_classification import classify_question

load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


## Defining Prompt to generate SQL query
dbprompt=[
    """
    You are an expert in converting English questions to SQL queries. 
    The database consists of four tables: flights, packages, hotels and offers, 
    each with the following columns:

    flights: flight_id, flight_operator, origin, destination, price
    flights table sample data: (1, 'Lufthansa', 'Singapore', 'London', 1200.00)
    
    packages: package_id, package_type, place, details, price
    packages table sample data: (1, 'Nature','Kerala', 'Includes flight and 3-star hotel', 1500.00)
    package_type has 4 types Nature,Romantic,Adventure,Family

    hotels: hotel_id, hotel_name, place, details, price
    hotels table sample data: (1, 'Cassandra','Hyderabad', '3-star hotel', 1500.00)
    
    offers: offer_id, offer_on, details
    offers table sample data: (1, 'Hotels','10% off upto $250 on bookings made over $2000')
    
    For example:

    Example 1: How many flight are present that go to Hyderabad from Boston?
    The SQL command will be: SELECT COUNT(*) FROM flights where origin='Boston' and destination='Hyderabad';

    Example 2: Give me all Family packages available.
    The SQL command will be: SELECT * FROM packages WHERE package_type='Family';

    Example 3: What are prices of hotels in hyderabad.
    The SQL command will be: SELECT * FROM hotels WHERE place='Hyderabad';
    
    Please note that the output should have SQL code alone and should not have ``` at the 
    beginning or end, and the word "sql" should not appear in the output.
    """
]


#Prompt for general questions
generalprompt=[
    """
    You are an expert in assisting users with their travel queries, 
    answer these general questions from users as a travel agent. 
    If the given question has to be answered by company database 
    your response should be a string 'database' else give your complete response
    """
]


#Prompt to convert retrived sql data to natural language
datatosenprompt=[
    """
    You are an expert in converting data from SQL database questions 
    to natural language as a travel chatbot. 
    The database consists of four tables: flights, packages, hotels and offers 
    each with the following columns:

    flights: flight_id, flight_operator, origin, destination, price
    flights table sample data: (1, 'Lufthansa', 'Singapore', 'London', 1200.00)
    
    packages: package_id, package_type, place, details, price
    packages table sample data: (1, 'Nature','Kerala', 'Includes flight and 3-star hotel', 1500.00)
    
    hotels: hotel_id, hotel_name, place, details, price
    hotels table sample data: (1, 'Cassandra','Hyderabad', '3-star hotel', 1500.00)
    
    offers: offer_id, offer_on, details
    offers table sample data: (1, 'Hotels','10% off upto $250 on bookings made over $2000')

    given a question, sql query and generated table data from different tables,
    you have to convert sql table data into natural language and your 
    respose should only include this answer. if sql query has no data you 
    should answer like an agent working for travel company. 
    never include sql query in your response. 
    """
]



## Function To Load Google Gemini Model and provide queries as response
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.parts[0].text



 #To convert database table data to english to present to user
def get_gemini_dbtoenglish(question,sqlquery,dbdata,datatosenprompt):    
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([question,sqlquery,dbdata,datatosenprompt[0]])
    return response.parts[0].text

## Fucntion To retrieve query from the database
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    try:
        cur.execute(sql)
    except:
        return ""
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


#To get SQL query and convert sql data to natural language
def askquestiontodb(question):                                       
    sqlquery=get_gemini_response(question,dbprompt)
    print("Generated SQL Queries: ",sqlquery)

    # If multiple SQL queries are generated for a question we split using(';') them and execute
    queries = sqlquery.split(";")  
    results = []
    for query in queries:
        result = read_sql_query(query.strip(), "travel.db")  # Remove leading/trailing whitespace
        results.append(result)

    dbdata=results
    print("dbdata",dbdata)

    if len(dbdata) == 0:
        print("No data returned from the database using generated query.")
        return"I could not get any details for your query, please try again..."
    else:
        #Convert SQL data to natural language  
        response=get_gemini_dbtoenglish(question,sqlquery,str(dbdata),datatosenprompt)
        return response



#We categorize our question using intent_classification
def askquestion(question):
    category = str(classify_question(question))
    print(question," --- Categorized Model : ",category)

    if(category=="database"):
        return askquestiontodb(question)
        
    else:
        #Response from chatgpt will be a string 'database' if company specific data is required as per prompt
        # and we pass this question again to Database else we return LLM's general answer
        response=get_gemini_response(question,generalprompt)
        print("General Question Answer: ",response) 
        
        if(response == 'database'):
            return askquestiontodb(question)
            
        return response