# test/vuln-cmd-py.py
import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route("/ping")
def ping():
    host = request.args.get("host", "")
    # Vulnerable: passes unsanitized user input into shell command
    cmd = f"ping -c 1 {host}"
    output = subprocess.check_output(cmd, shell=True)
    return output
