#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
from models.article import Article
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/get', methods=['GET'], strict_slashes=False)
def get_article():
    """Retrieves the list of all artciles
    """
    all_articles = storage.all(Article).values()
    list_articles = []
    for article in all_articles:
        list_articles.append(article.to_dict())
    return jsonify(list_articles)

@app_views.route('/get/<id>', methods=['GET'], strict_slashes=False)
def get_article_by_id(id):
    """Retrieve an artcile from its id
    """
    if id is None:
        abort(404)
    article  = storage.get(Article, id)
    if article is None:
        abord(404)
    return jsonify(article.to_dict())

@app_views.route('/add', methods=['POST'], strict_slashes=False)
def create_article():
    """
    Creates an article
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'title' not in request.get_json():
        abort(400, description="Missing email")
    if 'body' not in request.get_json():
        abort(400, description="Missing password")

    data = request.get_json()
    instance = Article(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/update/<id>', methods=['PUT'], strict_slashes=False)
def update_article(id):
    """
    Update an article
    """
    if id is None:
        abord(400, description="id missed")
    if not request.get_json():
        abord(400, description="Not a JSON")
    
    data = request.get_json()
    article = storage.get(Article, id)
    article.title = data['title']
    article.body = data['body']
    article.save()
    
    return make_response(jsonify(article.to_dict()))

@app_views.route('/delete/<id>', methods=['DELETE'], strict_slashes=False)
def delete_article(id):
    """
    Delete an article
    """
    if id is None:
        abord(400, description="id missed")
    
    article = storage.get(Article, id)
    article.delete()
    storage.save()
    return make_response(jsonify(article.to_dict()))
