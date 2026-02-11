# **Spreadsheet Cloud API: decomposeUserTask**

AI task decomposition: Convert user objectives to sequential action plans with formatted file export. 


## **Quick Start**

- **Base URL**: `http://api.aspose.cloud/v4.0`
- **Authentication Method**: `JWT (OAuth2, application)`  **Token URL**: `https://api.aspose.cloud/connect/token`
## **Interface Details**

### **Endpoint** 

```
PUT http://api.aspose.cloud/v4.0/cells/ai/task/decompose
```
### **Function Description**
Decomposition Principles:Follows SMART criteria to ensure task qualityUses hour-based system for time allocation and estimationCompatible with Redmine format for task assignment structureAutomatically sets project milestone nodesInput Requirements: Only requires the task list to be decomposed and time estimates for each taskOutput Results: Generates standardized, structured task decomposition plans ready for direct import into project management tools

### The request parameters of **decomposeUserTask** API are: 

| Parameter Name | Type | Path/Query String/HTTPBody | Description | 
| :- | :- | :- |:- | 
|TaskDescription|String|Body|Decompose user task description.|
|region|String|Query|The spreadsheet region setting.|
|password|String|Query|The password for opening spreadsheet file.|

### **Response Description**
```json
{
File
}
```


## OpenAPI Specification

The [OpenAPI Specification](https://reference.aspose.cloud/cells/#/AIController/DecomposeUserTask) defines a publicly accessible programming interface and lets you carry out REST interactions directly from a web browser.

[[Back to API list]](../DeveloperGuide.md#api-reference)  
[[Back to README]](../../README.md)