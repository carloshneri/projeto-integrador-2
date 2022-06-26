function busca_imagem() {
	
	console.log('o id do livro é:');
	id_livro = document.getElementById('isbn').value;
	console.log(id_livro);

	var url = 'https://pi002.herokuapp.com/livro/3/?format=json';
	//var url_get = url + id_livro + '/?format=json';
	dados = fetchAsync(url);
	document.getElementById("imagem_livro").src = dados.thumb
}
async function fetchAsync(url) {
	const opcao = {
		headers: {
			'Content-Type': 'application/json',
			'Access-Control-Allow-Origin': '*',
			"Access-Control-Allow-Credentials" : true
		},
		mode:'no-cors'
	};

	const response = fetch(url, opcao)
		.then(function(responseData){
		 console.log(responseData)
		 return responseData.json()
		})
		.then(function(jsonData){
			console.Console(jsonData)
			return jsonData;

		})
		
}
