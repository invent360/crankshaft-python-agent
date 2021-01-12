# openapi_client.PostsApi

All URIs are relative to *http://jsonplaceholder.typicode.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_posts**](PostsApi.md#create_posts) | **POST** /posts | Create a post
[**fetch_posts**](PostsApi.md#fetch_posts) | **GET** /posts | List all posts
[**get_post_by_id**](PostsApi.md#get_post_by_id) | **GET** /posts/{id} | Info for a specific post


# **create_posts**
> create_posts()

Create a post

### Example

```python
import time
import openapi_client
from openapi_client.api import posts_api
from openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://jsonplaceholder.typicode.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://jsonplaceholder.typicode.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = posts_api.PostsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Create a post
        api_instance.create_posts()
    except openapi_client.ApiException as e:
        print("Exception when calling PostsApi->create_posts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Null response |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_posts**
> Posts fetch_posts()

List all posts

### Example

```python
import time
import openapi_client
from openapi_client.api import posts_api
from openapi_client.model.posts import Posts
from openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://jsonplaceholder.typicode.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://jsonplaceholder.typicode.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = posts_api.PostsApi(api_client)
    limit = 1 # int | How many items to return at one time (max 100) (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all posts
        api_response = api_instance.fetch_posts(limit=limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PostsApi->fetch_posts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many items to return at one time (max 100) | [optional]

### Return type

[**Posts**](Posts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paged array of posts |  * x-next - A link to the next page of responses <br>  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_post_by_id**
> Post get_post_by_id(id)

Info for a specific post

### Example

```python
import time
import openapi_client
from openapi_client.api import posts_api
from openapi_client.model.error import Error
from openapi_client.model.post import Post
from pprint import pprint
# Defining the host is optional and defaults to http://jsonplaceholder.typicode.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://jsonplaceholder.typicode.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = posts_api.PostsApi(api_client)
    id = "id_example" # str | The id of the post to retrieve

    # example passing only required values which don't have defaults set
    try:
        # Info for a specific post
        api_response = api_instance.get_post_by_id(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PostsApi->get_post_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the post to retrieve |

### Return type

[**Post**](Post.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Expected response to a valid request |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

