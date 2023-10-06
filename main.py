#INTEGRANTES:
#GUILLERMO AMPUERO RAZURI
#AARON ZELA ROJAS
#####
# Importa el módulo 'ipaddress' para trabajar con direcciones IP y subredes
import ipaddress

# Define una función llamada 'subnet_calculator' que toma una dirección IP y una máscara de subred como argumentos
def subnet_calculator(ip, subnet_mask):
    try:
        # Crea un objeto IPv4Network utilizando la dirección IP y la máscara de subred proporcionadas
        network = ipaddress.IPv4Network(f'{ip}/{subnet_mask}', strict=False)

        # Muestra información sobre la red original
        print(f'Red Original: {network.network_address}/{subnet_mask}')
        print(f'Dirección de Broadcast: {network.broadcast_address}')
        print(f'Número de hosts disponibles: {network.num_addresses}')

        # Muestra información sobre las subredes
        print("\nSubredes:")
        # Divide la red original en subredes con un prefijo diferente de 3 bits (personalizable)
        for subnet in network.subnets(prefixlen_diff=3):
            print(f'Subred: {subnet.network_address}/{subnet.prefixlen}')
            print(f'Dirección de Broadcast: {subnet.broadcast_address}')
            print(f'Número de hosts disponibles: {subnet.num_addresses}')
            print('-' * 30)

    except ValueError as e:
        # Captura y muestra cualquier excepción que pueda ocurrir
        print(f"Error: {e}")

# Verifica si el script se está ejecutando como programa principal
if __name__ == "__main__":
    # Solicita al usuario ingresar una dirección IP y una máscara de subred
    ip = input("Introduce la dirección IP (Ejemplo: 192.168.1.0): ")
    subnet_mask = int(input("Introduce la máscara de subred (Ejemplo: 24): "))

    # Llama a la función 'subnet_calculator' con los valores proporcionados por el usuario
    subnet_calculator(ip, subnet_mask)

