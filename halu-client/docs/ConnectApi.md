# swagger_client.ConnectApi

All URIs are relative to *http://10.0.0.1:2015*

Method | HTTP request | Description
------------- | ------------- | -------------
[**modify_connect**](ConnectApi.md#modify_connect) | **POST** /master/connect | Connects you to a WiFi connection. The lamp will deduce which encryption to use automagically.


# **modify_connect**
> modify_connect(body=body)

Connects you to a WiFi connection. The lamp will deduce which encryption to use automagically.



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectApi()
body = swagger_client.Connect() # Connect | Starts the Connect (optional)

try: 
    # Connects you to a WiFi connection. The lamp will deduce which encryption to use automagically.
    api_instance.modify_connect(body=body)
except ApiException as e:
    print("Exception when calling ConnectApi->modify_connect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Connect**](Connect.md)| Starts the Connect | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

