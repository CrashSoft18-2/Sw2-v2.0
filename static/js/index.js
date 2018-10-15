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

function displayAsesorias(){
  window.location.replace("/index")
}

function displayHistorial(){
  window.location.replace("/historial")
}

function displayMisCitas(){
  window.location.replace("/misCitas")
}

function displaySeminarios(){
  window.location.replace("/seminarios")
}

function displayMisSeminarios(){
  window.location.replace("/misSeminarios")
}

function cancelarCita(id){
   window.location.replace("/cancelarReserva/" + id)
}

function inscripcion(id){
   window.location.replace("/inscripcion/" + id)
}

function cancelarSeminario(id){
   window.location.replace("/cancelarSeminario/" + id)
}

function cerrarSesion(){
   window.location.replace("/cerrarSesion")
}
   
