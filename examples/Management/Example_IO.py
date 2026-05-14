import base64
import os
import shutil
import uuid

from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

bookFormulaXlsx = "BookFormula.xlsx"
remoteFolder = "PythonSDK"

# If no environment variables are configured, please obtain the ClientId and ClientSecret from https://dashboard.aspose.cloud/#/applications and replace the following values:
# instance  = CellsApi('YourClientId','YourClientSecret')
instance  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'))

# 1 Check the formula error for an online Excel file in the Cells Cloud Storage.
file_path = str( uuid.uuid4())
print(file_path)
shutil.copy2(bookFormulaXlsx,file_path)
# instance.upload_file(  UploadFileRequest( file_path,file_path))
instance.upload_file(  UploadFileRequest( file_path))
# with open(bookFormulaXlsx, "rb") as f:
#     data = f.read()  
#     instance.upload_file(  UploadFileRequest( data, file_path +".xlsx"))
#     instance.upload_file(  UploadFileRequest( data, file_path))



instance.upload_file(  UploadFileRequest( bookFormulaXlsx, remoteFolder + '/' + bookFormulaXlsx))

tmp_path = instance.download_file( DownloadFileRequest(remoteFolder + '/' + bookFormulaXlsx))
shutil.move( tmp_path ,"DownloadFile_BookFormula.xlsx")
