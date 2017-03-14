# swagger_client.WizardApi

All URIs are relative to *http://10.0.0.1:2015*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_wizard**](WizardApi.md#get_wizard) | **GET** /master/wizard | Gets all the wizard information
[**modifywizard**](WizardApi.md#modifywizard) | **POST** /master/wizard | Starts the wizard


# **get_wizard**
> WizardResponse get_wizard()

Gets all the wizard information

Gets wizard properties

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WizardApi()

try: 
    # Gets all the wizard information
    api_response = api_instance.get_wizard()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WizardApi->get_wizard: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WizardResponse**](WizardResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modifywizard**
> modifywizard(body=body)

Starts the wizard



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WizardApi()
body = swagger_client.Wizard() # Wizard | Starts the wizard (optional)

try: 
    # Starts the wizard
    api_instance.modifywizard(body=body)
except ApiException as e:
    print("Exception when calling WizardApi->modifywizard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Wizard**](Wizard.md)| Starts the wizard | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

