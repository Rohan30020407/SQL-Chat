\# 🦜 SQL Chat



An AI-powered SQL Chat application that allows users to interact with a SQL database using natural language queries.



The application uses LangChain and Groq to understand user questions, generate SQL queries, execute them against a SQLite database, and display the results through a Streamlit interface.



\## Features



\- Chat with SQL database using natural language

\- Groq LLM integration

\- LangChain SQL Agent

\- SQLite database integration

\- Automatic SQL query generation

\- Natural language database querying

\- Query results displayed in a Streamlit interface

\- Supports filtered database queries

\- Secure API key input through the Streamlit sidebar



\## Tech Stack



\- Python

\- Streamlit

\- LangChain

\- LangChain Community

\- Groq

\- SQLite

\- SQLAlchemy



\## How It Works



1\. User enters a natural language question.

2\. LangChain SQL Agent interprets the question.

3\. Groq LLM generates the required SQL query.

4\. The SQL query is executed against the SQLite database.

5\. The result is displayed in the Streamlit interface.



\## Screenshots



\### Application Interface



!\[SQL Chat Interface](./screenshots/sql-chat-interface.png)



\### SQL Query Result



!\[SQL Query Result](./screenshots/sql-chat-query-result.png)



\### Filtered SQL Query



!\[Filtered SQL Query](./screenshots/sql-chat-filter-query.png)



\## Example Queries



\- Show all students

\- Show the students who scored more than 70 marks

\- Find students with marks greater than 80

\- Show the details of a specific student



\## Project Structure



\- `app.py` — Streamlit application and SQL chat interface

\- `sqlite.py` — SQLite database setup

\- `Student.db` — SQLite database

\- `screenshots/` — Project screenshots

\- `.gitignore` — Files excluded from Git



\## Setup



Install the required packages:



`pip install streamlit langchain langchain-community langchain-groq sqlalchemy`



Run the application:



`streamlit run app.py`



After launching the application, enter your Groq API key in the sidebar and start asking questions about the database.



\## Security



The Groq API key is entered through the Streamlit interface and is not hardcoded in the source code.



The `.env` file is excluded using `.gitignore`.



\## Author



Rohan Soni

