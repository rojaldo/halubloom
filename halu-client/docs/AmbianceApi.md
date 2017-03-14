# swagger_client.AmbianceApi

All URIs are relative to *http://10.0.0.1:2015*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_ambiance**](AmbianceApi.md#add_ambiance) | **POST** /master/ambiance | Adds a new Ambiance.
[**delete_ambiance**](AmbianceApi.md#delete_ambiance) | **DELETE** /master/ambiance/{id} | Removes a Ambiance from the database.
[**get_ambiance**](AmbianceApi.md#get_ambiance) | **GET** /master/ambiance/{id} | Gets information ambiance from its id
[**get_ambiances**](AmbianceApi.md#get_ambiances) | **GET** /master/ambiance | Gets all the ambiances information
[**modify_ambiance**](AmbianceApi.md#modify_ambiance) | **PUT** /master/ambiance/{id} | Modifies an existing Ambiance.


# **add_ambiance**
> AmbianceResponse add_ambiance(body=body)

Adds a new Ambiance.



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AmbianceApi()
body = swagger_client.Ambiance() # Ambiance | Ambiance object that needs to be added (optional)

try: 
    # Adds a new Ambiance.
    api_response = api_instance.add_ambiance(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmbianceApi->add_ambiance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Ambiance**](Ambiance.md)| Ambiance object that needs to be added | [optional] 

### Return type

[**AmbianceResponse**](AmbianceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ambiance**
> delete_ambiance(id)

Removes a Ambiance from the database.



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AmbianceApi()
id = 56 # int | ID of ambiance to delete

try: 
    # Removes a Ambiance from the database.
    api_instance.delete_ambiance(id)
except ApiException as e:
    print("Exception when calling AmbianceApi->delete_ambiance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of ambiance to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ambiance**
> Ambiance get_ambiance(id)

Gets information ambiance from its id

Gets ambiance properties

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AmbianceApi()
id = 56 # int | ID of ambiance which information we want

try: 
    # Gets information ambiance from its id
    api_response = api_instance.get_ambiance(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmbianceApi->get_ambiance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of ambiance which information we want | 

### Return type

[**Ambiance**](Ambiance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ambiances**
> AmbianceResponse get_ambiances()

Gets all the ambiances information

Gets ambiances properties

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AmbianceApi()

try: 
    # Gets all the ambiances information
    api_response = api_instance.get_ambiances()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmbianceApi->get_ambiances: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AmbianceResponse**](AmbianceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_ambiance**
> modify_ambiance(id, body=body)

Modifies an existing Ambiance.



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AmbianceApi()
id = 56 # int | ID of ambiance to delete
body = swagger_client.Ambiance() # Ambiance | Ambiance object that needs to be modified (optional)

try: 
    # Modifies an existing Ambiance.
    api_instance.modify_ambiance(id, body=body)
except ApiException as e:
    print("Exception when calling AmbianceApi->modify_ambiance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of ambiance to delete | 
 **body** | [**Ambiance**](Ambiance.md)| Ambiance object that needs to be modified | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

