from flask import Flask, render_template, request
import requests


### GET/POST/DELETE/PUT - Aluno
def get_alunos(url, alunos):
    a = alunos #remover essa linha com o Back
    url = url #remover essa linha com o Back
    #alunos = requests.get(url + "/alunos/")
    #return alunos.json()
    return a #remover essa linha com o Back

def post_aluno(url, dados):
    #envio = requests.post(url + "/alunos/", data=dados)
    alunos.append(dados) #remover essa linha com o Back
    #return envio
    return () #remover essa linha com o Back


def delete_aluno():
    pass


def put_aluno(url, dados):
    id = str(dados["id"])
    envio = requests.put(url + "/alunos/" + id, data=dados)
    return envio


def post_livro(url, dados):
    #envio = requests.post(url + "/livros/", data=dados)
    #return envio
    livro.append(dados) #remover essa linha com o Back
    return () #remover essa linha com o Back


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
    title = "Sala de Leitura"
    return render_template("home.html", title=title)

@app.route("/sobre_nos")
def sobre_nos():
    title = "Sobre Nós"
    return render_template("sobre_nos.html", title=title)

@app.route("/duvidas")
def duvidas():
    title = "Perguntas Frequentes"
    return render_template("duvidas.html", title=title)

@app.route("/aluno", methods=["GET", "POST"])
def aluno():
    if request.method == "GET":
        aluno = get_alunos(url, alunos)
  
    if request.method == "POST":
        al = {"id": request.form["input_aluno_id"], "nome": request.form["input_aluno_nome"]}
        put_aluno(url, al)
        aluno = get_alunos(url, aluno)
    return render_template("alunos.html", alunos=aluno)


@app.route("/cadastro_aluno", methods=["GET", "POST"])
def aluno_envio():
    if request.method == "POST":  # verifica se o metodo post do formulario
        aluno = {"id": request.form["ra"], "nome": request.form["nome"]}
        envio = post_aluno(url, aluno)
    return render_template("aluno_cadastro.html")


@app.route("/livros")
def livros():
    livros = livro #remover essa linha com o Back
    # livros = requests.get(url + "/livros").json()
    # livros = livros.json()
    return render_template("livros.html", livros=livros)


@app.route("/devolucao")
def devolucao():
    emprestimos = [
        {
            "id": "6",
            "titulo": "tadsasdjhga",
            "aluno": "Eu mesmo",
            "data_de_emprestimo": "14/11/12",
            "data_de_devolucao": "16/12/45",
        },
        {
            "id": "7",
            "titulo": "tadsasdjhga",
            "aluno": "Eu mesmo",
            "data_de_emprestimo": "15/07/12",
            "data_de_devolucao": "12/12/45",
        },
        {
            "id": "8",
            "titulo": "tad",
            "aluno": "Eu mesmo 001",
            "data_de_emprestimo": "14/09/12",
            "data_de_devolucao": "14/12/45",
        },
    ]
    # emprestimos = get_devolucao(url)
    return render_template("devolucao.html", emprestimos=emprestimos)


@app.route("/cadastro_livro", methods=["GET", "POST"])
def cadastro_livro():
    if request.method == "POST":
        l = {
            "id": request.form["isbn"],
            "titulo": request.form["titulo"],
            "autor": request.form["autor"],
            "editora": request.form["editora"],
            "assunto": request.form["assunto"],
            "resumo": request.form["resumo"],
            "imagem": ("static/images/capa de livros/" + request.form["capa_livro"]),
        }
        # arquivo = request.form['capa_livro']
        envio = post_livro(url, l)

        return render_template("livros_cadastro.html")
    else:
        return render_template("livros_cadastro.html")

@app.route("/emprestimo", methods=['GET', 'POST'])
def emprestimo():

    return render_template("emprestimos.html")




url = "http://localhost:3000"  # $ criar parametro de ambiente

alunos = [
            {"id": "1230258", "nome": "Carlos"},
            {"id": "1230259", "nome": "Gustavo fsfa"},
            {"id": "102", "nome": "adasdasd"},
            {"id": "123", "nome": "Tetse"},
            {"id": "22222", "nome": "SAO PAULO"},
            {"id": "22222", "nome": "ACME"},
            {"id": "9999999", "nome": "ACME"},
            {"id": "999999999", "nome": "ACME"},
            {"id": "wvErZ0K", "nome": ""},
            {"id": "Ugk0NVS", "nome": ""},
            {"id": "ffQIDkM", "nome": ""},
            {"id": "Doi8jDc", "nome": ""},
            {"id": "96565", "nome": "Tropeço"},
            {"id": "2to1LxO", "nome": ""},
        ]

livro = [
        {
            "id": "1",
            "titulo": "",
            "autor": "",
            "editora": "",
            "assunto": "",
            "resumo": "Eita livro legal",
            "imagem": "static/images/capa de livros/knowledge-1052013_1920.jpg",
        },
        {
            "id": "3",
            "titulo": "Jão e ",
            "autor": "Disney",
            "editora": "Estudio de cinema",
            "assunto": "Filme",
            "resumo": "Filme infantil",
            "imagem": "static/images/capa de livros/music-3510326_1920.jpg",
        },
        {
            "id": "1230258",
            "titulo": "Rei leão",
            "autor": "",
            "editora": "",
            "assunto": "",
            "resumo": "",
            "imagem": "static/images/capa de livros/knowledge-1052013_1920.jpg",
        },
        {
            "id": "102",
            "titulo": "jhgjhghgjhghgjhgjhgjhgjh",
            "autor": "",
            "editora": "",
            "assunto": "",
            "resumo": "",
            "imagem": "static/images/capa de livros/knowledge-1052013_1920.jpg",
        },
        {
            "id": "00000",
            "titulo": "123123",
            "autor": "",
            "editora": "",
            "assunto": "",
            "resumo": "",
        },
        {
            "id": "090",
            "titulo": "Kiko",
            "autor": "chaves",
            "editora": "SBT",
            "assunto": "",
            "resumo": "",
        },
        {   "id": "1223", 
            "titulo": "asd", 
            "autor": "", 
            "editora": "", 
            "assunto": "", 
            "resumo": ""
        },
        {
            "id": "98765421",
            "titulo": "joão e maria",
            "autor": "não me lembro",
            "assunto": "infantil",
            "resumo": "Livro sobre dois irmãos",
        },
        {
            "id": "986532147",
            "titulo": "O escaravelho",
            "autor": "não me lembro",
            "editora": "Vagalume",
            "assunto": "Infantil",
            "resumo": "livro que conta a história de uma serie de assassinatos ",
            "imagem": "static/images/capa de livros/Capturar1.PNG",
        },
        ]
