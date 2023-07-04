from PrivateKeyGenerator import generatePrivateKey
from CertificateGenerator import generateCertificate
from SavePrivateKeyAndCertificate import savePrivateKeyAndCertificate

def saveOrganisationToSystem(organisationID):
    # Sign-up into database.
    try:
        newPrivateKey = generatePrivateKey()
        newCertificate = generateCertificate(organisationID, newPrivateKey)
        savePrivateKeyAndCertificate(newPrivateKey, newCertificate, organisationID)

    except Error as e:
        print("Error during creting certificate or private key.")