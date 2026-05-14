# **Spreadsheet Cloud API: removeCharactersByPositionInRemoteSpreadsheet**

Deletes characters from every cell in the target range by position (first/last N, before/after a substring, or between two delimiters) while preserving formulas, formatting and data-validation. 


## **Quick Start**

- **Base URL**: `http://api.aspose.cloud/v4.0`
- **Authentication Method**: `JWT (OAuth2, application)`  **Token URL**: `https://api.aspose.cloud/connect/token`
## **Interface Details**

### **Endpoint** 

```
PUT http://api.aspose.cloud/v4.0/cells/{name}/worksheets/{worksheet}/range/{range}/content/remove/characters-by-position
```
### **Function Description**
**Position modes**  - `theFirstNCharacters` – remove N characters from the start  - `LastN` – remove N characters from the end  - `BeforeText` – delete everything before the first occurrence of the supplied substring  - `AfterText` – delete everything after the first occurrence  - `BetweenValues` – strip the substring (and optionally the delimiters themselves) between two user-defined values              **Options**  - `caseSensitive` – affects `BeforeText`, `AfterText` and `BetweenValues` searches  - `includingDelimiters` – when `BetweenValues` is used, controls whether the two boundary values are also removed               

### The request parameters of **removeCharactersByPositionInRemoteSpreadsheet** API are: 

| Parameter Name | Type | Path/Query String/HTTPBody | Description | 
| :- | :- | :- |:- | 
|name|String|Path|(Required) The name of the workbook file to be retrieved.|
|worksheet|String|Path|Specify the worksheet of spreadsheet.|
|range|String|Path|Specify the worksheet range of spreadsheet.|
|theFirstNCharacters|Integer|Query||
|theLastNCharacters|Integer|Query||
|allCharactersBeforeText|String|Query||
|allCharactersAfterText|String|Query||
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

The [OpenAPI Specification](https://reference.aspose.cloud/cells/#/TextProcessingController/RemoveCharactersByPositionInRemoteSpreadsheet) defines a publicly accessible programming interface and lets you carry out REST interactions directly from a web browser.

[[Back to API list]](../DeveloperGuide.md#api-reference)  
[[Back to README]](../../README.md)