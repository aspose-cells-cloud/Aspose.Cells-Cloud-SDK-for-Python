import base64
import os
import shutil

from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.models import *
from asposecellscloud.requests import *

EmployeeSalesSummaryXlsx = "EmployeeSalesSummary.xlsx"
RemoteFolder = "PythonSDK"
# Get Cells Cloud SDK instance
# If no environment variables are configured, please obtain the ClientId and ClientSecret from https://dashboard.aspose.cloud/#/applications and replace the following values:
# instance  = CellsApi('YourClientId','YourClientSecret')
instance  = CellsApi(os.getenv('CellsCloudTestClientId'),os.getenv('CellsCloudTestClientSecret'))

# Upload a local Excel file to Cells Cloud Storage.
instance.upload_file( UploadFileRequest(EmployeeSalesSummaryXlsx, "PythonSDK/EmployeeSalesSummary.xlsx"))

#Save an Excel file of Cells Cloud as another format file of Cells Cloud.
instance.save_spreadsheet_as( SaveSpreadsheetAsRequest ( EmployeeSalesSummaryXlsx,"pdf" ,folder= RemoteFolder ) )
instance.download_file( DownloadFileRequest("PythonSDK/EmployeeSalesSummary.pdf") , local_outpath="EmployeeSalesSummary3.pdf")
save_options_data = SaveOptionsData() 
save_options_data.filename = "New_EmployeeSalesSummary.pdf"
response = instance.save_spreadsheet_as( SaveSpreadsheetAsRequest ( EmployeeSalesSummaryXlsx,"pdf" ,save_options_data, folder= RemoteFolder ) )
if response.status == "OK": 
    print("Excel file saved as another format file successfully.")
else:
    print("Error saving Excel file as another format file.")
    print(response.text)
tmp_path = instance.download_file( DownloadFileRequest("New_EmployeeSalesSummary.pdf"))
shutil.move( tmp_path ,"New_EmployeeSalesSummary.pdf")
