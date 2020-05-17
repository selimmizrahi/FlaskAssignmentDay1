from flask import Flask, json
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

#
# @app.route('/posts/')
# def post_id():
#     p = requests.get('https://jsonplaceholder.typicode.com/posts')
#     posts = p.json()
#     response = app.response_class(
#         response=json.dumps(posts),
#         status=200,
#         mimetype='application/json'
#     )
#     return response
#
# @app.route('/posts/<userId>')
# def post_id(userId):
#     p = requests.get('https://jsonplaceholder.typicode.com/posts/?userId=' + userId)
#     posts = p.json()
#     response = app.response_class(
#         response=json.dumps(posts),
#         status=200,
#         mimetype='application/json'
#     )
#     return response
#


@app.route("/posts/<userId>/comments")
def get_comments(userId):
   post_response = requests.get("https://jsonplaceholder.typicode.com/posts/"+userId+"/comments")
   posts = post_response.json()

   response = app.response_class(
       response=json.dumps(posts),
       status=200,
       mimetype="application/json"
   )
   return response


if __name__ == "__main__":
    app.run()

