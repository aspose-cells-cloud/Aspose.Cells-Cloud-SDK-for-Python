# **Spreadsheet Cloud API: importJSONDataIntoSpreadsheet**

Import JSON data file into the local spreadsheet. 


## **Quick Start**

- **Base URL**: `http://api.aspose.cloud/v4.0`
- **Authentication Method**: `JWT (OAuth2, application)`  **Token URL**: `https://api.aspose.cloud/connect/token`
## **Interface Details**

### **Endpoint** 

```
PUT http://api.aspose.cloud/v4.0/cells/import/data/json
```
### **Function Description**
The method parses the JSON, maps the data to the spreadsheet's cell structure, and saves the file locally. Supported spreadsheet formats include .xlsx and .ods.## **Error Handling**- **400 Bad Request**: Invalid url.- **401 Unauthorized**:  Authentication has failed, or no credentials were provided.- **404 Not Found**: Source file not accessible.- **500 Server Error** The spreadsheet has encountered an anomaly in obtaining data.## **Key Features and Benefits**- **Direct Spreadsheet Integration**: Imports data directly into the specified spreadsheet.- **Efficient Data Handling**: Processes data efficiently, ensuring accurate parsing and insertion.        

### The request parameters of **importJSONDataIntoSpreadsheet** API are: 

| Parameter Name | Type | Path/Query String/HTTPBody | Description | 
| :- | :- | :- |:- | 
|datafile|File|FormData|Upload data file.|
|Spreadsheet|File|FormData|Upload spreadsheet file.|
|worksheet|String|Query|Need to import JSON data into the worksheet.|
|startcell|String|Query|Starting position for data import|
|insert|Boolean|Query|Controls the insertion behavior. true: inserts data; false: overwrites existing data.|
|outPath|String|Query|(Optional) The folder path where the workbook is stored. The default is null.|
|outStorageName|String|Query|Output file Storage Name.|
|fontsLocation|String|Query|Use Custom fonts.|
|region|String|Query|The spreadsheet region setting.|
|password|String|Query|The password for opening spreadsheet file.|

### **Response Description**
```json
{
File
}
```


## OpenAPI Specification

The [OpenAPI Specification](https://reference.aspose.cloud/cells/#/DataProcessingController/ImportJSONDataIntoSpreadsheet) defines a publicly accessible programming interface and lets you carry out REST interactions directly from a web browser.

[[Back to API list]](../DeveloperGuide.md#api-reference)  
[[Back to README]](../../README.md)