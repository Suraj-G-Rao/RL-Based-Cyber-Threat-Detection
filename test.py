from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Neo4j Credentials
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

def test_neo4j_connection():
    """Test connection to Neo4j by running `MATCH (n) RETURN n`."""
    try:
        driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
        driver.verify_connectivity()
        print("✅ Connected to Neo4j successfully!")

        with driver.session() as session:
            result = session.run("MATCH (n) RETURN n LIMIT 5")
            records = [record.data() for record in result]

            if records:
                print("🔹 Query Results:")
                for record in records:
                    print(record)
            else:
                print("⚠️ No data found in Neo4j.")
    except Exception as e:
        print(f"❌ Neo4j Connection Error: {e}")

if __name__ == "__main__":
    test_neo4j_connection()
