import socket 
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor


#lista que eu pesquisei as possiveis conexoes com a porta nao confie que realmente seja :p
Port_Names_principais = {
    20: "ftp-data",
    21: "ftp",
    22: "ssh",
    23: "telnet",
    25: "smtp",
    53: "dns",
    67: "dhcp-server",
    68: "dhcp-client",
    69: "tftp",
    80: "http",
    88: "kerberos",
    110: "pop3",
    123: "ntp",
    135: "msrpc",
    137: "netbios-ns",
    138: "netbios-dgm",
    139: "netbios-ssn",
    143: "imap",
    161: "snmp",
    389: "ldap",
    443: "https",
    445: "microsoft-ds/smb",
    465: "smtps",
    500: "ike-ipsec",
    514: "syslog",
    636: "ldaps",
    853: "dns-over-tls",
    993: "imaps",
    995: "pop3s",
    1433: "ms-sql-s",
    1521: "oracle",
    2049: "nfs",
    3306: "mysql",
    3389: "ms-wbt-server/rdp",
    5432: "postgresql",
    5900: "vnc",
    6379: "redis",
    8080: "http-proxy",
    8443: "https-alt",
    9200: "elasticsearch",
    11211: "memcached",
    27017: "mongodb"
} 


IP = input("Digite o ip desejado: ")

def opcao_portascomuns():
    for port in Port_Names_principais:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        s.settimeout(0.1)

        status = s.connect_ex((f"{IP}", port))

        if status == 0:
            print(f"[+] {port} is OPEN SERVICE: {Port_Names_principais[port]}")


def scan_single_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.3)
    try:
        status = s.connect_ex((IP, port))
        if status == 0:
            try:
                service_name = socket.getservbyport(port, "tcp")
            except OSError:
                service_name = "desconhecido"
            print(f"[+] {port} is OPEN SERVICE: {service_name}")
    except Exception:
        pass
    finally:
        s.close()



def todas_portas():
    print(f"Iniciando varredura em {IP} às {datetime.now()}")

    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(scan_single_port, range(1, 65536))

    print(f"A analise foi finalizada às {datetime.now()}")


def Imprimir_Menu():
    print("#############################")
    print("Opcão 1: analisar portas comuns.")
    print("Opcão 2: analisar todas as portas.")
    print("Opcão 3: fechar o programa.")
    print("#############################")


while True:
    Imprimir_Menu()
    
    selection = input("Qual opção deseja utilizar: ")
    if selection == "1":
        opcao_portascomuns()
    elif selection == "2":
        todas_portas()
    elif selection == "3":
        print("Fechando programa.")
        break
    else:
        print("Opção invalida\n")
