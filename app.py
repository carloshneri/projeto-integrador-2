from flask import Flask, render_template, redirect, url_for, request
import requests
import datetime

### GET/POST/DELETE/PUT - Aluno
def get_alunos(url):
    alunos = requests.get(url + "usuario/")
    return alunos.json()


def post_aluno(dados):
    envio = requests.post("https://pi002.herokuapp.com/usuario/?format=json", data=dados)

    return envio


def delete_aluno():
    pass


def put_aluno(url, dados):
    id = str(dados["id"])
    print(dados)
    envio = requests.put(url + "usuario/" + id + "/?format=json", data=dados)
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
        pass
        #aluno = requests.get("https://pi002.herokuapp.com/usuario/?format=json").json()
    if request.method == "POST":
        id = request.form["input_aluno_id"]
        tipo = request.form["input_aluno_funcao"]
        if tipo == "PUT":
            al = {
                "id": request.form["input_aluno_id"],
                "ra": request.form["input_aluno_ra"],
                "first_name": request.form["input_aluno_nome"],
                "username": request.form["input_aluno_nome"],
                "password": "3A",
                "turma": request.form["input_aluno_turma"],
                "ano": "4",
                "date_joined": "2022-06-29T15:04:05.997621-03:00",
            }
        
            print("https://pi002.herokuapp.com/usuario/" + id + "/?format=json")
            requests.put("https://pi002.herokuapp.com/usuario/" + id + "/?format=json", data=al)
           
        
        else:
            url = "https://pi002.herokuapp.com/usuario/" + id + "/?format=json"
            requests.delete(url)
    

    aluno = requests.get("https://pi002.herokuapp.com/usuario/?format=json").json()
    return render_template("alunos.html", alunos=aluno)


@app.route("/cadastro_aluno", methods=["GET", "POST"])
def aluno_envio():
    if request.method == "POST":
        aluno = {
            "ra": request.form["ra"],
            "first_name": request.form["nome"],
            "username": request.form["nome"],
            "password": "3A",
            "turma": request.form["serie"],
            "ano": "4",
            "date_joined": "2022-06-29T15:04:05.997621-03:00",
        }
        post_aluno(aluno)
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
            print(l)
            requests.put(url, l)

    else:
        pass

    livros = requests.get("https://pi002.herokuapp.com/livro/?format=json").json()
    return render_template("livros.html", livros=livros)


@app.route("/devolucao", methods = ['GET', 'POST'])
def devolucao():


    if request.method=='POST':
        id = request.form["input_aluno_id_devolucao"]
        
        url = "https://pi002.herokuapp.com/emprestimo/" + id + "/?format=json"
        
        requests.delete(url)

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
        print(l["trumb"])
        # arquivo = request.form['capa_livro']
        envio = post_livro(l)

        return render_template("livros_cadastro.html")
    else:
        return render_template("livros_cadastro.html")


@app.route("/emprestimo", methods=["GET", "POST"])
def emprestimo():

    if request.method == "POST":
        complemento = "T18:33:36-03:00"
        data_emprestimo = request.form["data_emprestimo"] + complemento
        lista_data = list(data_emprestimo)
        lista_data[4] = "-"
        lista_data[7] = "-"
        data_emprestimo = "".join(lista_data)
        print("essa é a lista ")
        print(data_emprestimo)

        empr = {
            "ra": int(request.form["ra"]),
            "dataemp": data_emprestimo,
            "datadev": "2022-06-09T18:33:36-03:00",
            "ativo": "True",
            "isbn": int(request.form["isbn"]),
        }
        envio = requests.post("https://pi002.herokuapp.com/emprestimo/?format=json", empr)
        print("enviado o emprestimo")
        print(envio)

    return render_template("emprestimos.html")


url = "https://pi002.herokuapp.com/"  # $ criar parametro de ambiente

