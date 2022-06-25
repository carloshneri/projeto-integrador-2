funcao = 'editar';

function editar_livro(id, isbn, titulo, autor, editora, assunto, resumo) {
	console.log('função editar livro');

	document.querySelector('#input_livro_isbn').disabled = false;
	document.querySelector('#input_livro_titulo').disabled = false;
	document.querySelector('#input_livro_autor').disabled = false;
	document.querySelector('#input_livro_editora').disabled = false;
	document.querySelector('#input_livro_assunto').disabled = false;
	document.querySelector('#input_livro_resumo').disabled = false;
	document.querySelector('#input_livro_id').disabled = false;

	document.getElementById('btn_confirmar_apagar').style.display = 'none';
	document.getElementById('btn_confirmar_edicao').style.display = '';

	document.getElementById('input_livro_id').value = id;
	document.getElementById('input_livro_isbn').value = isbn;
	document.getElementById('input_livro_titulo').value = titulo;
	document.getElementById('input_livro_autor').value = autor;
	document.getElementById('input_livro_editora').value = editora;
	document.getElementById('input_livro_assunto').value = assunto;
	document.getElementById('input_livro_resumo').value = resumo;
	
	document.getElementById('input_livro_funcao').value = 'PUT';

	var elems = document.getElementById('modal_livro');
	var instance = M.Modal.getInstance(elems);

	instance.open();
}

function apagar_livro(id, isbn, titulo, autor, editora) {
	document.getElementById('btn_confirmar_edicao').style.display = 'none';
	document.getElementById('btn_confirmar_apagar').style.display = '';

	document.getElementById('input_livro_id').value = id;
	document.getElementById('input_livro_id').style.display = 'none';
	document.getElementById('label_id').style.display = 'none';

	document.getElementById('input_livro_titulo').value = titulo;
	document.getElementById('input_livro_titulo').disabled = true;

	document.getElementById('input_livro_isbn').value = isbn;
	document.getElementById('input_livro_isbn').disabled = true;

	document.getElementById('input_livro_autor').value = autor;
	document.getElementById('input_livro_autor').disabled = true;

	document.getElementById('input_livro_editora').value = editora;
	document.getElementById('input_livro_editora').disabled = true;

	document.getElementById('input_livro_assunto').style.display = 'none';
	document.getElementById('label_assunto').style.display = 'none';

	document.getElementById('input_livro_resumo').style.display = 'none';
	document.getElementById('label_resumo').style.display = 'none';

	document.getElementById('input_livro_funcao').value = 'DELETE';

	var elems = document.getElementById('modal_livro');
	var instance = M.Modal.getInstance(elems);

	instance.open();
}
