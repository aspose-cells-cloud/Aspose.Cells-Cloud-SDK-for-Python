# **Spreadsheet Cloud API: convertTextInRemoteSpreadsheet**

Indicates converting the numbers stored as text into the correct number format, replacing unwanted characters and line breaks with the desired characters, and converting accented characters to their equivalent characters without accents. 


## **Quick Start**

- **Base URL**: `http://api.aspose.cloud/v4.0`
- **Authentication Method**: `JWT (OAuth2, application)`  **Token URL**: `https://api.aspose.cloud/connect/token`
## **Interface Details**

### **Endpoint** 

```
PUT http://api.aspose.cloud/v4.0/cells/{name}/worksheets/{worksheet}/range/{range}/content/convert/text
```
### **Function Description**
- **Convert numbers stored as text to numbers**Transform numeric data stored as text to numbers, ensuring accurate calculations and proper data representation.- **Replace specific characters**Replace all occurrences of specified characters in all the selected cells at once to standardize your information.- **Convert line breaks to space, comma or semicolon**Improve the readability of your sheets by converting line breaks to space, comma, or semicolon, creating a more organized and visually appealing presentation.- **Replace accented characters**If your data is in different languages, you have the option to swap accented characters like "é" or "ü" with their non-accented counterparts. This enhances consistency and clarity in your text.

### The request parameters of **convertTextInRemoteSpreadsheet** API are: 

| Parameter Name | Type | Path/Query String/HTTPBody | Description | 
| :- | :- | :- |:- | 
|name|String|Path|(Required) The name of the workbook file to be retrieved.|
|worksheet|String|Path|Specify the worksheet of spreadsheet.|
|range|String|Path|Specify the worksheet range of spreadsheet.|
|convertTextType|String|Query|Indicates the conversion of text type.|
|sourceCharacters|String|Query|Indicates the source characters.|
|targetCharacters|String|Query|Indicates the target characters.|
|folder|String|Query|(Optional) The folder path where the workbook is stored. The default is null.|
|storageName|String|Query|(Optional) The name of the storage if using custom cloud storage. Use default storage if omitted.|
|region|String|Query|Spreadsheet region/language setting (e.g., `en-US`, `fr-FR`). Influences number formatting, date parsing, and locale‑specific behavior.|
|password|String|Query|The password for opening spreadsheet file.|

### **Response Description**
```json
{
  "Name": "CellsCloudResponse",
  "Type": "Class",
  "IsAbstract": false,
  "Properties": [
    {
      "Name": "Code",
      "Nullable": true,
      "ReadOnly": false,
      "IsInherit": false,
      "DataType": {
        "Identifier": "Integer",
        "Name": "integer"
      }
    },
    {
      "Name": "Status",
      "Nullable": true,
      "ReadOnly": false,
      "IsInherit": false,
      "DataType": {
        "Identifier": "String",
        "Name": "string"
      }
    }
  ]
}
```


## OpenAPI Specification

The [OpenAPI Specification](https://reference.aspose.cloud/cells/#/TextProcessingController/ConvertTextInRemoteSpreadsheet) defines a publicly accessible programming interface and lets you carry out REST interactions directly from a web browser.

[[Back to API list]](../DeveloperGuide.md#api-reference)  
[[Back to README]](../../README.md)