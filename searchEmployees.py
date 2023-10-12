from esConnection import es
from flask import request, jsonify

def getEmployees():

    query_value = request.args.get('query', type=str)

    resp = es.search(index="", body={
        "size":1000,
        "query": {
            "match": {
                "FirstName": {
                    "query": query_value,
                    "fuzziness": "AUTO"
                }
            }
        }
    })
    
    return jsonify(resp)