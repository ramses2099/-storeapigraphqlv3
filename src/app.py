from flask import Flask, request, jsonify, render_template
from typing import Optional
from db import init_db


# init db
init_db()

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

