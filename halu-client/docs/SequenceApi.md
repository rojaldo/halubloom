# swagger_client.SequenceApi

All URIs are relative to *http://10.0.0.1:2015*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_sequence**](SequenceApi.md#add_sequence) | **POST** /master/sequence | Adds a new sequence.
[**delete_sequence**](SequenceApi.md#delete_sequence) | **DELETE** /master/sequence/{id} | Deletes a sequence
[**get_sequence**](SequenceApi.md#get_sequence) | **GET** /master/sequence/{id} | Gets information sequence from its id
[**get_sequences**](SequenceApi.md#get_sequences) | **GET** /master/sequence | Gets all the sequences information
[**modify_sequence**](SequenceApi.md#modify_sequence) | **PUT** /master/sequence | Modifies an existing sequence.


# **add_sequence**
> AddResponse add_sequence(body=body)

Adds a new sequence.



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SequenceApi()
body = swagger_client.Sequence() # Sequence | sequence object that needs to be added (optional)

try: 
    # Adds a new sequence.
    api_response = api_instance.add_sequence(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SequenceApi->add_sequence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Sequence**](Sequence.md)| sequence object that needs to be added | [optional] 

### Return type

[**AddResponse**](AddResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sequence**
> delete_sequence(id)

Deletes a sequence



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SequenceApi()
id = 56 # int | ID of sequence to delete

try: 
    # Deletes a sequence
    api_instance.delete_sequence(id)
except ApiException as e:
    print("Exception when calling SequenceApi->delete_sequence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of sequence to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sequence**
> Sequence get_sequence(id)

Gets information sequence from its id

Gets sequence properties

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SequenceApi()
id = 56 # int | ID of sequence which information we want

try: 
    # Gets information sequence from its id
    api_response = api_instance.get_sequence(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SequenceApi->get_sequence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of sequence which information we want | 

### Return type

[**Sequence**](Sequence.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sequences**
> SequenceResponse get_sequences()

Gets all the sequences information

Gets sequences properties

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SequenceApi()

try: 
    # Gets all the sequences information
    api_response = api_instance.get_sequences()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SequenceApi->get_sequences: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SequenceResponse**](SequenceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_sequence**
> modify_sequence(body=body)

Modifies an existing sequence.



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SequenceApi()
body = swagger_client.Sequence() # Sequence | Sequence object that needs to be modified (optional)

try: 
    # Modifies an existing sequence.
    api_instance.modify_sequence(body=body)
except ApiException as e:
    print("Exception when calling SequenceApi->modify_sequence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Sequence**](Sequence.md)| Sequence object that needs to be modified | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

