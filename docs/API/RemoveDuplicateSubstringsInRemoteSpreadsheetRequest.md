# **Spreadsheet Cloud API: removeDuplicateSubstringsInRemoteSpreadsheet**

Finds and removes repeated substrings inside every cell of the chosen range, using user-defined or preset delimiters, while preserving formulas, formatting and data-validation. 


## **Quick Start**

- **Base URL**: `http://api.aspose.cloud/v4.0`
- **Authentication Method**: `JWT (OAuth2, application)`  **Token URL**: `https://api.aspose.cloud/connect/token`
## **Interface Details**

### **Endpoint** 

```
PUT http://api.aspose.cloud/v4.0/cells/{name}/worksheets/{worksheet}/range/{range}/content/remove/duplicate-substrings
```
### **Function Description**
**How duplicates are detected**  1. Each cell value is split into substrings by the chosen delimiter(s).  2. The tool compares substrings **within the same cell** and keeps only the **first occurrence** of each duplicate.  3. Cleaned substrings are re-joined with the same delimiter(s) and written back to the cell.            **Delimiter options**  - Preset list: comma, semicolon, space, tab, line-break  - `Custom` – enter any character(s); multiple characters are treated as one composite delimiter  - `TreatConsecutiveDelimitersAsOne` – collapse adjacent delimiters into a single separator              Only string-type cells are processed; numbers, booleans and formulas are converted to string before splitting (formulas are dropped).  Returns the count of cleaned cells and the updated workbook stream.  

### The request parameters of **removeDuplicateSubstringsInRemoteSpreadsheet** API are: 

| Parameter Name | Type | Path/Query String/HTTPBody | Description | 
| :- | :- | :- |:- | 
|name|String|Path|(Required) The name of the workbook file to be retrieved.|
|worksheet|String|Path|Specify the worksheet of spreadsheet.|
|range|String|Path|Specify the worksheet range of spreadsheet.|
|delimiters|String|Query|comma, semicolon, space, tab, line-break |
|treatConsecutiveDelimitersAsOne|Boolean|Query|collapse adjacent delimiters into a single separator.|
|caseSensitive|Boolean|Query||
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

The [OpenAPI Specification](https://reference.aspose.cloud/cells/#/TextProcessingController/RemoveDuplicateSubstringsInRemoteSpreadsheet) defines a publicly accessible programming interface and lets you carry out REST interactions directly from a web browser.

[[Back to API list]](../DeveloperGuide.md#api-reference)  
[[Back to README]](../../README.md)