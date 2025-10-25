# app.py
from flask import Flask, render_template, request, redirect, url_for
from scanner import run_scan
from db import get_findings, init_db
import threading

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        target = request.form.get("target")
        # Launch scan in background thread so web UI stays responsive
        t = threading.Thread(target=run_scan, args=(target,))
        t.daemon = True
        t.start()
        return redirect(url_for("index"))
    findings = get_findings()
    return render_template("index.html", findings=findings)

@app.route("/findings")
def findings():
    items = get_findings(500)
    return render_template("findings.html", findings=items)

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
