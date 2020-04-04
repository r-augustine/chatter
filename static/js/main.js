document.addEventListener('DOMContentLoaded', () => {
    const socket = io.connect(`http://${document.domain}:${location.port}`);

    socket.on('connect', () => {
        // socket.send({message:'I am connected'})
        // joinRoom();
        console.log('user connected');
    });

    socket.on('disconnect', () => {
        console.log('user disconnected');
    })

    socket.on('message', data => {
        console.log(`Message received ${data.message}`);
        console.log(`Message received ${data.username}`);
        const div = document.createElement('div');
        const br = document.createElement('br');

        div.classList.add('msg');
        div.innerHTML = data.message;

        if(username != data.username){
            div.classList.add('msg-diff');
        }

        document.querySelector('#display-messages-section').append(div);
    });

    document.querySelector('#send-message').onclick = () => {
        socket.send({'message': document.querySelector('#user-message').value})
    }
    
    // const joinRoom = () => {
    //     console.log('joining...');
    //     socket.emit('join', {'username': username, 'room': 'longue'})
    // }

    // const leaveRoom = () => {
    //     console.log('leaving...');
    //     socket.emit('leave', {'username': username, 'room': 'longue'});
    // }
})