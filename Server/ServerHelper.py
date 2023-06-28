def savePrivateKeyAndCertificate(privateKey, certificate):
    # Save the private key and certificate
    private_key_pem = privateKey.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    cert_pem = certificate.public_bytes(
        serialization.Encoding.PEM
    )

    with open('private_key.pem', 'wb') as f:
        f.write(private_key_pem)

    with open('certificate.pem', 'wb') as f:
        f.write(cert_pem)