from flask import Blueprint,request
from services.livro_service import *
from utils.responses import resposta_erro, resposta_sucesso

livros_bp = Blueprint('livros',__name__)

# GET - Listar todos os Livros
@livros_bp.route('/livros', methods=['GET'])
def route_obter_livros():
    return resposta_sucesso(obter_livros())

# GET - Consultar Livro por id
@livros_bp.route('/livros/<int:id>',methods=['GET'])
def route_obter_livro_id(id):
    livro = obter_livro_id(id)
    if livro:
        return resposta_sucesso(livro)

    return resposta_erro("Livro não encontrado", 404)

# POST - Inserir Novo Livro
@livros_bp.route('/livros', methods=['POST'])
def route_inserir_livro():
    novo_livro = request.get_json()

    if not novo_livro.get('id') or not novo_livro.get('titulo') or not novo_livro.get('autor'):
        return resposta_erro("Campos obrigatórios: id, titulo, autor", 400)

    livro_inserido = inserir_livro(novo_livro)

    if livro_inserido is None:
        return resposta_erro("Já existe um livro com esse ID", 409)

    return resposta_sucesso(livro_inserido, 201)

# PUT - Editar um Livro
@livros_bp.route('/livros/<int:id>', methods=['PUT'])
def route_editar_livro(id):
    dados = request.get_json()
    livro_editado, erro = editar_livro(id, dados)
    if erro:
        return resposta_erro(erro, 409 if "ID" in erro else 404)
    return resposta_sucesso(livro_editado)

# DELETE - Excluir Livro
@livros_bp.route('/livros/<int:id>', methods=['DELETE'])
def route_excluir_livro(id):
    if excluir_livro(id):
        return resposta_sucesso("Livro removido com sucesso", 200)
    return resposta_erro("Livro não encontrado", 404)