##Requests and Responses¶
Scrapy uses Request and Response objects for crawling web sites.

Typically, Request objects are generated in the spiders and pass across the system until they reach the Downloader, which executes the request and returns a Response object which travels back to the spider that issued the request.

Both Request and Response classes have subclasses which add functionality not required in the base classes. These are described below in Request subclasses and Response subclasses.

Request objects¶
classscrapy.http.Request(*args, **kwargs)[source]¶
A Request object represents an HTTP request, which is usually generated in the Spider and executed by the Downloader, and thus generating a Response.

Parameters
url (str) –

the URL of this request

If the URL is invalid, a ValueError exception is raised.

callback (collections.abc.Callable) – the function that will be called with the response of this request (once it’s downloaded) as its first parameter. For more information see Passing additional data to callback functions below. If a Request doesn’t specify a callback, the spider’s parse() method will be used. Note that if exceptions are raised during processing, errback is called instead.

method (str) – the HTTP method of this request. Defaults to 'GET'.

meta (dict) – the initial values for the Request.meta attribute. If given, the dict passed in this parameter will be shallow copied.

body (bytes or str) – the request body. If a string is passed, then it’s encoded as bytes using the encoding passed (which defaults to utf-8). If body is not given, an empty bytes object is stored. Regardless of the type of this argument, the final value stored will be a bytes object (never a string or None).

headers (dict) –

the headers of this request. The dict values can be strings (for single valued headers) or lists (for multi-valued headers). If None is passed as value, the HTTP header will not be sent at all.

Caution

Cookies set via the Cookie header are not considered by the CookiesMiddleware. If you need to set cookies for a request, use the Request.cookies parameter. This is a known current limitation that is being worked on.

cookies (dict or list) –

the request cookies. These can be sent in two forms.

Using a dict:

request_with_cookies = Request(url="http://www.example.com",
                               cookies={'currency': 'USD', 'country': 'UY'})
Using a list of dicts:

request_with_cookies = Request(url="http://www.example.com",
                               cookies=[{'name': 'currency',
                                        'value': 'USD',
                                        'domain': 'example.com',
                                        'path': '/currency'}])
The latter form allows for customizing the domain and path attributes of the cookie. This is only useful if the cookies are saved for later requests.

When some site returns cookies (in a response) those are stored in the cookies for that domain and will be sent again in future requests. That’s the typical behaviour of any regular web browser.

To create a request that does not send stored cookies and does not store received cookies, set the dont_merge_cookies key to True in request.meta.

Example of a request that sends manually-defined cookies and ignores cookie storage:

Request(
    url="http://www.example.com",
    cookies={'currency': 'USD', 'country': 'UY'},
    meta={'dont_merge_cookies': True},
)
For more info see CookiesMiddleware.

Caution

Cookies set via the Cookie header are not considered by the CookiesMiddleware. If you need to set cookies for a request, use the Request.cookies parameter. This is a known current limitation that is being worked on.

encoding (str) – the encoding of this request (defaults to 'utf-8'). This encoding will be used to percent-encode the URL and to convert the body to bytes (if given as a string).

priority (int) – the priority of this request (defaults to 0). The priority is used by the scheduler to define the order used to process requests. Requests with a higher priority value will execute earlier. Negative values are allowed in order to indicate relatively low-priority.

dont_filter (bool) – indicates that this request should not be filtered by the scheduler. This is used when you want to perform an identical request multiple times, to ignore the duplicates filter. Use it with care, or you will get into crawling loops. Default to False.

errback (collections.abc.Callable) –

a function that will be called if any exception was raised while processing the request. This includes pages that failed with 404 HTTP errors and such. It receives a Failure as first parameter. For more information, see Using errbacks to catch exceptions in request processing below.

Changed in version 2.0: The callback parameter is no longer required when the errback parameter is specified.

flags (list) – Flags sent to the request, can be used for logging or similar purposes.

cb_kwargs (dict) – A dict with arbitrary data that will be passed as keyword arguments to the Request’s callback.