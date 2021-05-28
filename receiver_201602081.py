import sys
import os
import socket

ip_addr = sys.argv[1]
port = sys.argv[2]

r = socket.socket(socket.AF_INET, socket.SOCK_DGRAM | socket.SOCK_NONBLOCK)
r.settimeout(15)
r.bind(('', int(port)))

while 1:
    t = input("enter a command:\n1. receive [file_name]\n2. exit\n")
    s_t = t.split()
    r.sendto(t.encode('utf-8'), (sys.argv[1], int(sys.argv[2])))
    print("checking acknowledgment of command")

    if s_t[0] == "exit":
        print("received exit command \nsystem received exit command.. closing my socket..")
        sys.exit()
        break
    else:
        data, addr = r.recvfrom(2000)
        data = data.decode('utf-8')
        print(data)

        if data == "valid list command.":
            data1, addr = r.recvfrom(2000)
            data1 = data1.decode('utf-8')
            
            read_file = open(s_t[1], 'wb')

            if data1 == "file exist!":
                data2, addr = r.recvfrom(2000)
                check = data2.decode('utf-8')
                check = int(check)
                count = 0
                
                time = 0
                for i in range(0, check+1):
                    if time == i:
                        r.sendto("1".encode('utf-8'), addr)
                        data5, addr = r.recvfrom(2000)
                        data5.decode('utf-8')
                        time += 1
                        data3, addr = r.recvfrom(2048)
                        read_file.write(data3)
                        count += 1
                    print("Received packet number:", count) 

                print("new received file closed. check contents in directory.")
