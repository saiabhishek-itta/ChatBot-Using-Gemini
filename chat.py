from dotenv import load_dotenv
from intent_classification import classify_question

load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.parts[0].text

## Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
dbprompt=[
    """
    You are an expert in converting English questions to SQL queries! The database consists of three tables: flights, packages, and holidays, each with the following columns:

    flights: flight_id, origin, destination, price
    flights table sample data: (1, 'Singapore', 'London', 1200.00)
    
    packages: package_id, package_type, place, details, price
    packages table sample data: (1, 'Nature','Kerala', 'Includes flight and 3-star hotel', 1500.00)
    
    hotels: hotel_id, hotel_name, place, details, price
    hotels table sample data: (1, 'Cassandra','Hyderabad', '3-star hotel', 1500.00)
    
    offers: offer_id, offer_on, details
    offers table sample data: (1, 'Hotels','10% off upto $250 on bookings made over $2000')
    
    For example:

    Example 1: How many flight are present that go to Hyderabad from Boston?
    The SQL command will be: SELECT COUNT(*) FROM flights where origin='Boston' and destination='Hyderabad';

    Example 2: Give me all Family packages available.
    The SQL command will be: SELECT * FROM packages WHERE package_type='Family';

    Example 3: Give me all hotels available in hyderabad that cost less than 10000.
    The SQL command will be: SELECT * FROM hotels WHERE place='Hyderabad' and price < 10000;
    
    Please note that the output should have SQL code alone and should not have ``` at the beginning or end, and the word "sql" should not appear in the output.
    """
]

gnprompt=[
    """
    You are an expert in assisting users with their travel queries, answer these general questions from users as a travel agent.
    """
]


datatosenprompt[
    """
    
    """
]



def askquestion(question):
    category = str(classify_question(question))
    print(question," --- Categorized Model : ",category)

    if(category=="database"):
        response=get_gemini_response(question,dbprompt)
        print("Generated SQL Query: ",response)
        response=read_sql_query(response,"travel.db")
        if len(response) == 0:
            print("No data returned from the query.")
            return"I could not get any details for your query, please try again..."
        else:    
            return response
    else:
        response=get_gemini_response(question,gnprompt)
        print("General Question Answer: ",response)
        return response
