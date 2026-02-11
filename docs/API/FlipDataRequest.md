# **Spreadsheet Cloud API: flipData**

Transposes a specified data range (rows become columns, columns become rows). 


## **Quick Start**

- **Base URL**: `http://api.aspose.cloud/v4.0`
- **Authentication Method**: `JWT (OAuth2, application)`  **Token URL**: `https://api.aspose.cloud/connect/token`
## **Interface Details**

### **Endpoint** 

```
PUT http://api.aspose.cloud/v4.0/cells/flip
```
### **Function Description**
This API flips the orientation of a given data matrix. For example, a 3x2 range (3 rows, 2 columns) will become a 2x3 range (2 rows, 3 columns) in the output. It is commonly used for restructuring data to meet the input requirements of different charts, reports, or data models.

### The request parameters of **flipData** API are: 

| Parameter Name | Type | Path/Query String/HTTPBody | Description | 
| :- | :- | :- |:- | 
|Spreadsheet|File|FormData|Upload spreadsheet file.|
|worksheet|String|Query|The worksheet name.|
|cellArea|String|Query|A specified data range|
|Horizontal|Boolean|Query|Horizontal/Vertical Flip.|
|outPath|String|Query|(Optional) The folder path where the workbook is stored. The default is null.|
|outStorageName|String|Query|Output file Storage Name.|
|region|String|Query|The spreadsheet region setting.|
|password|String|Query|The password for opening spreadsheet file.|

### **Response Description**
```json
{
File
}
```


## OpenAPI Specification

The [OpenAPI Specification](https://reference.aspose.cloud/cells/#/TransformController/FlipData) defines a publicly accessible programming interface and lets you carry out REST interactions directly from a web browser.

[[Back to API list]](../DeveloperGuide.md#api-reference)  
[[Back to README]](../../README.md)