# swagger_client.ActionApi

All URIs are relative to *http://10.0.0.1:2015*

Method | HTTP request | Description
------------- | ------------- | -------------
[**modify_effect**](ActionApi.md#modify_effect) | **PUT** /master/action | Stop effect
[**use_ambiance**](ActionApi.md#use_ambiance) | **POST** /master/action | Use Ambiance.


# **modify_effect**
> modify_effect(body=body)

Stop effect



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActionApi()
body = swagger_client.Effect() # Effect | Effect stop (optional)

try: 
    # Stop effect
    api_instance.modify_effect(body=body)
except ApiException as e:
    print("Exception when calling ActionApi->modify_effect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Effect**](Effect.md)| Effect stop | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **use_ambiance**
> ActionResponse use_ambiance(body)

Use Ambiance.



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActionApi()
body = swagger_client.AmbianceId() # AmbianceId | Ambiance id to use

try: 
    # Use Ambiance.
    api_response = api_instance.use_ambiance(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionApi->use_ambiance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AmbianceId**](AmbianceId.md)| Ambiance id to use | 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

