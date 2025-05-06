import os
import uvicorn
import networkx as nx
from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# If you already have the official neo4j driver installed:
# pip install neo4j
from neo4j import GraphDatabase, basic_auth

# 1. Pydantic model for the request body
class GraphMLExportRequest(BaseModel):
    neo4j_url: str            # e.g., "bolt://localhost:7687"
    user: str                 # e.g., "neo4j"
    password: str             # e.g., "your12345"
    database_name: Optional[str] = "neo4j"  # optional; defaults to "neo4j"
    filename: Optional[str] = "export"      # optional filename prefix for the graphml file


# 2. Create the minimal FastAPI app
app = FastAPI()


# 3. Utility class for connecting to Neo4j
class CustomNeo4jDatabase:
    def __init__(self, host: str, user: str, password: str):
        self.driver = GraphDatabase.driver(host, auth=basic_auth(user, password))

    def query(self, query: str, database: str = None):
        """Execute a read-only Cypher query and return the records as a list of dicts."""
        with self.driver.session(database=database) as session:
            return session.run(query).data()


# 4. Endpoint for exporting GraphML
@app.post("/exportGraphML")
def export_graphml(payload: GraphMLExportRequest):
    """
    Connects to a specified Neo4j database, exports *all* nodes and relationships
    as a GraphML file, and saves the file in ./graphs/ folder.
    """
    try:
        # 4.1) Build a Neo4j connection with provided details
        custom_connection = CustomNeo4jDatabase(
            host=payload.neo4j_url,
            user=payload.user,
            password=payload.password
        )

         # 4.2) Fetch all nodes via properties(n)
        nodes_query = """
            MATCH (n)
            RETURN id(n) AS node_id, labels(n) AS labels, properties(n) AS props
        """
        nodes_result = custom_connection.query(nodes_query, database=payload.database_name)

        # 4.3) Fetch all relationships via properties(r)
        rels_query = """
            MATCH (n)-[r]->(m)
            RETURN id(r) AS rel_id, type(r) AS rel_type,
                   id(n) AS start_id, id(m) AS end_id, properties(r) AS props
        """
        rels_result = custom_connection.query(rels_query, database=payload.database_name)

        # 4.4) Construct a NetworkX graph
        G = nx.MultiDiGraph()  # or nx.MultiGraph() if you prefer undirected

        # ---- Add nodes
        for record in nodes_result:
            node_id = record["node_id"]
            labels = record["labels"]
            props = record["props"]  # Already a dict because we used properties(n)
            props["_labels"] = labels  # Store labels so they appear in GraphML
            G.add_node(node_id, **props)

        # ---- Add relationships
        for record in rels_result:
            rel_id = record["rel_id"]
            rel_type = record["rel_type"]
            start_id = record["start_id"]
            end_id = record["end_id"]
            props = record["props"]  # Already a dict because we used properties(r)
            props["_type"] = rel_type
            # Use rel_id as the 'key' in a MultiDiGraph to support multi-edges
            G.add_edge(start_id, end_id, key=rel_id, **props)

        # 4.5) Determine output filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{payload.filename}_{timestamp}.graphml"
        graphs_dir = os.path.join(os.getcwd(), "graphs")
        os.makedirs(graphs_dir, exist_ok=True)
        file_path = os.path.join(graphs_dir, filename)

        # 4.6) Write out GraphML
        nx.write_graphml(G, file_path)

        # 4.7) Return success info
        return {
            "message": "GraphML export successful",
            "file_path": file_path,
            "nodes_count": G.number_of_nodes(),
            "edges_count": G.number_of_edges()
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 5. Run the app on port 3000 if executed directly
if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=3000, reload=False)
