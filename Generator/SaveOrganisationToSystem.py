from PrivateKeyGenerator import generatePrivateKey
from CertificateGenerator import generateCertificate

def saveOrganisationToSystem(organisationID):
    # Sign-up into database.
    try:
        generateCertificate(organisationID)

    except Error as e:
        print("Error during saving certificates.")