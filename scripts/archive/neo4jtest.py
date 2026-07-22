"""
Test Neo4j connection before loading the full graph.
Run this first to make sure everything is working.
"""

from neo4j import GraphDatabase

# ── Config — update password if different ──────────────────────────────────────
URI      = "neo4j://localhost:7687"
USERNAME = "neo4j"
PASSWORD = "12345678"


def test_connection():
    try:
        driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))
        with driver.session() as session:
            result = session.run("RETURN 'Connected to Neo4j!' AS msg")
            print(result.single()["msg"])

            # Check version
            version = session.run("CALL dbms.components() YIELD versions RETURN versions[0] AS version")
            print(f"Neo4j version: {version.single()['version']}")

        driver.close()
        print("\n✅ Connection successful — ready to load graph!")

    except Exception as e:
        print(f"\n❌ Connection failed: {e}")
        print("Make sure Neo4j Desktop database is started.")


if __name__ == "__main__":
    test_connection()