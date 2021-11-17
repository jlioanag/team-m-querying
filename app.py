from flask import Flask, jsonify, request
import requests
import json 

from api import getDocuments, getRanking
from query import *

app = Flask(__name__)

@app.route("/search", methods=["GET"])
def search():
    
    # Load query parameters from UI/UX
    params = request.args
    raw_query = params['q']

    # Make multiple transformations on the query 
    '''
    processedQueries = process(raw_query)
    '''

    rankedOrder = getRanking(params, raw_query)
    queryResults = getDocuments(rankedOrder)

    result = createQueryResult(queryResults)

    return jsonify(result)

@app.route("/track", methods=["POST"])
def track():
    pass

if __name__ == "__main__":
    app.run(debug=True, port="8080")