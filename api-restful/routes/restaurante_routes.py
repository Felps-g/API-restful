from flask import Blueprint, request
from controllers.restaurante_controllers import (
    get_restaurantes,
    get_restaurante_by_id,
    get_restaurante_by_nome,
    create_restaurante,
    update_restaurante,
    delete_restaurante
)

# Define um Blueprint para as rotas de "Restaurante"
restaurante_routes = Blueprint('restaurante_routes', __name__)

# Rota para listar todos os restaurantes (GET)
@restaurante_routes.route('/Restaurante', methods=['GET'])
def restaurantes_get():
    return get_restaurantes()

# Rota para buscar um restaurante pelo ID (GET)
@restaurante_routes.route('/Restaurante/<int:restaurante_id>', methods=['GET'])
def restaurante_get_by_id(restaurante_id):
    return get_restaurante_by_id(restaurante_id)

# Rota para buscar um restaurante pelo nome (GET)
@restaurante_routes.route('/Restaurante/nome/<string:restaurante_nome>', methods=['GET'])
def restaurante_get_by_nome(restaurante_nome):
    return get_restaurante_by_nome(restaurante_nome)

# Rota para criar um novo restaurante (POST)
@restaurante_routes.route('/Restaurante', methods=['POST'])
def restaurantes_post():
    return create_restaurante(request.json)

# Rota para atualizar um restaurante pelo ID (PUT)
@restaurante_routes.route('/Restaurante/<int:restaurante_id>', methods=['PUT'])
def restaurantes_put(restaurante_id):
    return update_restaurante(restaurante_id, request.json)

# Rota para excluir um restaurante pelo ID (DELETE)
@restaurante_routes.route('/Restaurante/<int:restaurante_id>', methods=['DELETE'])
def restaurante_delete(restaurante_id):
    return delete_restaurante(restaurante_id)