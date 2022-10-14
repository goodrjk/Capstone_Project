var http = require("http");
var server = http.createServer(function (req, res) {
res.writeHead(200);
res.end("Initial Index File For UdaPeople Backend");
});
server.listen(3000);
