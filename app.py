from flask import Flask, render_template, request
import requests

url = "http://localhost:3000"  # $ criar parametro de ambiente

### GET/POST/DELETE/PUT - Aluno
def get_alunos(url):
    alunos = requests.get(url + "/alunos/")
    return alunos.json()


def post_aluno(url, dados):
    envio = requests.post(url + "/alunos/", data=dados)
    return envio


def delete_aluno():
    pass


def put_aluno(url, dados):
    id = str(dados["id"])
    envio = requests.put(url + "/alunos/" + id, data=dados)
    return envio


def post_livro(url, dados):
    envio = requests.post(url + "/livros/", data=dados)
    return envio


### GET/DELETE/PUT - Livros
def get_devolucao(url):
    emprestimos = requests.get(url + "/emprestimos")
    return emprestimos.json()


def delete_devolucao():
    pass


# Aplicação flask

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/aluno", methods=["GET", "POST"])
def aluno():
    if request.method == "GET":
        alunos = get_alunos(url)

    if request.method == "POST":
        al = {"id": request.form["input_aluno_id"], "nome": request.form["input_aluno_nome"]}
        put_aluno(url, al)
        alunos = get_alunos(url)
    return render_template("alunos.html", alunos=alunos)


@app.route("/cadastro_aluno", methods=["GET", "POST"])
def aluno_envio():
    if request.method == "POST":  # verifica se o metodo post do formulario
        aluno = {"id": request.form["ra"], "nome": request.form["nome"]}
        envio = post_aluno(url, aluno)
    return render_template("aluno_cadastro.html")


@app.route("/livros")
def livros():
    livros = requests.get(url + "/livros").json()
    # livros = livros.json()
    return render_template("livros.html", livros=livros)


@app.route("/devolucao")
def devolucao():
    emprestimos = get_devolucao(url)
    return render_template("devolucao.html", emprestimos=emprestimos)


@app.route("/cadastro_livro", methods=["GET", "POST"])
def cadastro_livro():
    if request.method == "POST":
        livro = {
            "id": request.form["isbn"],
            "titulo": request.form["titulo"],
            "autor": request.form["autor"],
            "editora":request.form["editora"],
            "assunto": request.form["assunto"],
            "resumo": request.form["resumo"],
            "imagem":("static/images/capa de livros/" + request.form['capa_livro']),
        }
        #arquivo = request.form['capa_livro']
        envio = post_livro(url, livro)

        return render_template("livros_cadastro.html")
    else:
        return render_template("livros_cadastro.html")
