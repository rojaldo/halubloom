# swagger_client.OtaFileApi

All URIs are relative to *http://10.0.0.1:2015*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adds_ota_file**](OtaFileApi.md#adds_ota_file) | **POST** /master/otaFile | Installs the new upgrade. Once the lamp receives this message, it will install the Upgrade and then reboot.
[**modify_ota_file**](OtaFileApi.md#modify_ota_file) | **PUT** /master/otaFile | Starts the download of the OTA image.


# **adds_ota_file**
> adds_ota_file(body=body)

Installs the new upgrade. Once the lamp receives this message, it will install the Upgrade and then reboot.



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OtaFileApi()
body = swagger_client.OtaFile() # OtaFile | Adds a new otaFile to the database (optional)

try: 
    # Installs the new upgrade. Once the lamp receives this message, it will install the Upgrade and then reboot.
    api_instance.adds_ota_file(body=body)
except ApiException as e:
    print("Exception when calling OtaFileApi->adds_ota_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OtaFile**](OtaFile.md)| Adds a new otaFile to the database | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_ota_file**
> modify_ota_file()

Starts the download of the OTA image.



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OtaFileApi()

try: 
    # Starts the download of the OTA image.
    api_instance.modify_ota_file()
except ApiException as e:
    print("Exception when calling OtaFileApi->modify_ota_file: %s\n" % e)
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

