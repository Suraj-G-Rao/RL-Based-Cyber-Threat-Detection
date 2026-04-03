import streamlit as st
import os
import time
import groq
from neo4j import GraphDatabase

# Streamlit UI
st.set_page_config(page_title="Cyber Threat Intelligence Chatbot", layout="wide")
st.markdown("<h1 style='text-align: center;'>🔍 Cyber Threat Intelligence Chatbot</h1>", unsafe_allow_html=True)

# API Key Input
groq_api_key = st.text_input("Enter your Groq API Key", type="password")

# Neo4j Connection Details (Hardcoded Password)
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "Suraj@0203"  # Hardcoded Password

# Connect to Neo4j
def get_neo4j_driver():
    try:
        return GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    except Exception as e:
        return None, f"❌ Connection Error: {str(e)}"

driver = get_neo4j_driver()
if driver is None:
    st.stop()  # Stop execution if connection fails

# Groq API Function
def generate_cypher_query(user_input):
    """Uses Groq API to generate a Cypher query based on user input."""
    if not groq_api_key:
        return None, "❌ Groq API Key is required!"
    
    client = groq.Client(api_key=groq_api_key)
    prompt = f"""

    Convert the following natural language question into a precise Cypher query for Neo4j, based on the Cyber Knowledge Graph (CKG). The graph contains the following node labels:

GeneralInfo_CVE: (id, Data_Format, Data_Type, No_CVES, Data_Version, Timestamp)
CVE: (id, Assigner, Description, Published_Date, Last_Modified_Date, Name)
CWE: (id, Status, Description, Submission_Name, Abstraction, Modes_Of_Introduction, Extended_Description, Name, Modifications, Language, Submission_Date, Extended_Name, Alternate_Terms, Structure, Likelihood_Of_Exploit, Submission_Organization, Background_Details, Notes, Affected_Resources)
CVSS_3: (id, Attack_Vector, Base_Severity, Vector_String, User_Interaction, Confidentiality_Impact, Name, Integrity_Impact, Base_Score, Scope, Version, Availability_Impact, Privileges_Required, Attack_Complexity)
CVSS_2: (id, Integrity_Impact, Base_Score, Vector_String, Access_Complexity, Version, Authentication, Access_Vector, Availability_Impact, Confidentiality_Impact, Name)
Reference_Data: (id, url, refSource, Name)
CPE: (id, uri)

The graph also has the following relationships:

referencedBy
CVSS2_Impact
CVSS3_Impact
Problem_Type
belongsTo
applicableIn
Related_Weakness

Example conversions:

- "Get the description of CVE with ID 1" → MATCH (cve:CVE) WHERE id(cve) = 1 RETURN cve.Description
- "Retrieve the name and assigner of CVE with ID 5" → MATCH (cve:CVE) WHERE id(cve) = 5 RETURN cve.Name, cve.Assigner
- "Fetch all details of CVE with ID 10" → MATCH (cve:CVE) WHERE id(cve) = 10 RETURN cve.Name, cve.Description, cve.Assigner, cve.Published_Date, cve.Last_Modified_Date

Task: Generate a precise Cypher query for Neo4j based on the following user query:
Question: "{user_input}"

Ensure the query retrieves only the attributes explicitly requested by the user.

Output: Only return the Cypher query, without any additional text.
"""



    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )
        cypher_query = response.choices[0].message.content.strip()

        if not cypher_query.lower().startswith("match"):
            return None, "⚠️ Invalid Cypher query generated!"

        return cypher_query, None
    except Exception as e:
        return None, f"❌ Error: {str(e)}"

# Run Cypher Query
def run_cypher_query(query):
    """Executes the Cypher query and returns results."""
    try:
        with driver.session() as session:
            result = session.run(query)
            return [record.data() for record in result]
    except Exception as e:
        return f"❌ Execution Error: {str(e)}"

# User Input
user_query = st.text_input("Enter your cybersecurity query", "List all threats with high severity")

if st.button("Generate Cypher Query & Fetch Data"):
    start_time = time.time()

    # Step 1: Generate Cypher Query
    cypher_query, error = generate_cypher_query(user_query)

    if error:
        st.error(error)
    else:
        st.text_area("Generated Cypher Query:", cypher_query, height=100)

        # Step 2: Execute Query in Neo4j
        if cypher_query:
            results = run_cypher_query(cypher_query)

            if isinstance(results, str):
                st.error(results)
            elif results:
                st.success("✅ Query executed successfully!")
                st.write(results)
            else:
                st.warning("⚠️ No data found.")

    # Response Time
    response_time = round(time.time() - start_time, 5)
    st.write(f"**Response Time:** `{response_time}` seconds")
