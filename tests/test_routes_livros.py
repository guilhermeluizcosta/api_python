def test_get_livros(client):
    response = client.get('/livros')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_get_livro_por_id(client):
    response = client.get('/livros/1')
    assert response.status_code == 200
    assert response.get_json()['titulo'] == 'A Metamorfose'

def test_get_livro_por_id_nao_encontrado(client):
    response = client.get('/livros/999')
    assert response.status_code == 404

def test_post_livro_sucesso(client):
    novo = {'id': 3, 'titulo': '1984', 'autor': 'George Orwell'}
    response = client.post('/livros', json=novo)
    assert response.status_code == 201
    assert response.get_json()['titulo'] == '1984'

def test_post_livro_com_id_existente(client):
    response = client.post('/livros', json={'id': 1, 'titulo': 'Repetido', 'autor': 'x'})
    assert response.status_code == 409

def test_post_livro_campos_faltando(client):
    response = client.post('/livros', json={'id': 4})
    assert response.status_code == 400

def test_put_livro_sucesso(client):
    response = client.put('/livros/1', json={'titulo': 'Atualizado'})
    assert response.status_code == 200
    assert response.get_json()['titulo'] == 'Atualizado'

def test_put_livro_id_conflict(client):
    client.post('/livros', json={'id': 3, 'titulo': 'Livro', 'autor': 'Autor'})
    response = client.put('/livros/1', json={'id': 3})
    assert response.status_code == 409

def test_put_livro_nao_encontrado(client):
    response = client.put('/livros/999', json={'titulo': 'Inexistente'})
    assert response.status_code == 404

def test_delete_livro_sucesso(client):
    response = client.delete('/livros/1')
    assert response.status_code == 200

def test_delete_livro_nao_encontrado(client):
    response = client.delete('/livros/999')
    assert response.status_code == 404
