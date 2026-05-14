# **Spreadsheet Cloud API: addTextInRemoteSpreadsheet**

Specify appending text to multiple cells at once, allowing you to add prefixes, suffixes, labels, or any specific characters. You can choose the exact position of the text—in the beginning, at the end, or before or after certain characters in the cell. 


## **Quick Start**

- **Base URL**: `http://api.aspose.cloud/v4.0`
- **Authentication Method**: `JWT (OAuth2, application)`  **Token URL**: `https://api.aspose.cloud/connect/token`
## **Interface Details**

### **Endpoint** 

```
PUT http://api.aspose.cloud/v4.0/cells/{name}/worksheets/{worksheet}/range/{range}/content/add/text
```
### **Function Description**
Bulk-inserts the supplied string into every cell of the chosen range at the exact position you specify(prefix, suffix, before/after a given substring, or offset).  - **position** enum: None, AtTheBeginning, AtTheEnd, BeforeText, AfterText.  - **selectText**: when `BeforeText` or `AfterText` is used, this field supplies the anchor substring; if the anchor is not found the cell is left unchanged.- **skipEmptyCells**: `true` → only non-blank cells are processed; `false` → empty cells receive the new text directly.- **Numeric / boolean / formula cells** are converted to string before insertion; formulas are **dropped** to avoid corruption.- Returns the **count of touched cells** and the updated workbook stream.

### The request parameters of **addTextInRemoteSpreadsheet** API are: 

| Parameter Name | Type | Path/Query String/HTTPBody | Description | 
| :- | :- | :- |:- | 
|name|String|Path|(Required) The name of the workbook file to be retrieved.|
|worksheet|String|Path|Specify the worksheet of spreadsheet.|
|range|String|Path|Specify the worksheet range of spreadsheet.|
|text|String|Query|Specify the added text content.|
|position|String|Query|Indicates the specific location for adding text content.None, AtTheBeginning, AtTheEnd, BeforeText, AfterText.|
|selectText|String|Query|Indicates selecting the specific position to add text based on the content of the text.|
|skipEmptyCells|Boolean|Query|Indicates skip empty cells.|
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

The [OpenAPI Specification](https://reference.aspose.cloud/cells/#/TextProcessingController/AddTextInRemoteSpreadsheet) defines a publicly accessible programming interface and lets you carry out REST interactions directly from a web browser.

[[Back to API list]](../DeveloperGuide.md#api-reference)  
[[Back to README]](../../README.md)