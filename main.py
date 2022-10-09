import base64
from socket import *

from pip._vendor.distlib.compat import raw_input

msg = "\r\n I love computer networks!"

endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver

# Create socket called clientSocket and establish a TCP connection with mailserver

# Fill in start
MailServer = "mail.smtp2go.com"
MailPort =  80
serverPort = (MailServer, MailPort)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(serverPort)

recv = clientSocket.recv(1024)
print("Message after connection request: ", recv.decode())

if recv[:3] != '220':
    print('220 reply not received from server.\n')
# Fill in end


# Send HELO command and print server response.

helloCommand = 'HELLO Alice\r\n'
clientSocket.send(helloCommand.encode())
recv1 = clientSocket.recv(1024)
print("\nSend HELO command and print server response:", recv1.decode())

if recv1[:3] != '250':
    print('250 reply not received from server.\n')

# Fill in start
mailFromCommand = 'MAIL FROM: <sender@email.com> \r\n'
clientSocket.send(mailFromCommand.encode())
recv2 = clientSocket.recv(1024)
print("After MAIL FROM command:", recv2.decode())
# Fill in end

# Send RCPT TO command and print server response.

# Fill in start
rcptTo = "RCPT TO: <destination@email.com> \r\n"
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024)
print("After RCPT TO command: ", recv3.decode())
if recv1[:3] != '250':
    print('250 reply not received from server.\n')

# Fill in end

# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
# Fill in start
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024)
print("After DATA command: ", recv4.decode())
if recv1[:3] != '250':
    print('250 reply not received from server.\n')
# Fill in end #

# Send message data.

# Fill in start
subject = "Subject: SMTP mail client testing \r\n\r\n"
clientSocket.send(subject.encode())

message = raw_input("Enter message here: \r\n")

# Fill in end

# Message ends with a single period.
mailEndMsg = "\r\n.\r\n"

# Fill in start
clientSocket.send(message.encode())
clientSocket.send(mailEndMsg.encode())

recv5 = clientSocket.recv(1024)
print("Response after sending message body:", recv5.decode())

# Fill in end

# Send QUIT command and get server response.

# Fill in start
quitCommand = "QUIT\r\n"
clientSocket.send(quitCommand.encode())
recv6 = clientSocket.recv(1024)
print(recv6.decode())
print(quitCommand)
# Fill in end
clientSocket.close()
