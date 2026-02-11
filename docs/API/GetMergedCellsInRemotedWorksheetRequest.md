# **Spreadsheet Cloud API: getMergedCellsInRemotedWorksheet**

Get all merged cell area form a remote spreadsheet worksheet. 


## **Quick Start**

- **Base URL**: `http://api.aspose.cloud/v4.0`
- **Authentication Method**: `JWT (OAuth2, application)`  **Token URL**: `https://api.aspose.cloud/connect/token`
- **Example** 

## **Interface Details**

### **Endpoint** 

```
GET http://api.aspose.cloud/v4.0/cells/{name}/worksheets/{worksheet}/mergedcells
```
### **Function Description**
This endpoint queries a remote spreadsheet service (e.g., Google Sheets, Office 365 Excel Online) for a specific worksheet and returns a structured list of all merged cell areas.Each merged area is typically defined by its top-left and bottom-right cell coordinates. The response is useful for data processing, layout analysis, or ensuring data integrity before performing operations that may be affected by cell merging.## **Error Handling**- **400 Bad Request**: Invalid url.- **401 Unauthorized**:  Authentication has failed, or no credentials were provided.- **404 Not Found**: Source file not accessible.- **500 Server Error** The spreadsheet has encountered an anomaly in obtaining data.

### The request parameters of **getMergedCellsInRemotedWorksheet** API are: 

| Parameter Name | Type | Path/Query String/HTTPBody | Description | 
| :- | :- | :- |:- | 
|name|String|Path|spreadsheet name|
|worksheet|String|Path|worksheet name|
|folder|String|Query|The cloud storage path of the spreadsheet.|
|storageName|String|Query|(Optional) The name of the storage if using custom cloud storage. Use default storage if omitted.|
|region|String|Query|The spreadsheet region setting.|
|password|String|Query|The password for opening spreadsheet file.|

### **Response Description**
```json
[
{
  "Name": "CellArea",
  "Type": "Class",
  "IsAbstract": false,
  "Properties": [
    {
      "Name": "EndColumn",
      "Nullable": true,
      "ReadOnly": false,
      "IsInherit": false,
      "DataType": {
        "Identifier": "Integer",
        "Name": "integer"
      }
    },
    {
      "Name": "EndRow",
      "Nullable": true,
      "ReadOnly": false,
      "IsInherit": false,
      "DataType": {
        "Identifier": "Integer",
        "Name": "integer"
      }
    },
    {
      "Name": "StartColumn",
      "Nullable": true,
      "ReadOnly": false,
      "IsInherit": false,
      "DataType": {
        "Identifier": "Integer",
        "Name": "integer"
      }
    },
    {
      "Name": "StartRow",
      "Nullable": true,
      "ReadOnly": false,
      "IsInherit": false,
      "DataType": {
        "Identifier": "Integer",
        "Name": "integer"
      }
    }
  ]
}
]
```


## OpenAPI Specification

The [OpenAPI Specification](https://reference.aspose.cloud/cells/#/ManagementController/GetMergedCellsInRemotedWorksheet) defines a publicly accessible programming interface and lets you carry out REST interactions directly from a web browser.

[[Back to API list]](../DeveloperGuide.md#api-reference)  
[[Back to README]](../../README.md)