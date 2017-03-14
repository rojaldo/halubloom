# swagger_client.SsidApi

All URIs are relative to *http://10.0.0.1:2015*

Method | HTTP request | Description
------------- | ------------- | -------------
[**modify_ssid**](SsidApi.md#modify_ssid) | **POST** /master/ssid | Changes the Access Point settings of your master lamp.


# **modify_ssid**
> modify_ssid(body=body)

Changes the Access Point settings of your master lamp.



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SsidApi()
body = swagger_client.Ssid() # Ssid | Changes the Access Point settings of your master lamp (optional)

try: 
    # Changes the Access Point settings of your master lamp.
    api_instance.modify_ssid(body=body)
except ApiException as e:
    print("Exception when calling SsidApi->modify_ssid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Ssid**](Ssid.md)| Changes the Access Point settings of your master lamp | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

