# test/command_injection_subprocess_shell.py
import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route("/check")
def check():
    host = request.args.get("host", "")
    # Vulnerable: using shell=True with untrusted input
    out = subprocess.check_output(f"nslookup {host}", shell=True, stderr=subprocess.STDOUT)
    return out

if __name__ == "__main__":
    app.run(port=8082)
