# db.py
import sqlite3
from contextlib import closing
from config import DB_PATH

SCHEMA = """
CREATE TABLE IF NOT EXISTS endpoints (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT,
    method TEXT,
    params TEXT,
    discovered_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS findings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    endpoint_id INTEGER,
    vuln_type TEXT,
    payload TEXT,
    evidence TEXT,
    severity TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(endpoint_id) REFERENCES endpoints(id)
);
"""

def init_db():
    with closing(sqlite3.connect(DB_PATH)) as conn:
        conn.executescript(SCHEMA)
        conn.commit()

def insert_endpoint(url, method="GET", params=""):
    with closing(sqlite3.connect(DB_PATH)) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO endpoints (url, method, params) VALUES (?, ?, ?)", (url, method, params))
        conn.commit()
        return cur.lastrowid

def insert_finding(endpoint_id, vuln_type, payload, evidence, severity):
    with closing(sqlite3.connect(DB_PATH)) as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO findings (endpoint_id, vuln_type, payload, evidence, severity) VALUES (?, ?, ?, ?, ?)",
            (endpoint_id, vuln_type, payload, evidence, severity),
        )
        conn.commit()
        return cur.lastrowid

def get_findings(limit=100):
    with closing(sqlite3.connect(DB_PATH)) as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT f.id, e.url, f.vuln_type, f.payload, f.evidence, f.severity, f.created_at
            FROM findings f JOIN endpoints e ON f.endpoint_id = e.id
            ORDER BY f.created_at DESC
            LIMIT ?
        """, (limit,))
        return cur.fetchall()
