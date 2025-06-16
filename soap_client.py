from zeep import Client

# WSDL de démonstration (service public)
WSDL_URL = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"

def convert_number_to_words(number: int) -> str:
    """
    Appelle le service SOAP pour convertir un nombre en toutes lettres.
    """
    client = Client(wsdl=WSDL_URL)
    result = client.service.NumberToWords(ubiNum=number)
    return result

if __name__ == "__main__":
    number = 123
    print(f"Résultat : {convert_number_to_words(number)}")
