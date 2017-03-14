# swagger_client.OtaStatusApi

All URIs are relative to *http://10.0.0.1:2015*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ota_status**](OtaStatusApi.md#get_ota_status) | **GET** /master/otaStatus | Retrieves the OTA Status from each lamp.
[**modify_ota_status**](OtaStatusApi.md#modify_ota_status) | **PUT** /master/otaStatus | Makes all the lamps try to connect to the OTA server to update their status.


# **get_ota_status**
> list[OtaStatus] get_ota_status()

Retrieves the OTA Status from each lamp.

Gets otaStatus properties from each lamp.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OtaStatusApi()

try: 
    # Retrieves the OTA Status from each lamp.
    api_response = api_instance.get_ota_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OtaStatusApi->get_ota_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[OtaStatus]**](OtaStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_ota_status**
> modify_ota_status()

Makes all the lamps try to connect to the OTA server to update their status.



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OtaStatusApi()

try: 
    # Makes all the lamps try to connect to the OTA server to update their status.
    api_instance.modify_ota_status()
except ApiException as e:
    print("Exception when calling OtaStatusApi->modify_ota_status: %s\n" % e)
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

