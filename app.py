"""This file contains endpoint for application"""

from flask import Flask, request, jsonify
from tree_operations import rephrase

app = Flask(__name__)


@app.route("/paraphrase", methods=["GET"])
def parse():
    params = request.args
    tree = params.get("tree")
    limit = params.get("limit")

    if not limit:
        limit = 20  # default value for limit
    if not tree:
        return jsonify({"error": "tree is required parameter"}), 400  # return error if tree parameter is missed

    response = {"paraphrases": []}
    trees = rephrase(tree, limit)
    for tree in trees:
        response["paraphrases"].append({"tree": tree})
    return jsonify(response), 200

