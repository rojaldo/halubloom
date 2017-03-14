# swagger_client.SpaceApi

All URIs are relative to *http://10.0.0.1:2015*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_space**](SpaceApi.md#add_space) | **POST** /master/space | Adds  a new Space.
[**delete_space**](SpaceApi.md#delete_space) | **DELETE** /master/space/{id} | Deletes a space
[**get_space**](SpaceApi.md#get_space) | **GET** /master/space | Gets all the spaces information
[**get_space_id**](SpaceApi.md#get_space_id) | **GET** /master/space/{id} | Gets information space from its id
[**modify_color_space**](SpaceApi.md#modify_color_space) | **POST** /space/{id}/color | Plays color
[**modify_space**](SpaceApi.md#modify_space) | **PUT** /master/space | Modifies an existing space.
[**turn_off_space**](SpaceApi.md#turn_off_space) | **POST** /space/{id}/turnOff | Plays turnOff
[**turn_on_space**](SpaceApi.md#turn_on_space) | **POST** /space/{id}/turnOn | Plays turnOn


# **add_space**
> AddResponse add_space(body=body)

Adds  a new Space.



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpaceApi()
body = swagger_client.Space() # Space | Space object that needs to be added (optional)

try: 
    # Adds  a new Space.
    api_response = api_instance.add_space(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->add_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Space**](Space.md)| Space object that needs to be added | [optional] 

### Return type

[**AddResponse**](AddResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_space**
> delete_space(id)

Deletes a space



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpaceApi()
id = 56 # int | ID of space to delete

try: 
    # Deletes a space
    api_instance.delete_space(id)
except ApiException as e:
    print("Exception when calling SpaceApi->delete_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of space to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_space**
> list[Space] get_space()

Gets all the spaces information

Gets spaces properties

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpaceApi()

try: 
    # Gets all the spaces information
    api_response = api_instance.get_space()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->get_space: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Space]**](Space.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_space_id**
> Space get_space_id(id)

Gets information space from its id

Gets space properties

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpaceApi()
id = 56 # int | ID of space which information we want

try: 
    # Gets information space from its id
    api_response = api_instance.get_space_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpaceApi->get_space_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of space which information we want | 

### Return type

[**Space**](Space.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_color_space**
> modify_color_space(id, body=body)

Plays color



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpaceApi()
id = 56 # int | color plays
body = swagger_client.Color() # Color | Adds a new color to the database (optional)

try: 
    # Plays color
    api_instance.modify_color_space(id, body=body)
except ApiException as e:
    print("Exception when calling SpaceApi->modify_color_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| color plays | 
 **body** | [**Color**](Color.md)| Adds a new color to the database | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_space**
> modify_space(body=body)

Modifies an existing space.



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpaceApi()
body = swagger_client.SpaceResponse() # SpaceResponse | Space object that needs to be modified (optional)

try: 
    # Modifies an existing space.
    api_instance.modify_space(body=body)
except ApiException as e:
    print("Exception when calling SpaceApi->modify_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpaceResponse**](SpaceResponse.md)| Space object that needs to be modified | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **turn_off_space**
> turn_off_space(id)

Plays turnOff



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpaceApi()
id = 56 # int | TurnOn plays

try: 
    # Plays turnOff
    api_instance.turn_off_space(id)
except ApiException as e:
    print("Exception when calling SpaceApi->turn_off_space: %s\n" % e)
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

# **turn_on_space**
> turn_on_space(id)

Plays turnOn



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpaceApi()
id = 56 # int | TurnOn plays

try: 
    # Plays turnOn
    api_instance.turn_on_space(id)
except ApiException as e:
    print("Exception when calling SpaceApi->turn_on_space: %s\n" % e)
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

