import socket
import switch as sw
from vars import STATUS_ERROR, STATUS_ALIVE, STATUS_EXIT

    
#############################
### Server initialization ###
#############################


host = "0.0.0.0"
port = 1337

# Create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Reuse addr
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print("Binding server on addr {} and port {}".format(host, port))
# Bind the socket to a public host and some port
serversocket.bind((host, port))

# Become a server socket
# Queue up as many as 50 connect requests before refusing outside connections.
serversocket.listen(5)

#leading_symbol = b'> '
leading_symbol = b'>> '


####################
### Forever loop ###
####################

while True:
    # Accept connections from outside
    conn, addr = serversocket.accept()
    print('Connected with ' + addr[0] + ":" + str(addr[1]))
    swcmd = sw.SwitcherCommands()
    data, status = swcmd.get_command("banner")
    conn.send(data)
    while conn:
        conn.send(leading_symbol)
        data = conn.recv(1024)
        try:
            data = data.decode('utf-8')
            data = data.strip()
        except UnicodeDecodeError as e:
            data = ""
            conn.close()
            break

        tosend, status = swcmd.get_command(data)
        if status == STATUS_ALIVE:
            conn.sendall(tosend)
            
        elif status == STATUS_ERROR:
            conn.sendall("An glitch appeared during command execution.\n".encode('utf-8'))
            conn.sendall("Glitched: {}.\n".format(tosend).encode('utf-8')) 
 
        elif status == STATUS_EXIT:
            conn.sendall("\nConnection to interface has been shutdown.\n".encode('utf-8'))
            conn.close()
            break

