import base64
import os
import uuid
from pathlib import Path

from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *
from datetime import datetime

bookFormulaXlsx = "BookFormula.xlsx"
remoteFolder = "PythonSDK"
asposecellsMSI = "PowerShell-7.5.3-win-x64.msi"
# If no environment variables are configured, please obtain the ClientId and ClientSecret from https://dashboard.aspose.cloud/#/applications and replace the following values:
# instance  = CellsApi('YourClientId','YourClientSecret')
instance  = CellsApi(os.getenv('CellsCloudClientId'),os.getenv('CellsCloudClientSecret'))

# bytes_content = Path(bookFormulaXlsx).read_bytes()
# uploaded_filename = str(uuid.uuid4()) + ".xlsx"
# instance.upload_file(  UploadFileRequest( bytes_content, remoteFolder +"/" + uploaded_filename))
#
# instance.upload_file(  UploadFileRequest( bookFormulaXlsx, remoteFolder +"/" + bookFormulaXlsx))
#
# page_count = instance.get_page_count( GetPageCountRequest(bookFormulaXlsx ,folder= remoteFolder ) )
# print(int(page_count))
if os.path.exists(asposecellsMSI):
    # start = datetime.now()
    # instance.upload_file(  UploadFileRequest( asposecellsMSI, asposecellsMSI))
    # end = datetime.now()
    # duration = end - start
    # print(f"Upload time taken:{start} -- {end} -- {duration.total_seconds():.2f} second.")
    start = datetime.now()
    instance.download_file(  DownloadFileRequest( asposecellsMSI) , local_outpath=asposecellsMSI +"_Downloaded.msi" )
    end = datetime.now()
    duration = end - start
    print(f"Download time taken:{start} -- {end} -- {duration.total_seconds():.2f} second.")
