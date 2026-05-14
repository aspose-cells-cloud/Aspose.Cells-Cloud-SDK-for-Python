import os
from asposecellscloud.apis.cells_api import CellsApi
from asposecellscloud.requests import *

# 1. Initialize API Client
instance = CellsApi(os.getenv('CellsCloudClientId'), os.getenv('CellsCloudClientSecret'))

# 2. Prepare Parameters
# Required: name (str), sheet_name (str), row_index (int)
# Optional: folder (str), storage_name (str)
name = "EmployeeSalesSummary.xlsx"
sheet_name = "Sales"
row_index = 1
folder = ""
storage_name = ""  # optional parameter example

try:
    # 3. Build Request Object
    # Required parameters are passed positionally; optional parameters as keywords
    put_insert_worksheet_row_request = PutInsertWorksheetRowRequest(
        name,
        sheet_name,
        row_index,
        folder=folder,
        storage_name=storage_name
    )

    # 4. Call API Method
    result = instance.put_insert_worksheet_row(put_insert_worksheet_row_request)

    print("API call successful:", result)

except Exception as e:
    print("API call failed:", e)