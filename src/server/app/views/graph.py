# https://github.com/graphql-python/flask-graphql
from flask import request, jsonify
from flask_graphql import GraphQLView
from app.data import db
from app.graph import schema
from app import app


def graph_view():
    session = db.init_session(request.form["session_id"])
    if session:
        view = GraphQLView.as_view('graph', schema=schema, graphiql=True)
        return view()
    else:
        db.context["currentUser"] = None  # Init currentUser for handling permissions
        return jsonify("Invalid session"), 400


app.add_url_rule('/graph', view_func=graph_view, methods=["POST"])

# Optional, for adding batch query support (used in Apollo-Client)
# app.add_url_rule('/graphql/batch', view_func=GraphQLView.as_view('graphql', schema=schema, batch=True))
