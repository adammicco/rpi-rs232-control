$command = $args[0]
$data = [System.Text.Encoding]::ASCII.GetBytes($command)

$port = 8080
$remoteHost = "raspberrypi.local"

$socket = new-object System.Net.Sockets.TcpClient($remoteHost, $port)
$stream = $socket.GetStream()

$stream.Write($data, 0, $data.length)