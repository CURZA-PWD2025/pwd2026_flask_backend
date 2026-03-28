from app.controllers.user_controller import UserController
from flask import request, Blueprint


users = Blueprint('users', __name__, url_prefix='/users')

@users.route('/')
def get_all():
    return UserController.get_all()
@users.route('/<int:id>')
def show(id):
    return UserController.show(id)

@users.route("/", methods=['POST'])
def create():
    return UserController.create(request.get_json())

@users.route("/<int:id>", methods=['PUT'])
def update(id):
    return  UserController.update(request=request.get_json(), id=id)
    

@users.route("/<int:id>", methods=['DELETE'])
def destroy(id):
    return UserController.destroy( id)
