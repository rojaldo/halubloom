# swagger_client.NotificationApi

All URIs are relative to *http://10.0.0.1:2015*

Method | HTTP request | Description
------------- | ------------- | -------------
[**modify_notification**](NotificationApi.md#modify_notification) | **PUT** /master/notification | requests a notification message to master lamp


# **modify_notification**
> modify_notification()

requests a notification message to master lamp



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationApi()

try: 
    # requests a notification message to master lamp
    api_instance.modify_notification()
except ApiException as e:
    print("Exception when calling NotificationApi->modify_notification: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

