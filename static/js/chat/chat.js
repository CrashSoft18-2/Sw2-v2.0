
var USUARIO_ACTUAL = sessionStorage.getItem('user');
var mensajes = [];
var chats = [];
var index = 0;
div_user_list = $('#user_list_content ul');

var usuarios = [];
var usuario = [];
var div;
var currentTime = Date.now()

window.onload = main;

function main(){
	$('#user_list_header').click(function(){
		$('#user_list').toggleClass('collapsed');
	});
	$('#user_list').append("<input type='text' onkeypress='filter()' id='searchChat' placeholder='&#61447; Buscar'/>");
	agregarAlumnos();
	agregarProfesores();
	abrirAlRecibir();
}

function filter(){
	expr = document.getElementById("searchChat").value;
	
	$('.user_item').each(function(){
		console.log(thix.textContent);
	});
}
	
	
 function agregarAlumnos(){
	firebase.database().ref().child("Usuarios").child("Alumnos").on('value', function(snapshot) {
	    snapshot.forEach(function(child) {
		var user = {}
		user.id = child.val().id;
		user.user = child.val().user;
		user.nombre = String(child.val().nombre);
		 
		if(user.user != USUARIO_ACTUAL){
		   usuarios.push(user);
		   div_user_list.append( "<li style='list-style: none;' class = 'user_item' onClick = " + String.fromCharCode(34) + "openChatBox(" + index + ")" + String.fromCharCode(34) + ">" + user.nombre + "<span class='span'>" + "<img src='https://assotgb.org/wp-content/uploads/2018/09/Symbole-%C3%A9tudiant.png' alt='alumno' height='25' width='25'>" + "</span> </li>");
	    	
		   $('.user_item').click(function(){
		   });
		   index++;
		} else{
		   usuario.push(user);
		}
	    });
	});
 }	 
	
	
    //Agregar profesores a la lista del chat
function agregarProfesores(){
	firebase.database().ref().child("Usuarios").child("Profesores").on('value', function(snapshot) {
	    snapshot.forEach(function(child) {
		var user = {}
		user.id = child.val().id;
		user.user = child.val().user;
		user.nombre = String(child.val().nombre);
		
		if(user.user != USUARIO_ACTUAL){
		   usuarios.push(user);
		   div_user_list.append( "<li style='list-style: none;' class = 'user_item' onClick = " + String.fromCharCode(34) + "openChatBox(" + index + ")" + String.fromCharCode(34) + ">" + user.nombre + "<span class='span'>" + "<img src='http://icons.iconarchive.com/icons/iconsmind/outline/256/Professor-icon.png' alt='alumno' height='25' width='25'>" + "</span> </li>");
	    	
		   $('.user_item').click(function(){
		   });
		   index++;
		} else{
		   usuario.push(user);
		}
	    });
	});
}
   
    //Abrir ventana de chat al recibir mensaje
function abrirAlRecibir(){
firebase.database().ref().child("user-messages").child(USUARIO_ACTUAL).on('child_added', function(snapshot) {
			firebase.database().ref().child("Mensajes").child(snapshot.key).once('value').then(function(childsnapshot) {
				var id;
				if(snapshot.val() == "1"){
					user = buscarUsuario(childsnapshot.val().to);
				} else if(snapshot.val() == "2"){
					user = buscarUsuario(childsnapshot.val().from);
				}
				onChildAdded(user.user);
			});
});
}

function buscarUsuario(user){
	var us;
	for(i = 0; i < usuarios.length; i++){
		if(usuarios[i].user == user){
			us = usuarios[i];
			us.index = i;
			break;
		}
	}
	return us;
}

function onChildAdded(user){
	var usuario_temp= buscarUsuario(user);
	openChatBox(usuario_temp.index);
}

function noRepetido(id){
	var noRepe = true;
	let chat = $("#" + id);
	if (chat.length){
		noRepe = false;
	}
	return noRepe;
}

function openChatBox(index){
	let chat = $("#" + usuarios[index].user);
	var div;
	if (chat.length){
		if (chat.parent().parent().children()[1].style.display == "none"){
			chat.parent().parent().children()[1].style.display = "block";
		}
	} else {
		div = $("<div id = '" + usuarios[index].user + "'> </div>");
		$(div).chatbox({id: usuario[0].nombre.split(" ")[0],
				title : usuarios[index].nombre,
				user: usuarios[index],
				offset: 230 + 240*$('.ui-chatbox').length,
				width: 230,
				messageSent : function(id, user, msg) {
					//Guarda en base de datos los mensajes tras enviarlos en el chat
					var ref = firebase.database().ref("Mensajes");
					var ref_storage = firebase.database().ref("user-messages");
					var message = {
						"from": usuario[0].user,
						"to": user.user,
						"message": msg,
						"timestamp": Date.now()
					}
					var newRef = ref.push();
					var val = newRef.key;
					var data = {};
					data[val] = "1";
					ref_storage.child(usuario[0].user).update(data)
					data[val] = "2";
					ref_storage.child(user.user).update(data)
					newRef.set(message);

				}});
		}

		//Mostrar mensajes de conversaciones anteriores al abrir el chat
		firebase.database().ref().child("user-messages").child(USUARIO_ACTUAL).once('value').then(function(snapshot) {
			snapshot.forEach(function(child) {
				firebase.database().ref().child("Mensajes").child(child.key).once('value').then(function(childsnapshot) {
					var id;
					if(child.val() == "1"){
						id = usuario[0].nombre.split(" ")[0];
						user = buscarUsuario(childsnapshot.val().to);
					} else if(child.val() == "2"){
						user = buscarUsuario(childsnapshot.val().from);
						id = user.nombre.split(" ")[0];
					}

					if (user.user == usuarios[index].user){
						if (noRepetido(child.key)){
							mensajes.push(child.key);
							if(chat.length){
								chat.chatbox("option", "boxManager").addMsg(id, childsnapshot.val().message, child.key);
							} else{
								div.chatbox("option", "boxManager").addMsg(id, childsnapshot.val().message, child.key);
							}
						}
					}
				});
			});
		});
	}
