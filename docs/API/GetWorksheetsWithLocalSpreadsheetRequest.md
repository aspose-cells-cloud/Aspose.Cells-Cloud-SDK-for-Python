# **Spreadsheet Cloud API: getWorksheetsWithLocalSpreadsheet**

Fetches a complete list of worksheets from the currently active local spreadsheet. 


## **Quick Start**

- **Base URL**: `http://api.aspose.cloud/v4.0`
- **Authentication Method**: `JWT (OAuth2, application)`  **Token URL**: `https://api.aspose.cloud/connect/token`
## **Interface Details**

### **Endpoint** 

```
PUT http://api.aspose.cloud/v4.0/cells/spreadsheet/worksheets
```
### **Function Description**
This endpoint accesses the local spreadsheet application (e.g., Excel) via interop or a local API,collects the name and type (e.g., standard, chart, macro) of every worksheet,and returns the collection as a structured JSON array. This is typically used to populatea worksheet selector UI or to audit spreadsheet contents.## **Error Handling**- **400 Bad Request**: Invalid url.- **401 Unauthorized**:  Authentication has failed, or no credentials were provided.- **404 Not Found**: Source file not accessible.- **500 Server Error** The spreadsheet has encountered an anomaly in obtaining data.

### The request parameters of **getWorksheetsWithLocalSpreadsheet** API are: 

| Parameter Name | Type | Path/Query String/HTTPBody | Description | 
| :- | :- | :- |:- | 
|Spreadsheet|File|FormData|Upload spreadsheet file.|
|region|String|Query|The spreadsheet region setting.|
|password|String|Query|The password for opening spreadsheet file.|

### **Response Description**
```json
{
String
}
```


## OpenAPI Specification

The [OpenAPI Specification](https://reference.aspose.cloud/cells/#/ManagementController/GetWorksheetsWithLocalSpreadsheet) defines a publicly accessible programming interface and lets you carry out REST interactions directly from a web browser.

[[Back to API list]](../DeveloperGuide.md#api-reference)  
[[Back to README]](../../README.md)