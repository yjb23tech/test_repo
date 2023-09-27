from flask import Flask 

#This launches and runs my server 
app = Flask(__name__)

from app import routes 