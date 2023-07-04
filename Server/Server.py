from Generator.CertificateGenerator import generateCertificate
from Generator.NamingGenerator import generateNameOfOrganisation
from flask import Flask, request

app = Flask(__name__)

@app.route('/savePair', methods=['POST'])
def joinServer():
    try:
        # Get credentials of client
        client_ip = request.remote_addr
        client_port = request.environ.get('REMOTE_PORT')

        # Generate Certificate - Save it
        generateCertificate(generateNameOfOrganisation(client_ip + ":" + client_port))

    except Exception:
        # TODO --- LOGGING
        return "Error, please check peer name."
    
    return 'Successfull save.'

if __name__ == '__main__':
    app.run()
