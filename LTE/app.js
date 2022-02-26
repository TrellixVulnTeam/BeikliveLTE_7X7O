var express = require('express'),
	app = express(),
	server = require('http').createServer(app),
	io = require('socket.io')(server),
	port = process.env.PORT || 6600;	//服务器端口

app.use(express.static(__dirname));

io.on('connection', (socket) => {




})

server.listen(port, () => {
	console.log('listening on %d...', port);
	console.log('open browser: 127.0.0.1:%d', port)
});