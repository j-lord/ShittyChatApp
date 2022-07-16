// initializing a socket
var socket = io();

socket.on('connect', function() {
    console.log("chat")
});


const send_message = () => {
    $message = $("#my_message").val()
    socket.emit("global_message", $message)
    $("#my_message").val("")
}


socket.on("global_message", function(msg){
    $username = msg["username"]
    $message = msg["msg"]
    $(".chat_box").append(`<p class="message">
                            <span class="uname">${$username} : </span>
                            ${$message}</p>`)
});