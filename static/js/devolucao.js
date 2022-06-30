function devolver(id) {
	console.log('função devolucao');
	    
    document.getElementById("input_aluno_id_devolucao").value = id;
       
    var elems = document.getElementById("modal2");
    var instance = M.Modal.getInstance(elems);
    instance.open();
}
