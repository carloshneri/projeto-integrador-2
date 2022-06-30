


async function busca_imagem() {
	id_livro = document.getElementById('isbn').value;
	var url = 'https://pi002.herokuapp.com/livro/';
	var url_get = url + id_livro + '/?format=json'
	const response = await fetch(url_get);
	const jsonData = await response.json();
	console.log(jsonData);
	document.getElementById('imagem_livro').src = jsonData.thumb;
}
/*
	console.log('o id do livro é:');
	id_livro = document.getElementById('isbn').value;
	console.log(id_livro);

	var url = 'https://pi002.herokuapp.com/livro/1/?format=json';
	//var url_get = url + id_livro + '/?format=json';
	dados = fetchAsync(url);
	console.log('dados')
	console.log(dados)
	document.getElementById('imagem_livro').src = dados.thumb;
}
async function fetchAsync(url) {
	const opcao = {
		method: 'GET',
		headers: {
			'Content-Type': 'application/json',
		},
	};

	const resposta = fetch(url, opcao)
		.then(function (responseData) {
			return responseData.json();
        })
         .then(function(jsonData){   
			return(jsonData)
		
}*/
