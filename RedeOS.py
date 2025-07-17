import socket
import subprocess

def NetworkInterfaces():
    command = subprocess.run("ifconfig", capture_output=True, text=True)
    print(command.stdout)
    
def IpAddress():
    ip = subprocess.run(["hostname", "-I"], capture_output=True, text=True)
    hostname = socket.gethostname()
    print(f"O nome do host é {hostname} e o seu endereço IP é {ip.stdout[:12:]}")

def AddressPing():
    webAdress = input("Informe o endereço desejado no formato www.example.com: ")
    print("Aguarde...")
    command = subprocess.run(["ping", webAdress, "-c 10"], capture_output=True, text=True)
    print(command.stdout)

def MachineAdress():
    machineAddress = input("Informe o endereço IP da máquina desejada no formato xxx.xxx.xxx.xxx: ")
    print("Aguarde...")
    command = subprocess.run(["ping", machineAddress, "-c 10"], capture_output=True, text=True)
    print(command.stdout)

def HostsOn():
    lan = input("Informe o endereço IP da rede no formato xxx.xxx.xxx.xxx/xx: ")
    command = subprocess.run(["nmap", "-sn", lan], capture_output=True, text=True)
    command = "\n".join([line for line in command.stdout.splitlines() if "Host is up" not in line])
    with open("log.txt", "w") as f:
        f.write(command)
    with open("log.txt", "r") as f:
        log = f.read()
        print(log)

while True:

    print("[1] Interfaces de rede do sistema")
    print("[2] Endereço IP da máquina")
    print("[3] Ping para um endereço específico")
    print("[4] Ping para uma máquina específica")
    print("[5] Verificar hosts com utilitário Nmap")
    print("[6] Para fechar o programa")

    op = int(input("\nDigite uma opção para verificar as informações: "))
    match op:

        case 1:
            NetworkInterfaces()

        case 2:
            IpAddress()

        case 3:
            AddressPing()
            
        case 4:
            MachineAdress()
            
        case 5:
            HostsOn()
        
        case 6:
            print("Programa finalizado com sucesso!")
            break

        case _:
            print("Opção inválida! Informe outra opção:\n")