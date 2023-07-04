from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from Macros.MacroDefinitions import blobStorageConnectionString
from Macros.MacroDefinitions import blobStorageConnectionName

def blobClient(filePath):
    blobServiceClient = BlobServiceClient.from_connection_string(blobStorageConnectionString)
    containerClient = blobServiceClient.get_container_client(blobStorageConnectionName)

    

