from flask import jsonify

def resposta_sucesso(dados, status=200):
    if isinstance(dados, (list, dict)):
        return jsonify(dados), status
    return jsonify({'mensagem': dados}), status

def resposta_erro(mensagem, status=400):
    return jsonify({'erro': mensagem}), status