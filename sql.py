from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
#import google.generativeai as genai
## Configure Genai Key

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
prompt=[
    """
    You are an expert in converting English questions to SQL queries! The database consists of three tables: flights, packages, and holidays, each with the following columns:

    flights: flightid, origin, destination, cost
    packages: packageid, package_type, details, cost
    holidays: holidayid, region, details, cost
    
    For example:

    Example 1: How many flight are present that go to Hyderabad from Boston?
    The SQL command will be: SELECT COUNT(*) FROM flights where origin='Boston' and destination='Hyderabad';

    Example 2: Tell me all the packages that are of type "Luxury".
    The SQL command will be: SELECT * FROM packages WHERE package_type='Luxury';

    Please note that the output should have SQL code alone and should not have ``` at the beginning or end, and the word "sql" should not appear in the output.
    """
]

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"travel.db")
    st.subheader("The REsponse is")
    for row in response:
        print(row)
        st.header(row)