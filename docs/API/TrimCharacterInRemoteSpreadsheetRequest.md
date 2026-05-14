# **Spreadsheet Cloud API: trimCharacterInRemoteSpreadsheet**

The TrimSpreadsheetContent API is designed to process and trim content within a spreadsheet. This API allows users to remove extra spaces, line breaks, or other unnecessary characters from the content of selected cells. It is particularly useful for cleaning up data entries and ensuring consistency in spreadsheet formatting 


## **Quick Start**

- **Base URL**: `http://api.aspose.cloud/v4.0`
- **Authentication Method**: `JWT (OAuth2, application)`  **Token URL**: `https://api.aspose.cloud/connect/token`
## **Interface Details**

### **Endpoint** 

```
PUT http://api.aspose.cloud/v4.0/cells/{name}/worksheets/{worksheet}/range/{range}/content/trim
```
### **Function Description**
Based on the functional description provided, the following is a summary of the data cleansing tool:## **Core Features Overview**The tool focuses on text formatting cleanup and provides a variety of whitespace and newline processing functions to ensure that spreadsheet data is clean, professional and easy to use.## ** Primary Cleaning Capacity**- **Trim the first and last spaces** - Remove extra spaces at the beginning and end of text - Improve data appearance neatness and readability- **Processing of extra spaces between words** - Eliminate extra spaces between words - Solve the format confusion caused by multi-source data- **Special spaces removed** - Specially clear non-breaking spaces - Ensure data accuracy and consistency- **Line break management** - Remove extra or all line breaks. - Keep cell content organized and professional looking## ** Functional Value**Through comprehensive space and line break cleaning, the tool can effectively improve data quality, eliminate data processing obstacles caused by format problems, and provide users with a reliable and clean spreadsheet environment.        

### The request parameters of **trimCharacterInRemoteSpreadsheet** API are: 

| Parameter Name | Type | Path/Query String/HTTPBody | Description | 
| :- | :- | :- |:- | 
|name|String|Path|Specify the spreadsheet name on remote server.|
|worksheet|String|Path|Specify the worksheet of spreadsheet.|
|range|String|Path|Specify the worksheet range of spreadsheet.|
|trimContent|String|Query|Specify the trim content.|
|trimLeading|Boolean|Query|Specify to trim content from the beginning.|
|trimTrailing|Boolean|Query|Specify to trim content from the end.|
|trimSpaceBetweenWordTo1|Boolean|Query|Remove excess spaces between words within a cell.|
|trimNonBreakingSpaces|Boolean|Query|Remove non-breaking spaces.|
|removeExtraLineBreaks|Boolean|Query|Remove extra line breaks.|
|removeAllLineBreaks|Boolean|Query|Remove all line breaks.|
|folder|String|Query|Specify the spreadsheet storage position on remote server|
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

The [OpenAPI Specification](https://reference.aspose.cloud/cells/#/TextProcessingController/TrimCharacterInRemoteSpreadsheet) defines a publicly accessible programming interface and lets you carry out REST interactions directly from a web browser.

[[Back to API list]](../DeveloperGuide.md#api-reference)  
[[Back to README]](../../README.md)