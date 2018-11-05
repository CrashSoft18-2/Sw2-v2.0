function buscar() {
   var prof, carr, curso, filterProf, filterCarr, filterCurso, table, tr, td1, td2, td3, i;
   prof = document.getElementById("prof");
   filterProf = prof.value.toUpperCase();

   carr = document.getElementById("carrera");
   filterCarr = carr.value.toUpperCase();

   curso = document.getElementById("curso");
   filterCurso = curso.value.toUpperCase();

   table = document.getElementById("myTable");
   tr = table.getElementsByTagName("tr");
   for (i = 0; i < tr.length; i++) {
     td1 = tr[i].getElementsByTagName("td")[0];
     console.log(td1);
     td2 = tr[i].getElementsByTagName("td")[2];
     console.log(td2);
     td3 = tr[i].getElementsByTagName("td")[1];
     console.log(td3);
     if (td1, td2, td3) {
       if ((td1.innerHTML.toUpperCase().indexOf(filterProf) > -1) && (td2.innerHTML.toUpperCase().indexOf(filterCurso) > -1) && (td3.innerHTML.toUpperCase().indexOf(filterCarr) > -1)) {
         tr[i].style.display = "";
       } else {
         tr[i].style.display = "none";
       }
     }
   }
 }

function buscarCitas() {
   var prof, carr, curso, filterProf, filterCarr, filterCurso, table, tr, td1, td2, td3, td4, i;
   prof = document.getElementById("prof");
   filterProf = prof.value.toUpperCase();

   carr = document.getElementById("carrera");
   filterCarr = carr.value.toUpperCase();

   curso = document.getElementById("fecha");
   filterCurso = curso.value.toUpperCase();
   
   carrera = document.getElementById("consulta");
   filterConsulta = carrera.value.toUpperCase();
   
   table = document.getElementById("detalle");
   tr = table.getElementsByTagName("tr");
   for (i = 0; i < tr.length; i++) {
     td1 = tr[i].getElementsByTagName("td")[0];
     td3 = tr[i].getElementsByTagName("td")[1];
     td2 = tr[i].getElementsByTagName("td")[2];
     td4 = tr[i].getElementsByTagName("td")[5];
     if (td1, td2, td3) {
       if ((td1.innerHTML.toUpperCase().indexOf(filterProf) > -1) && (td2.innerHTML.toUpperCase().indexOf(filterCurso) > -1) && (td3.innerHTML.toUpperCase().indexOf(filterCarr) > -1) && (td4.innerHTML.toUpperCase().indexOf(filterConsulta) > -1)) {
         tr[i].style.display = "";
       } else {
         tr[i].style.display = "none";
       }
     }
   }
 }


function buscarSeminario() {
   var prof, carr, curso, filterProf, filterCarr, filterCurso, table, tr, td1, td2, td3, i;
   prof = document.getElementById("prof");
   filterProf = prof.value.toUpperCase();

   carr = document.getElementById("carrera");
   filterCarr = carr.value.toUpperCase();
   
   topic = document.getElementById("topic");
   filterTopic = topic.value.toUpperCase();
   
   table = document.getElementById("myTable");
   tr = table.getElementsByTagName("tr");
   for (i = 0; i < tr.length; i++) {
     td1 = tr[i].getElementsByTagName("td")[0];
     td2 = tr[i].getElementsByTagName("td")[1];
     td3 = tr[i].getElementsByTagName("td")[2];
     if (td1, td2, td3) {
       if ((td1.innerHTML.toUpperCase().indexOf(filterProf) > -1) && (td2.innerHTML.toUpperCase().indexOf(filterCarr) > -1) && (td3.innerHTML.toUpperCase().indexOf(filterTopic) > -1)) {
         tr[i].style.display = "";
       } else {
         tr[i].style.display = "none";
       }
     }
   }
 }

function displayProximasAsesorias(){
  window.location.replace("/profesor/displayProximasAsesorias")
}

function cambiarDisponibilidad(id){
   window.location.replace("/profesor/editarDisponibilidad/" + id)
}

function displayHistorial(){
  window.location.replace("/profesor/displayHistorial")
}

function displaySeminarios(){
  window.location.replace("/profesor/displaySeminarios")
}

function displaySeminarioDetalle(id){
  window.location.replace("/profesor/displaySeminariosDetalle/" + id)
}

function addLine(){
   document.task = "add";
   document.getElementById("add").style.display = "none";
   
   var tbody = document.getElementById("detalle").firstChild.nextSibling;
   
   var nodeTema = document.createElement("input");
   var nodeConc = document.createElement("input");
   
   var save = document.createElement("img");
   var cancel = document.createElement("img");
   
   save.setAttribute("class", "save");
   save.setAttribute("src", "data:image/png;base64,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");
   save.setAttribute("onclick", "submitHistorial()");
   cancel.setAttribute("class", "cancel");
   cancel.setAttribute("src", "https://techflourish.com/images/cross-with-sunset-clipart-16.png");
   cancel.setAttribute("onclick", "cancel()");
   
   nodeTema.setAttribute("class", "row");
   nodeTema.setAttribute("name", "tema");
   nodeConc.setAttribute("class", "row");
   nodeConc.setAttribute("name", "conclusion");
   nodeTema.setAttribute("id", "temaTratado");
   nodeConc.setAttribute("id", "conclusion");
   
   var cell1 = document.createElement("td");
   var cell2 = document.createElement("td");
   var cell3 = document.createElement("td");
   
   cell1.appendChild(nodeTema);
   cell2.appendChild(nodeConc);
   cell3.appendChild(save);
   cell3.appendChild(cancel);
   
   var row = document.createElement("tr");
   row.appendChild(cell1);
   row.appendChild(cell2);
   row.appendChild(cell3);
   tbody.appendChild(row);
}

function cancel(){
   document.getElementById("add").style.display = "inline";
   $("#conclusion").parent().parent().remove()
}

function submitHistorial(){ 
   if (document.task == "add"){
      document.formHistorial.action = "/profesor/agregarTemaTratado/" + document.profesor.value;
   } else if (document.task == "edit"){
   } else if (document.task == "delete"){
   }
   document.formHistorial.submit()
}

/*
function cancelarCita(id){
   window.location.replace("/alumno/cancelarReserva/" + id)
}

function inscripcion(id){
   window.location.replace("/alumno/inscripcionSeminario/" + id)
}

function cancelarSeminario(id){
   window.location.replace("/alumno/cancelarSeminario/" + id)
}*/

function cerrarSesion(){
   window.location.replace("/profesor/cerrarSesion");
}
   
