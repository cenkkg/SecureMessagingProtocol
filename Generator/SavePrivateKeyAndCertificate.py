from cryptography.hazmat.primitives import serialization

def savePrivateKeyAndCertificate(privateKey, certificate, certificateSubject):

    private_key_pem = privateKey.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    certificate_pem = certificate.public_bytes(
        encoding=serialization.Encoding.PEM
    )

    with open(certificateSubject + ":certificate", "wb") as cert_file:
        cert_file.write(certificate_pem.public_bytes(serialization.Encoding.PEM))

    
    with open(certificateSubject + ":privateKey", "wb") as privateKey_file:
            privateKey_file.write(private_key_pem.public_bytes(serialization.Encoding.PEM))
    
    