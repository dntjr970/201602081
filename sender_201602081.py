import sys
import os
import socket

port = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 8000))


while 1:
   data, addr = s.recvfrom(2000)

   data = (data.decode('utf-8')).split()
   if data[0] == "exit":
       print("recevied exit command \nsystem recevied exit command.. closing my socket..")
       sys.exit()
       break
   else:
       count = 0
       s.sendto("valid list command.".encode('utf-8'), addr)

       if os.path.isfile(data[1]):
           s.sendto("file exist!".encode('utf-8'), addr)

       if os.path.isfile(data[1]):
           file_size = os.stat(data[1]).st_size
           number_file = int(file_size/2048)
           number_file2 = str(number_file)
           s.sendto(number_file2.encode('utf-8'), addr)
           time = 0

           read_file = open(data[1], 'rb')
           for i in range(0, number_file+1): 
               if int(time) == i:
                   data2, addr = s.recvfrom(2000)
                   data2.decode('utf-8')
                   data2 = int(data2)
                   time += data2
                   s.sendto("1".encode('utf-8'), addr)
                   filec = read_file.read(2048)
                   s.sendto(filec, addr)
                   count += 1
                   print("packet number ", count, "\n data sending now")
           print("sent all the files normaily")