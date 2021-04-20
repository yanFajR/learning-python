import paramiko 
import time #import time

def connect(server_ip, server_port, user, paswd): #method untuk connect ke tujuan
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server_ip,
                   server_port,
                   username=user,
                   password=paswd,
                   look_for_keys=False,
                   allow_agent=False)
    return client

def get_shell(client): #method untuk menangkap shell tujuan
    connection = client.invoke_shell()
    return connection

def send_command(connection, command): #method untuk mengirimkan command
    connection.send(command + '\n')
    time.sleep(2) #untuk menunggu eksekusi dua detik
    output = connection.recv(4096)  #menerima output eksekusi command
    return output

def close(client): #method untuk menutup koneksi
    client.close()

