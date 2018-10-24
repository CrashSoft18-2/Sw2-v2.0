
var USUARIO_ACTUAL = sessionStorage.getItem('user');
var mensajes = []
var mensajes = [];
var chats = [];
var index = 0;
div_user_list = $('#user_list_content ul');
 //Funcion colapsar chat
var usuarios = [];
var usuario = [];
var div;
var currentTime = Date.now()
 window.onload = main;
 function main(){
	$('#user_list_header').click(function(){
		$('#user_list').toggleClass('collapsed');
	});
	//////////////////////////////////////////////
    
	var chats = [];
	var index = 0;
	div_user_list = $('#user_list_content ul');
	agregarAlumnos();
	agregarProfesores();
	abrirAlRecibir();
}
	
	var usuarios = [];
	var usuario = [];
	var div;
	var currentTime = Date.now()
	
    //Agregar alumnos a la lista del chat
function agregarAlumnos(){
	firebase.database().ref().child("Usuarios").child("Alumnos").on('value', function(snapshot) {
	    snapshot.forEach(function(child) {
		var user = {}
@@ -37,7 +41,9 @@ var mensajes = []
		}
	    });
	});
	
}
 function agregarProfesor(){
    //Agregar profesores a la lista del chat
	firebase.database().ref().child("Usuarios").child("Profesores").on('value', function(snapshot) {
	    snapshot.forEach(function(child) {
@@ -58,11 +64,11 @@ var mensajes = []
		}
	    });
	});
	
    abrirAlRecibir()
    //Abrir ventana de chat al recibir mensaje
    function abrirAlRecibir(){
        firebase.database().ref().child("user-messages").child(USUARIO_ACTUAL).on('child_added', function(snapshot) {
}
    
//Abrir ventana de chat al recibir mensaje
function abrirAlRecibir(){
	firebase.database().ref().child("user-messages").child(USUARIO_ACTUAL).on('child_added', function(snapshot) {
				firebase.database().ref().child("Mensajes").child(snapshot.key).once('value').then(function(childsnapshot) {
					var id;
					if(snapshot.val() == "1"){
@@ -72,96 +78,96 @@ var mensajes = []
					}
					onChildAdded(user.user);
				});
        });
    }
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
function buscarUsuario(user){
	var us;
	for(i = 0; i < usuarios.length; i++){
		if(usuarios[i].user == user){
			us = usuarios[i];
			us.index = i;
			break;
		}
		return us;
	}
	return us;
}
	
	function onChildAdded(user){
		var usuario_temp= buscarUsuario(user);
		openChatBox(usuario_temp.index);
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
 	function noRepetido(id){
		var noRepe = true;
		let chat = $("#" + id);
		if (chat.length){
			noRepe = false;
function openChatBox(index){
	let chat = $("#" + usuarios[index].user);
	var div;
	if (chat.length){
		if (chat.parent().parent().children()[1].style.display == "none"){
			chat.parent().parent().children()[1].style.display = "block";
		}
		return noRepe;
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
						console.log(childsnapshot.val())
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
				}});
		}
 		//Mostrar mensajes de conversaciones anteriores al abrir el chat
		firebase.database().ref().child("user-messages").child(USUARIO_ACTUAL).once('value').then(function(snapshot) {
			snapshot.forEach(function(child) {
				firebase.database().ref().child("Mensajes").child(child.key).once('value').then(function(childsnapshot) {
					console.log(childsnapshot.val())
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
					});
					}
				});
			});
		}
		});
}
