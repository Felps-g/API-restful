from models.restaurante_models import Restaurante  # Importa o modelo Restaurante
from db import db  # Conexão com o banco de dados
import json
from flask import make_response, request

# Função para obter todos os restaurantes
def get_restaurantes():
    restaurantes = Restaurante.query.all()  # Busca todos os restaurantes no banco
    
    if not restaurantes:
        response = make_response(
            json.dumps({
                'mensagem': 'Nenhum restaurante encontrado.',
                'dados': []
            }, ensure_ascii=False, sort_keys=False)
        )
    else:
        response = make_response(
            json.dumps({
                'mensagem': 'Lista de restaurantes.',
                'dados': [restaurante.json() for restaurante in restaurantes]
            }, ensure_ascii=False, sort_keys=False)
        )
    
    response.headers['Content-Type'] = 'application/json'
    return response


# Função para obter um restaurante específico por ID
def get_restaurante_by_id(restaurante_id):
    restaurante = Restaurante.query.get(restaurante_id)

    if restaurante:
        response = make_response(
            json.dumps({
                'mensagem': 'Restaurante encontrado.',
                'dados': restaurante.json()
            }, ensure_ascii=False, sort_keys=False)
        )
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(
            json.dumps({'mensagem': 'Restaurante não encontrado.', 'dados': {}}, ensure_ascii=False),
            404
        )
        response.headers['Content-Type'] = 'application/json'
        return response


# Função para consultar um restaurante por nome
def get_restaurante_by_nome(restaurante_nome):
    restaurante = Restaurante.query.filter_by(nome=restaurante_nome).first()

    if restaurante:
        response = make_response(
            json.dumps({
                'mensagem': 'Restaurante encontrado.',
                'dados': restaurante.json()
            }, sort_keys=False)
        )
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(
            json.dumps({
                'mensagem': 'Restaurante não encontrado.',
                'dados': {}
            }, sort_keys=False),
            404
        )
        response.headers['Content-Type'] = 'application/json'
        return response


# Função para criar um novo restaurante
def create_restaurante(restaurante_data):
    if not all(key in restaurante_data for key in ['nome', 'endereco', 'tipo_cozinha']):
        response = make_response(
            json.dumps({'mensagem': 'Dados inválidos. Nome, endereço e tipo de cozinha são obrigatórios.'}, ensure_ascii=False),
            400
        )
        response.headers['Content-Type'] = 'application/json'
        return response
    
    novo_restaurante = Restaurante(
        nome=restaurante_data['nome'],
        endereco=restaurante_data['endereco'],
        tipo_cozinha=restaurante_data['tipo_cozinha']
    )
    
    db.session.add(novo_restaurante)
    db.session.commit()

    response = make_response(
        json.dumps({
            'mensagem': 'Restaurante cadastrado com sucesso.',
            'restaurante': novo_restaurante.json()
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response


# Função para atualizar um restaurante por ID
def update_restaurante(restaurante_id, restaurante_data):
    restaurante = Restaurante.query.get(restaurante_id)

    if not restaurante:
        response = make_response(
            json.dumps({'mensagem': 'Restaurante não encontrado.'}, ensure_ascii=False),
            404
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    if not all(key in restaurante_data for key in ['nome', 'endereco', 'tipo_cozinha']):
        response = make_response(
            json.dumps({'mensagem': 'Dados inválidos. Nome, endereço e tipo de cozinha são obrigatórios.'}, ensure_ascii=False),
            400
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    restaurante.nome = restaurante_data['nome']
    restaurante.endereco = restaurante_data['endereco']
    restaurante.tipo_cozinha = restaurante_data['tipo_cozinha']

    db.session.commit()

    response = make_response(
        json.dumps({
            'mensagem': 'Restaurante atualizado com sucesso.',
            'restaurante': restaurante.json()
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response


# Função para excluir um restaurante por ID com confirmação via parâmetro
def delete_restaurante(restaurante_id):
    confirmacao = request.args.get('confirmacao')

    if confirmacao != 'true':
        response = make_response(
            json.dumps({'mensagem': 'Confirmação necessária para excluir o restaurante.'}, ensure_ascii=False),
            400
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    restaurante = Restaurante.query.get(restaurante_id)
    if not restaurante:
        response = make_response(
            json.dumps({'mensagem': 'Restaurante não encontrado.'}, ensure_ascii=False),
            404
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    db.session.delete(restaurante)
    db.session.commit()

    response = make_response(
        json.dumps({'mensagem': 'Restaurante excluído com sucesso.'}, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response