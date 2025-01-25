"""
File name: server_db.py
"""

# --- Imports ---
import json


# --- Constants and variables ---
SERVER_DB = "D:\SEM6\Load_bal\loadbalancer\server\server_db.json"


# --- Functions ---
def load_serverdb(server_db):
    server_info = {}
    with open(server_db, encoding="utf-8") as f:
        server_info = json.load(f)
    return server_info


server_info = load_serverdb(SERVER_DB)