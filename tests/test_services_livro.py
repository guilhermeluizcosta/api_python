import pytest
from services import livro_service

@pytest.fixture(autouse=True)
def reset_livros():
    livro_service.livros.clear()
    livro_service.livros.extend([
        {'id': 1, 'titulo': 'A Metamorfose', 'autor': 'Franz Kafka'},
        {'id': 2, 'titulo': 'A Divina Comédia', 'autor': 'Dante Aligheri'}
    ])

def test_obter_livros():
    resultado = livro_service.obter_livros()
    assert len(resultado) == 2

def test_obter_livro_id_encontrado():
    livro = livro_service.obter_livro_id(1)
    assert livro['titulo'] == 'A Metamorfose'

def test_obter_livro_id_nao_encontrado():
    assert livro_service.obter_livro_id(999) is None

def test_inserir_livro():
    novo = {'id': 3, 'titulo': '1984', 'autor': 'George Orwell'}
    livro = livro_service.inserir_livro(novo)
    assert livro == novo
    assert len(livro_service.livros) == 3

def test_inserir_livro_id_existente():
    novo = {'id': 1, 'titulo': 'Repetido', 'autor': 'Outro'}
    assert livro_service.inserir_livro(novo) is None

def test_editar_livro_sucesso():
    editado, erro = livro_service.editar_livro(1, {'titulo': 'Novo Titulo'})
    assert erro is None
    assert editado['titulo'] == 'Novo Titulo'

def test_editar_livro_id_existente_conflict():
    livro_service.inserir_livro({'id': 3, 'titulo': 'Outro', 'autor': 'Autor'})
    _, erro = livro_service.editar_livro(1, {'id': 3})
    assert "ID" in erro

def test_editar_livro_nao_encontrado():
    _, erro = livro_service.editar_livro(999, {'titulo': 'x'})
    assert erro == 'Livro não encontrado'

def test_excluir_livro_sucesso():
    resultado = livro_service.excluir_livro(1)
    assert resultado is True
    assert livro_service.obter_livro_id(1) is None

def test_excluir_livro_nao_encontrado():
    assert livro_service.excluir_livro(999) is False
