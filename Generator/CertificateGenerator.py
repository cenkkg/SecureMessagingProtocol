from cryptography import x509
import datetime

def generateCertificate(privateKey, certificateSubject):
    subject = x509.Name([
        x509.NameAttribute(x509.NameOID.COMMON_NAME, certificateSubject),
    ])
    cert = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        subject
    ).public_key(
        privateKey.public_key()
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.datetime.utcnow()
    ).not_valid_after(
        datetime.datetime.utcnow() + datetime.timedelta(days=365)
    ).sign(privateKey, hashes.SHA256())