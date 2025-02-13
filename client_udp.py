import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        msg = input('Você: ') + '\n'
        client.sendto(msg.encode(), ('127.0.0.1', 2805))
        data, sender = client.recvfrom(1024)
        print('IP:',sender[0] + ': ' + data.decode())
        if data.decode() == 'sair\n' or msg == 'sair\n':
            break
            print('--------------------------------')
            print('---> Conexão finalizada!')

except Exception as error:
    print('---> Erro de conexão')
    print('--------------------------------')
    print(error)
    print('--------------------------------')
    client.close()