# swagger_client.BroadcastApi

All URIs are relative to *http://10.0.0.1:2015*

Method | HTTP request | Description
------------- | ------------- | -------------
[**modify_color_broadcast**](BroadcastApi.md#modify_color_broadcast) | **POST** /broadcast/color | Plays color
[**turn_off_broadcast**](BroadcastApi.md#turn_off_broadcast) | **POST** /broadcast/turnOff | Plays turnOff
[**turn_on_broadcast**](BroadcastApi.md#turn_on_broadcast) | **POST** /broadcast/turnOn | Plays turnOn


# **modify_color_broadcast**
> modify_color_broadcast(body=body)

Plays color



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BroadcastApi()
body = swagger_client.Color() # Color | color plays (optional)

try: 
    # Plays color
    api_instance.modify_color_broadcast(body=body)
except ApiException as e:
    print("Exception when calling BroadcastApi->modify_color_broadcast: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Color**](Color.md)| color plays | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **turn_off_broadcast**
> turn_off_broadcast()

Plays turnOff



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BroadcastApi()

try: 
    # Plays turnOff
    api_instance.turn_off_broadcast()
except ApiException as e:
    print("Exception when calling BroadcastApi->turn_off_broadcast: %s\n" % e)
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

# **turn_on_broadcast**
> turn_on_broadcast()

Plays turnOn



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BroadcastApi()

try: 
    # Plays turnOn
    api_instance.turn_on_broadcast()
except ApiException as e:
    print("Exception when calling BroadcastApi->turn_on_broadcast: %s\n" % e)
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

