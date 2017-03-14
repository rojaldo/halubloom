# swagger_client.LampApi

All URIs are relative to *http://10.0.0.1:2015*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_lamp**](LampApi.md#delete_lamp) | **DELETE** /master/lamp/{id} | Removes a lamp from the network database.
[**get_lamp**](LampApi.md#get_lamp) | **GET** /master/lamp/{id} | Gets information lamp from its id
[**get_lamps**](LampApi.md#get_lamps) | **GET** /master/lamp | Gets all the lamps information
[**modify_color**](LampApi.md#modify_color) | **POST** /lamp/{id}/color | Plays color
[**turn_off**](LampApi.md#turn_off) | **POST** /lamp/{id}/turnOff | Plays turnOff
[**turn_on**](LampApi.md#turn_on) | **POST** /lamp/{id}/turnOn | Plays turnOn


# **delete_lamp**
> delete_lamp(id)

Removes a lamp from the network database.



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LampApi()
id = 56 # int | ID of lamp to delete

try: 
    # Removes a lamp from the network database.
    api_instance.delete_lamp(id)
except ApiException as e:
    print("Exception when calling LampApi->delete_lamp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of lamp to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lamp**
> Lamp get_lamp(id)

Gets information lamp from its id

Gets lamp properties

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LampApi()
id = 56 # int | ID of lamp which information we want

try: 
    # Gets information lamp from its id
    api_response = api_instance.get_lamp(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LampApi->get_lamp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of lamp which information we want | 

### Return type

[**Lamp**](Lamp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lamps**
> LampResponse get_lamps()

Gets all the lamps information

Gets lamps properties

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LampApi()

try: 
    # Gets all the lamps information
    api_response = api_instance.get_lamps()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LampApi->get_lamps: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LampResponse**](LampResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_color**
> modify_color(id, body=body)

Plays color



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LampApi()
id = 56 # int | color plays
body = swagger_client.Color() # Color | Adds a new color to the database (optional)

try: 
    # Plays color
    api_instance.modify_color(id, body=body)
except ApiException as e:
    print("Exception when calling LampApi->modify_color: %s\n" % e)
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

# **turn_off**
> turn_off(id)

Plays turnOff



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LampApi()
id = 56 # int | TurnOn plays

try: 
    # Plays turnOff
    api_instance.turn_off(id)
except ApiException as e:
    print("Exception when calling LampApi->turn_off: %s\n" % e)
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

# **turn_on**
> turn_on(id)

Plays turnOn



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LampApi()
id = 56 # int | TurnOn plays

try: 
    # Plays turnOn
    api_instance.turn_on(id)
except ApiException as e:
    print("Exception when calling LampApi->turn_on: %s\n" % e)
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

