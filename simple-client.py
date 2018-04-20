import socket
import pygame



host = '192.168.0.107'
port = 80

data = 0;

clock = pygame.time.Clock()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))


while True:
    try:
        clock.tick(1)
        s.send(str(data)+'\r\n')
        print 'sent %d' % (data)
        data += 1
    except KeyboardInterrupt:
        break

s.close()