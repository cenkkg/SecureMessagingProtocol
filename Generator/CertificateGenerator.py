from cryptography import x509
import datetime
from Generator.PrivateKeyGenerator import generatePrivateKey
from cryptography.hazmat.primitives import hashes
from SaveProvateKeyAndCertificate import savePrivateKeyAndCertificate


def generateCertificate(certificateSubject):

    private_key = generatePrivateKey()

    subject = x509.Name([
        x509.NameAttribute(x509.NameOID.COMMON_NAME, certificateSubject),
    ])


    cert = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        subject
    ).public_key(
        private_key.public_key()
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.datetime.utcnow()
    ).not_valid_after(
        datetime.datetime.utcnow() + datetime.timedelta(days=365)
    ).sign(private_key, hashes.SHA256())


    savePrivateKeyAndCertificate(private_key, cert, certificateSubject)
