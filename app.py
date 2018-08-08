# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request, make_response, abort
from flask_cors import CORS, cross_origin
from Post import Post

_headers = ['Content-Type', 'Authorization']

app = Flask(__name__)
cors = CORS(app, resources = {r"/posts/*": {"origins":"*"}})

@app.route("/")
@app.route("/posts")
@app.route("/posts/")
@cross_origin(origin = '*', headers = _headers)
def index():
    return jsonify([post.to_dict() for post in Post.select()])

@app.route('/posts/<int:id_post>')
def post(id_post):
    try:
        post = Post.get(id = id_post)
        return jsonify(post.to_dict())
    except Post.DoesNorExist:
        _abort(404)

@app.route('/posts/new_post', methods = ['POST'])
@cross_origin(origin = '*', headers = _headers)
def new_post():
    data_from_client = request.json
    post = Post(title = data_from_client['title'],
                content = data_from_client['content'],
                emitDate = data_from_client['emitDate'],
                expireDate = data_from_client['expireDate'])
    post.save()
    
    return jsonify({'status': 200, 'mensagem': 'Postagem salva com sucesso!'})

@app.route('/posts/<int:id_post>', methods = ['PUT', 'PATCH'])
@cross_origin(origin = '*', headers = _headers)
def edit_post(id_post):
    data_from_client = request.json

    try:
        post_from_db = Post.get(id = id_post)
    except Post.DoesNotExist as e:
        _abort(404)

    post_from_db.title = data_from_client['title']
    post_from_db.content = data_from_client['content']
    post_from_db.emitDate = data_from_client['emitDate']
    post_from_db.expireDate = data_from_client['expireDate']
    post_from_db.save()

    return jsonify({'status': 200, 'mensagem': 'Postagem salva com sucesso'})

@app.route('/posts/<int:id_post>', methods = ['DELETE'])
@cross_origin(origin = '*', headers = _headers)
def del_post(id_post):
    try:
        post_from_db = Post.get(id = id_post)
        post_from_db.delete_instance()
        return jsonify({'status': 200, 'mensagem': 'Postagem excluída com sucesso'})
    except Post.DoesNotExist:
        _abort(404)

def _abort(error_cod):
    abort(error_cod)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug = True)
