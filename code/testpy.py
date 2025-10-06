# test/unsafe_pickle_deserialization.py
# Vulnerable: untrusted data deserialized with pickle.loads (RCE risk)
import base64
import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route("/load", methods=["POST"])
def load():
    b64 = request.get_data(as_text=True) or ""
    try:
        raw = base64.b64decode(b64, validate=True)
        obj = pickle.loads(raw)  # ❌ VULNERABLE: arbitrary code execution
        return {"loaded_type": type(obj).__name__}
    except Exception as e:
        return {"error": str(e)}, 400

if __name__ == "__main__":
    app.run(port=8084)
