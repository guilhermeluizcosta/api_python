from models.livro import livros

def obter_livros():
    return livros

def obter_livro_id(id):
    return next((livro for livro in livros if livro.get('id') == id), None)

def inserir_livro(novo_livro):
    if obter_livro_id(novo_livro.get('id')) is not None:
        return None
    livros.append(novo_livro)
    return novo_livro

def editar_livro(id, dados_atualizados):
    novo_id = dados_atualizados.get('id')
    if novo_id and novo_id != id:
        if obter_livro_id(novo_id):
            return None, "Já existe um livro com o ID fornecido"
    for i, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[i].update(dados_atualizados)
            return livros[i], None

    return None, "Livro não encontrado"

def excluir_livro(id):
    for i, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[i]
            return True
    return False
