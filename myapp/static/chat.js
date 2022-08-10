// initializing a socket
var socket = io();
socket.on('connect', function() {
    console.log("chat")
    // mymessage = "I am logged in"
    // socket.emit('login_message', mymessage);
});

// send message when user clicks send button
const send_message = () => {
    $message = $("#my_message").val()
    socket.emit("global_message", $message)
    $("#my_message").val("")
}

// receive message and send to browser
socket.on("global_message", function(msg){
    $username = msg["username"]
    $message = msg["msg"]
    $(".chat_box").append(`<p class="message">
                            <span class="uname">${$username} : </span>
                            ${$message}</p>`)
});


// after this is when you will call the learnIt.py script to run a query
