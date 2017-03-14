# swagger_client.ScheduledApi

All URIs are relative to *http://10.0.0.1:2015*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_scheduled**](ScheduledApi.md#add_scheduled) | **POST** /master/scheduled | Adds  a new Scheduled.
[**delete_scheduled**](ScheduledApi.md#delete_scheduled) | **DELETE** /master/Scheduled/{id} | Deletes a scheduled
[**get_scheduled**](ScheduledApi.md#get_scheduled) | **GET** /master/Scheduled/{id} | Gets information scheduled from its id
[**get_scheduleds**](ScheduledApi.md#get_scheduleds) | **GET** /master/scheduled | Gets all the scheduled information
[**modify_scheduled**](ScheduledApi.md#modify_scheduled) | **PUT** /master/scheduled | Modifies an existing scheduled.


# **add_scheduled**
> AddResponse add_scheduled(body=body)

Adds  a new Scheduled.



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScheduledApi()
body = swagger_client.Scheduled() # Scheduled | Scheduled object that needs to be added (optional)

try: 
    # Adds  a new Scheduled.
    api_response = api_instance.add_scheduled(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledApi->add_scheduled: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Scheduled**](Scheduled.md)| Scheduled object that needs to be added | [optional] 

### Return type

[**AddResponse**](AddResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scheduled**
> delete_scheduled(id)

Deletes a scheduled



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScheduledApi()
id = 56 # int | ID of scheduled to delete

try: 
    # Deletes a scheduled
    api_instance.delete_scheduled(id)
except ApiException as e:
    print("Exception when calling ScheduledApi->delete_scheduled: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of scheduled to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scheduled**
> Scheduled get_scheduled(id)

Gets information scheduled from its id

Gets scheduled properties

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScheduledApi()
id = 56 # int | ID of groups which information we want

try: 
    # Gets information scheduled from its id
    api_response = api_instance.get_scheduled(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledApi->get_scheduled: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of groups which information we want | 

### Return type

[**Scheduled**](Scheduled.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scheduleds**
> ScheduledResponse get_scheduleds()

Gets all the scheduled information

Gets scheduleds properties

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScheduledApi()

try: 
    # Gets all the scheduled information
    api_response = api_instance.get_scheduleds()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledApi->get_scheduleds: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ScheduledResponse**](ScheduledResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_scheduled**
> modify_scheduled(body=body)

Modifies an existing scheduled.



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScheduledApi()
body = swagger_client.Scheduled() # Scheduled | Scheduled object that needs to be modified (optional)

try: 
    # Modifies an existing scheduled.
    api_instance.modify_scheduled(body=body)
except ApiException as e:
    print("Exception when calling ScheduledApi->modify_scheduled: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Scheduled**](Scheduled.md)| Scheduled object that needs to be modified | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

