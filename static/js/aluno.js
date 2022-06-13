
funcao = "editar"

function editar(id,nome){

    document.querySelector("#input_aluno_id").disabled = false
    document.querySelector("#input_aluno_nome").disabled = false
    document.getElementById("btn_confirmar_apagar").style.display = 'none'
    document.getElementById("btn_confirmar_edicao").style.display = ''
    
    document.getElementById("input_aluno_id").value = id
    document.getElementById("input_aluno_nome").value = nome
    
    var elems = document.getElementById("modal1");
    var instance = M.Modal.getInstance(elems);
    instance.open();
};


function apagar(id,nome){
    //this.id = id
    //this.nome = nome
    //funcao = apagar
    document.getElementById("btn_confirmar_edicao").style.display = 'none'
    document.getElementById("btn_confirmar_apagar").style.display = ''
    
    document.getElementById("input_aluno_id").value = id
    document.getElementById("input_aluno_nome").value = nome
    document.querySelector("#input_aluno_id").disabled = true
    document.querySelector("#input_aluno_nome").disabled = true
    
    var elems = document.getElementById("modal1");
    var instance = M.Modal.getInstance(elems);
    instance.open();
};


function ok(){
    funcao
    if (funcao == 'editar') 
        console.log("editar")      
    else
        console.log("apagar")

    document.querySelector("#input_aluno_id").disabled = false
    document.querySelector("#input_aluno_nome").disabled = false
    
};

