from flask import Flask, request, jsonify, render_template
from textblob import TextBlob
import os

aplicacao = Flask(__name__)

@aplicacao.route("/analisar", methods=["POST"])
def analisar_sentimento():
    dados = request.get_json()
    texto = dados.get("texto", "")

    if not texto:
        return jsonify({"erro": "Nenhum texto enviado"}), 400

    analise = TextBlob(texto)
    polaridade = analise.sentiment.polarity

    if polaridade > 0.1:
        classificacao = "Positivo"
        emoji = "😀"
        cor = "#4CAF50"
        descricao = "O texto expressa sentimentos positivos!"
    elif polaridade < -0.1:
        classificacao = "Negativo"
        emoji = "😡"
        cor = "#F44336"
        descricao = "O texto expressa sentimentos negativos."
    else:
        classificacao = "Neutro"
        emoji = "😐"
        cor = "#FF9800"
        descricao = "O texto é neutro em relação aos sentimentos."

    # Calcular porcentagem
    porcentagem = abs(polaridade) * 100

    resposta = {
        "texto": texto,
        "polaridade": polaridade,
        "classificacao": classificacao,
        "emoji": emoji,
        "cor": cor,
        "descricao": descricao,
        "porcentagem": round(porcentagem, 1)
    }

    return jsonify(resposta), 200

@aplicacao.route("/", methods=["GET"])
def pagina_principal():
    return render_template('index.html')

if __name__ == "__main__":
    aplicacao.run(debug=True)
