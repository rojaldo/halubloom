# swagger_client.DiscoveryApi

All URIs are relative to *http://10.0.0.1:2015*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_discovery**](DiscoveryApi.md#get_discovery) | **GET** /master/discovery | Gets all the Discovery information
[**modify_discovery**](DiscoveryApi.md#modify_discovery) | **POST** /master/discovery | Discovery


# **get_discovery**
> list[Discovery] get_discovery()

Gets all the Discovery information

Gets Discovery properties

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiscoveryApi()

try: 
    # Gets all the Discovery information
    api_response = api_instance.get_discovery()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiscoveryApi->get_discovery: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Discovery]**](Discovery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_discovery**
> modify_discovery()

Discovery



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiscoveryApi()

try: 
    # Discovery
    api_instance.modify_discovery()
except ApiException as e:
    print("Exception when calling DiscoveryApi->modify_discovery: %s\n" % e)
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

