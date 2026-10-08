import socket 

Port_Names = {
    21 : "ftp",
    22 : "ssh",
    23 : "telnet",
    80 : "http",
    443 : "https",
    445: "SMB",
    3389 : "RDP",
} 


IP = input("Digite o IP que deseja escanear: ")


for port in Port_Names:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    s.settimeout(0.5)

    status = s.connect_ex((f"{IP}", port))

    if status == 0:
        print(f"{port} is OPEN SERVICE: {Port_Names[port]}")
    else:
        print(f"{port} is CLOSED SERVICE: {Port_Names[port]}")
