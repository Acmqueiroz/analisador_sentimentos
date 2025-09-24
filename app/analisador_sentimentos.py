from flask import Flask, request, jsonify
from textblob import TextBlob

aplicacao = Flask(__name__)

@aplicacao.route("/analisar", methods=["POST"])
def analisar_sentimento():
    dados = request.get_json()
    texto = dados.get("texto", "")

    if not texto:
        return jsonify({"erro": "Nenhum texto enviado"}), 400

    analise = TextBlob(texto)
    polaridade = analise.sentiment.polarity

    if polaridade > 0:
        classificacao = "Positivo 😀"
    elif polaridade < 0:
        classificacao = "Negativo 😡"
    else:
        classificacao = "Neutro 😐"

    resposta = {
        "texto": texto,
        "polaridade": polaridade,
        "classificacao": classificacao
    }

    return jsonify(resposta), 200

@aplicacao.route("/", methods=["GET"])
def pagina_teste():
    return """
    <html>
      <head><meta charset="utf-8"><title>Analisador de Sentimentos</title></head>
      <body>
        <h2>Analisador de Sentimentos</h2>
        <form method="post" action="/analisar" onsubmit="event.preventDefault(); enviar();">
          <textarea id="texto" rows="6" cols="60" placeholder="Cole um texto aqui..."></textarea><br/>
          <button type="submit">Analisar</button>
        </form>
        <pre id="resultado"></pre>

        <script>
          async function enviar() {
            const texto = document.getElementById('texto').value;
            const res = await fetch('/analisar', {
              method: 'POST',
              headers: {'Content-Type': 'application/json'},
              body: JSON.stringify({ texto })
            });
            const json = await res.json();
            document.getElementById('resultado').textContent = JSON.stringify(json, null, 2);
          }
        </script>
      </body>
    </html>
    """

if __name__ == "__main__":
    aplicacao.run(debug=True)
