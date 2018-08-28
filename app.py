# coding: UTF-8

from flask import Flask, jsonify, request, make_response, abort
from flask_cors import CORS, cross_origin
from model.Post import Post
from model.Test import Test

_headers = ['Content-Type', 'Authorization']

# post = Post()

app = Flask(__name__)
cors = CORS(app, resources = {r"/posts/*" : {"origins" : "*"}})
cors = CORS(app, resources = {r"/tests/*" : {"origins" : "*"}})


@app.route("/tests")
@cross_origin(origin = '*', headers = _headers)
def tests():
    return tests_()


@app.route("/tests/")
@cross_origin(origin = '*', headers = _headers)
def tests_():
    return jsonify([test.to_dict() for test in Test.select()])


@app.route("/")
def index():
    return posts_()


@app.route("/posts")
def posts():
    return posts_()


@app.route("/posts/")
@cross_origin(origin = '*', headers = _headers)
def posts_():
    return jsonify([post.to_dict() for post in Post.select()])


@app.route('/posts/<int:id_post>')
def post(id_post):
    try:
        post = Post.get(id=id_post)
        return jsonify(post.to_dict())
    except Post.DoesNotExist:
        abort(404)


@app.route('/posts/new_post', methods=['POST'])
@cross_origin(origin='*', headers=_headers)
def new_post():
    data_from_client = request.json
    post = Post(title = data_from_client['title'],
                content = data_from_client['content'],
                emitDate = data_from_client['emitDate'],
                expireDate = data_from_client['expireDate'])
    post.save()
    
    return _jsonify(200, 'Postagem salva com sucesso!')


@app.route('/posts/<int:id_post>', methods = ['PUT', 'PATCH'])
@cross_origin(origin = '*', headers = _headers)
def edit_post(id_post):
    data_from_client = request.json

    try:
        post_from_db = Post.get(id = id_post)
    except Post.DoesNotExist:
        abort(404)

    post_from_db.title = data_from_client['title']
    post_from_db.content = data_from_client['content']
    post_from_db.emitDate = data_from_client['emitDate']
    post_from_db.expireDate = data_from_client['expireDate']
    post_from_db.save()

    return _jsonify(200, 'Postagem salva com sucesso!')


@app.route('/posts/<int:id_post>', methods = ['DELETE'])
@cross_origin(origin = '*', headers = _headers)
def del_post(id_post):
    try:
        post_from_db = Post.get(id = id_post)
        post_from_db.delete_instance()

        return _jsonify(200, 'Postagem excluída com sucesso!')
    except Post.DoesNotExist:
        abort(404)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def _jsonify(id_status, message):
    return jsonify({'status': id_status, 'mensagem': message})

if __name__ == '__main__':
    app.run(debug = True)
