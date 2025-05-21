from flask import Flask, jsonify,request

app = Flask(__name__)

livros = [{
    'id':1,
    'titulo':'A Metamorfose',
    'autor': 'Franz Kafka'
}, {
    'id':2,
    'titulo':'A Divina Comédia',
    'autor': 'Dante Aligheri'
}]

# Consultar todos os livros
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)


# Consultar Livro por id
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_id(id):
    for livro in livros:
        if livro.get('id')==id:
            return jsonify(livro)

# Criar Livro
@app.route('/livros', methods=['POST'])
def inserir_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

# Editar Livro
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id')== id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

# Excluir Livro
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id')==id:
            del livros[indice]
            return jsonify(livros)


app.run(port=5000,host='localhost',debug=True)

