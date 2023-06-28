import socket
from cryptography.hazmat.primitives import serialization
from Generator.PrivateKeyGenerator import generatePrivateKey
from Generator.CertificateGenerator import generateCertificate
from Generator.NamingGenerator import generateNameOfOrganisation
from ServerHelper import savePrivateKeyAndCertificate
from flask import Flask, request

app = Flask(__name__)

@app.route('/flush', methods=['POST'])
def joinServer(peerName):
    try:
        # Get credentials of client
        client_ip = request.remote_addr
        client_port = request.environ.get('REMOTE_PORT')

        # Okey, save certificate and private key.
        privateKey  = generatePrivateKey()
        certificate = generateCertificate(privateKey, generateNameOfOrganisation(peerName))
        savePrivateKeyAndCertificate(privateKey, certificate)
    except Exception:
        # TODO --- LOGGING
        return "Error, please check peer name."
    return 'Successfull save.'

if __name__ == '__main__':
    app.run()
