
funcao = "editar"

function editar(id,ra,nome, turma){

    document.querySelector("#input_aluno_id").disabled = false
    document.querySelector("#input_aluno_nome").disabled = false
    document.getElementById("btn_confirmar_apagar").style.display = 'none'
    document.getElementById("btn_confirmar_edicao").style.display = ''
    
    document.getElementById("input_aluno_id").value = id
    document.getElementById("input_aluno_ra").value = ra
    document.getElementById("input_aluno_nome").value = nome
    document.getElementById("input_aluno_turma").value = turma

    document.getElementById('input_aluno_funcao').value = 'PUT';    
    var elems = document.getElementById("modal1");
    var instance = M.Modal.getInstance(elems);
    instance.open();

};


function apagar(id,ra, nome, turma){
   
    document.getElementById("btn_confirmar_edicao").style.display = 'none';
    document.getElementById("btn_confirmar_apagar").style.display = '';
    
    document.getElementById("input_aluno_id").value = id;
    document.getElementById('input_aluno_id').style.display = 'none';
    document.getElementById('label_id').style.display = 'none';
	

    document.getElementById("input_aluno_ra").value = ra;
    
    document.getElementById("input_aluno_nome").value = nome;
    
    document.getElementById("input_aluno_turma").value = turma;
    
    document.getElementById('input_aluno_funcao').value = 'DELETE';
    
    var elems = document.getElementById("modal1");
    var instance = M.Modal.getInstance(elems);
    instance.open();
};




