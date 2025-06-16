from zeep import Client
from zeep.exceptions import Fault

# URL du WSDL de la calculatrice
wsdl_url = 'http://www.dneonline.com/calculator.asmx?wsdl'

try:
    # Création d'un client SOAP à partir du WSDL
    client = Client(wsdl_url)

    # --- DEBUT : COMMENTE OU SUPPRIME CES LIGNES ---
    # print("Opérations disponibles :")
    # for service_name in client.wsdl.services:
    #     service = client.wsdl.services[service_name]
    #     for port_name in service.ports:
    #         port = service.ports[port_name]
    #         for operation_name in port.binding.operations:
    #             print(f"  - {operation_name}")
    # --- FIN : COMMENTE OU SUPPRIME CES LIGNES ---


    # Appel de l'opération 'Add'
    num1 = 5
    num2 = 7
    result_add = client.service.Add(num1, num2)
    print(f"\n{num1} + {num2} = {result_add}")

    # Appel de l'opération 'Subtract'
    num3 = 10
    num4 = 3
    result_subtract = client.service.Subtract(num3, num4)
    print(f"{num3} - {num4} = {result_subtract}")

except Fault as e:
    print(f"Erreur SOAP : {e}")
except Exception as e:
    print(f"Une erreur inattendue est survenue : {e}")