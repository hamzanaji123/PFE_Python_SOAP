from zeep import Client
from zeep.exceptions import Fault
import pytest

# URL du WSDL de la calculatrice
WSDL_URL = 'http://www.dneonline.com/calculator.asmx?wsdl'

# Une "fixture" Pytest pour créer le client SOAP une seule fois pour tous les tests
# C'est une bonne pratique pour éviter de recréer l'objet à chaque test
@pytest.fixture(scope="module")
def soap_client():
    """Initialise et retourne un client Zeep pour le service de calculatrice."""
    client = Client(WSDL_URL)
    return client

# Test pour l'opération 'Add'
def test_add_operation(soap_client):
    """Vérifie que l'opération Add fonctionne correctement."""
    result = soap_client.service.Add(5, 7)
    assert result == 12, "L'addition 5 + 7 devrait être 12"

# Test pour l'opération 'Subtract'
def test_subtract_operation(soap_client):
    """Vérifie que l'opération Subtract fonctionne correctement."""
    result = soap_client.service.Subtract(10, 3)
    assert result == 7, "La soustraction 10 - 3 devrait être 7"

# Un test supplémentaire pour un autre scénario (ex: multiplication)
def test_multiply_operation(soap_client):
    """Vérifie que l'opération Multiply fonctionne correctement."""
    result = soap_client.service.Multiply(4, 5)
    assert result == 20, "La multiplication 4 * 5 devrait être 20"

# Un test pour un cas d'échec attendu (ex: diviser par zéro, si l'API le gère spécifiquement)
# Ce service de calculatrice renvoie un nombre, pas une erreur explicite pour div par zéro,
# mais c'est un bon exemple de ce qu'on ferait pour une vraie API.
# Un test pour un cas d'échec attendu (ex: diviser par zéro)
# Un test pour un cas d'échec attendu (ex: diviser par zéro)
def test_divide_by_zero_handling(soap_client):
    """
    Vérifie que la division par zéro lève une exception SOAP (Fault).
    """
    with pytest.raises(Fault) as excinfo:
        soap_client.service.Divide(1, 0)

    # Optionnel: Vérifier le message de l'erreur si tu veux être très spécifique
    # C'est une bonne pratique pour des API de paiement où les messages d'erreur sont importants
    assert "Arithmetic operation resulted in an overflow" in str(excinfo.value)
    assert "Server was unable to process request" in str(excinfo.value)
