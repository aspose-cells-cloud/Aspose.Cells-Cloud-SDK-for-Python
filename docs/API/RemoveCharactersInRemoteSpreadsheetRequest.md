# **Spreadsheet Cloud API: removeCharactersInRemoteSpreadsheet**

Deletes user-defined characters, predefined symbol sets, or any substring from every cell in the chosen range while preserving formulas, formatting and data-validation for a remote spreadsheet. 


## **Quick Start**

- **Base URL**: `http://api.aspose.cloud/v4.0`
- **Authentication Method**: `JWT (OAuth2, application)`  **Token URL**: `https://api.aspose.cloud/connect/token`
## **Interface Details**

### **Endpoint** 

```
PUT http://api.aspose.cloud/v4.0/cells/{name}/worksheets/{worksheet}/range/{range}/content/remove/characters
```
### **Function Description**
RemoveCustomText performs precise, position-based or pattern-based deletion inside the supplied range while preserving formulas, formatting and data-validation.            **Removal modes**  - `CustomChars` – delete each character supplied in `customCharacters` (case-insensitive by default)  - `CharacterSet` – pick a built-in set:    - `NonPrinting` – ASCII 0-31 + 127,129,141,143,144,157 (line-breaks, etc.)    - `Text` – all letters A-Z / a-z    - `Numeric` – all digits 0-9    - `Symbols` – math, geometric, technical, currency, letter-like symbols (?, ™, 1, …)    - `Punctuation` – any punctuation mark  - `Substring` – remove the entire substring specified in `substring` (case-sensitive option available)              **Options**  - `caseSensitive` – affects `Substring` mode and `CustomChars` when enabled  - Empty result is allowed; if every character is removed the cell becomes blank(empty string). - Numbers, booleans, errors are skipped; only string-type cell values are touched.

### The request parameters of **removeCharactersInRemoteSpreadsheet** API are: 

| Parameter Name | Type | Path/Query String/HTTPBody | Description | 
| :- | :- | :- |:- | 
|name|String|Path|(Required) The name of the workbook file to be retrieved.|
|worksheet|String|Path|Specify the worksheet of spreadsheet.|
|range|String|Path|Specify the worksheet range of spreadsheet.|
|removeTextMethod|String|Query|Specify the removal of text method type.|
|characterSets|String|Query|Specify the character sets.|
|removeCustomValue|String|Query|Specify the remove custom value.|
|caseSensitive|Boolean|Query|Affects `Substring` mode and `CustomChars` when enabled.|
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

The [OpenAPI Specification](https://reference.aspose.cloud/cells/#/TextProcessingController/RemoveCharactersInRemoteSpreadsheet) defines a publicly accessible programming interface and lets you carry out REST interactions directly from a web browser.

[[Back to API list]](../DeveloperGuide.md#api-reference)  
[[Back to README]](../../README.md)