# swagger_client.LampSettingsApi

All URIs are relative to *http://10.0.0.1:2015*

Method | HTTP request | Description
------------- | ------------- | -------------
[**modify_settings**](LampSettingsApi.md#modify_settings) | **POST** /lamp/{id}/settings | modifies lamp settings


# **modify_settings**
> modify_settings(id, body=body)

modifies lamp settings



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LampSettingsApi()
id = 56 # int | lamp id
body = swagger_client.LampSettings() # LampSettings | Lamp settings (optional)

try: 
    # modifies lamp settings
    api_instance.modify_settings(id, body=body)
except ApiException as e:
    print("Exception when calling LampSettingsApi->modify_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| lamp id | 
 **body** | [**LampSettings**](LampSettings.md)| Lamp settings | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

