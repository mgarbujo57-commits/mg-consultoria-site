from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "mg-consultoria-chave"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contato", methods=["POST"])
def contato():
    nome = request.form.get("nome", "").strip()
    email = request.form.get("email", "").strip()
    telefone = request.form.get("telefone", "").strip()
    mensagem = request.form.get("mensagem", "").strip()

    if not nome or not email or not mensagem:
        flash("Preencha nome, e-mail e mensagem.", "erro")
        return redirect(url_for("home") + "#contato")

    # Neste exemplo, os dados são apenas recebidos.
    # Para produção, conecte este ponto a e-mail, banco de dados ou CRM.
    print({
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "mensagem": mensagem
    })

    flash("Mensagem recebida! Em breve entraremos em contato.", "sucesso")
    return redirect(url_for("home") + "#contato")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
