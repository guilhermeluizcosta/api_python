from flask import Blueprint, jsonify,request,abort
from models.livro import livros

livros_bp = Blueprint('livros',__name__)

# GET - Listar todos os Livros
@livros_bp.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)


# GET - Consultar Livro por id
@livros_bp.route('/livros/<int:id>',methods=['GET'])
def obter_livro_id(id):
    livro = next((livro for livro in livros if livro.get('id') == id), None)
    if not livro:
        abort(404, description="Livro não encontrado")
    return jsonify(livro)


# POST - Inserir Novo Livro
@livros_bp.route('/livros', methods=['POST'])
def inserir_livro():
    novo_livro = request.get_json()
    if not novo_livro.get('id') or not novo_livro.get('titulo') or not novo_livro.get('autor'):
        abort(400, description="Campos obrigatórios: id, titulo, autor")
    livros.append(novo_livro)
    return jsonify(livros), 201

# PUT - Editar um Livro
@livros_bp.route('/livros/<int:id>', methods=['PUT'])
def editar_livro(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id')== id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
    abort(404, description="Livro não encontrado")


# DELETE - Excluir Livro
@livros_bp.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id')==id:
            del livros[indice]
            return jsonify(livros), 200
    abort(404, description="Livro não encontrado")