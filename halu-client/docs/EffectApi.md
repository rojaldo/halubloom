# swagger_client.EffectApi

All URIs are relative to *http://10.0.0.1:2015*

Method | HTTP request | Description
------------- | ------------- | -------------
[**play_effect**](EffectApi.md#play_effect) | **POST** /master/effect | Adds a new Effect to the database
[**stop_effect**](EffectApi.md#stop_effect) | **DELETE** /master/effect | Stops an effect


# **play_effect**
> play_effect(body=body)

Adds a new Effect to the database



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EffectApi()
body = swagger_client.Effect() # Effect | Adds and play a new Effect to the database (optional)

try: 
    # Adds a new Effect to the database
    api_instance.play_effect(body=body)
except ApiException as e:
    print("Exception when calling EffectApi->play_effect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Effect**](Effect.md)| Adds and play a new Effect to the database | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_effect**
> stop_effect(id)

Stops an effect



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EffectApi()
id = 56 # int | Effect ID to stop

try: 
    # Stops an effect
    api_instance.stop_effect(id)
except ApiException as e:
    print("Exception when calling EffectApi->stop_effect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Effect ID to stop | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

