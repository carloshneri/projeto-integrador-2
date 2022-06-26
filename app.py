from flask import Flask, render_template, redirect, url_for, request
import requests
import datetime

### GET/POST/DELETE/PUT - Aluno
def get_alunos(url, alunos):
    a = alunos  # remover essa linha com o Back
    url = url  # remover essa linha com o Back
    # alunos = requests.get(url + "/alunos/")
    # return alunos.json()
    return a  # remover essa linha com o Back


def post_aluno(url, dados):
    # envio = requests.post(url + "/alunos/", data=dados)
    alunos.append(dados)  # remover essa linha com o Back
    # return envio
    return ()  # remover essa linha com o Back


def delete_aluno():
    pass


def put_aluno(url, dados):
    id = str(dados["id"])
    envio = requests.put(url + "/alunos/" + id, data=dados)
    return envio


def post_livro(dados):
    envio = requests.post("https://pi002.herokuapp.com/livro/?format=json", data=dados)
    # return envio
    # livro.append(dados) #remover essa linha com o Back
    return ()  # remover essa linha com o Back


### GET/DELETE/PUT - Livros
def get_devolucao():
    emprestimos = requests.get("https://pi002.herokuapp.com/emprestimo/?format=json")
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


@app.route("/livros", methods=["GET", "POST"])
def livros():
    if request.method == "POST":
        
        tipo = request.form["input_livro_funcao"]
        
        id = request.form["input_livro_id"]
        
        if tipo == "DELETE":
            url = "https://pi002.herokuapp.com/livro/" + id + "/?format=json"
            requests.delete(url)

        elif tipo == "PUT":
            
            l = {
                "id": request.form["input_livro_id"],
                "isbn": request.form["input_livro_isbn"],
                "titulo": request.form["input_livro_titulo"],
                 "autor": request.form["input_livro_autor"],
                "editora": request.form["input_livro_editora"],
                "assunto": request.form["input_livro_assunto"],
                "resumo": request.form["input_livro_resumo"],
                 }
            url = "https://pi002.herokuapp.com/livro/" + id + "/?format=json"
            requests.put(url, l)
        

    else:
        pass

    livros = requests.get("https://pi002.herokuapp.com/livro/?format=json").json()
    return render_template("livros.html", livros=livros)



@app.route("/devolucao")
def devolucao():
    """emprestimos = [
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
    ]"""
    emprestimos = get_devolucao()
    return render_template("devolucao.html", emprestimos=emprestimos)


@app.route("/cadastro_livro", methods=["GET", "POST"])
def cadastro_livro():
    if request.method == "POST":
        l = {
            "id": request.form["isbn"],
            "isbn": request.form["isbn"],
            "titulo": request.form["titulo"],
            "trumb": request.files["capa_livro"],
            "autor": request.form["autor"],
            "editora": request.form["editora"],
            "assunto": request.form["assunto"],
            "resumo": request.form["resumo"],
            "data_cadastro": "2022-06-10",
        }

        # arquivo = request.form['capa_livro']
        envio = post_livro(l)

        return render_template("livros_cadastro.html")
    else:
        return render_template("livros_cadastro.html")


@app.route("/emprestimo", methods=["GET", "POST"])
def emprestimo():
    
    if request.method =="POST":
        complemento = "T18:33:36-03:00"
        data_emprestimo = request.form['data_emprestimo']+complemento
        lista_data = list(data_emprestimo)
        lista_data[4]="-"
        lista_data[7] = "-"
        data_emprestimo = ''.join(lista_data)
        print("essa é a lista ")        
        print(data_emprestimo)

        empr ={ "ra": int(request.form['ra']),
                "dataemp": data_emprestimo,
                "datadev": "2022-06-09T18:33:36-03:00",
                "ativo":'True',
                "isbn":int(request.form['isbn'])}
        envio = requests.post("https://pi002.herokuapp.com/emprestimo/?format=json", empr)
        print("enviado o emprestimo")
        print(envio)


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
