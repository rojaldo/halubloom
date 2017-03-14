# swagger_client.GroupApi

All URIs are relative to *http://10.0.0.1:2015*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_group**](GroupApi.md#add_group) | **POST** /master/group | Adds a new group.
[**delete_group**](GroupApi.md#delete_group) | **DELETE** /master/group/{id} | Deletes a group
[**get_group**](GroupApi.md#get_group) | **GET** /master/group/{id} | Gets information groups from its id
[**get_groups**](GroupApi.md#get_groups) | **GET** /master/group | Gets all the groups information
[**modify_group**](GroupApi.md#modify_group) | **PUT** /master/group | Modifies an existing group.
[**turn_off_group**](GroupApi.md#turn_off_group) | **POST** /group/{id}/turnOff | Plays turnOff on a group
[**turn_on_group**](GroupApi.md#turn_on_group) | **POST** /group/{id}/turnOn | Plays turnOn on a group


# **add_group**
> AddResponse add_group(body=body)

Adds a new group.



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupApi()
body = swagger_client.Group() # Group | group object that needs to be added (optional)

try: 
    # Adds a new group.
    api_response = api_instance.add_group(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->add_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Group**](Group.md)| group object that needs to be added | [optional] 

### Return type

[**AddResponse**](AddResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> delete_group(id)

Deletes a group



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupApi()
id = 56 # int | ID of group to delete

try: 
    # Deletes a group
    api_instance.delete_group(id)
except ApiException as e:
    print("Exception when calling GroupApi->delete_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of group to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group**
> Group get_group(id)

Gets information groups from its id

Gets groups properties

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupApi()
id = 56 # int | ID of groups which information we want

try: 
    # Gets information groups from its id
    api_response = api_instance.get_group(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of groups which information we want | 

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups**
> GroupResponse get_groups()

Gets all the groups information

Gets groups properties

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupApi()

try: 
    # Gets all the groups information
    api_response = api_instance.get_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GroupResponse**](GroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_group**
> modify_group(body=body)

Modifies an existing group.



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupApi()
body = swagger_client.Group() # Group | Group object that needs to be modified (optional)

try: 
    # Modifies an existing group.
    api_instance.modify_group(body=body)
except ApiException as e:
    print("Exception when calling GroupApi->modify_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Group**](Group.md)| Group object that needs to be modified | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **turn_off_group**
> turn_off_group(id)

Plays turnOff on a group



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupApi()
id = 56 # int | TurnOff plays

try: 
    # Plays turnOff on a group
    api_instance.turn_off_group(id)
except ApiException as e:
    print("Exception when calling GroupApi->turn_off_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| TurnOff plays | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **turn_on_group**
> turn_on_group(id)

Plays turnOn on a group



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GroupApi()
id = 56 # int | TurnOn plays

try: 
    # Plays turnOn on a group
    api_instance.turn_on_group(id)
except ApiException as e:
    print("Exception when calling GroupApi->turn_on_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| TurnOn plays | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

