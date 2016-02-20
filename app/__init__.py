from flask import Flask

app = Flask(__name__)
# Don't import views before app is declared.
from app import views
