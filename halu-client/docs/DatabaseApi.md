# swagger_client.DatabaseApi

All URIs are relative to *http://10.0.0.1:2015*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_database**](DatabaseApi.md#get_database) | **GET** /master/database | The database is where the master lamp saves all the data.


# **get_database**
> DatabaseResponse get_database()

The database is where the master lamp saves all the data.



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DatabaseApi()

try: 
    # The database is where the master lamp saves all the data.
    api_response = api_instance.get_database()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatabaseApi->get_database: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DatabaseResponse**](DatabaseResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

