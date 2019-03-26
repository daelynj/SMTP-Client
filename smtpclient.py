from socket import *

msg = "\r\n I love computer networks!"
end_msg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mail_server = 'smtp.uvic.ca'
mail_port = 25

# Create socket called clientSocket and establish a TCP connection with mailserver
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((mail_server, mail_port))

recv = client_socket.recv(1024).decode()

print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')

# Send HELO command and print server response.
helo_command = 'HELO Alice\r\n'
client_socket.send(helo_command.encode())
recv1 = client_socket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
    
# Send MAIL FROM command and print server response.
mail_from = 'mail from: jonesd@uvic.ca\r\n'
client_socket.send(mail_from.encode())
recv1 = client_socket.recv(1024).decode()

print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response. 
rcpt_to = 'rcpt to: <daewillownyou@gmail.com>\r\n'
client_socket.send(rcpt_to.encode())
recv1 = client_socket.recv(1024).decode()

print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send DATA command and print server response. 
data = 'data\r\n'
print(data)

client_socket.send(data.encode())
recv1 = client_socket.recv(1024).decode()

print(recv1)
if recv1[:3] != '354':
    print('250 reply not received from server.')

# Send message data.
msg = input()
msg = msg + '\r\n'

# Message ends with a single period.
mail_msg_ends = '.\r\n'
print(mail_msg_ends)
client_socket.send(msg.encode() + mail_msg_ends.encode())
recv1 = client_socket.recv(1024).decode()

print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# # Send QUIT command and get server response.
quit_cmd = 'quit\r\n'

client_socket.send(quit_cmd.encode())
print(quit_cmd)
recv1 = client_socket.recv(1024).decode()

print(recv1)
if recv1[:3] != '221':
    print('250 reply not received from server.')