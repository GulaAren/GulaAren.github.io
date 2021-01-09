---
layout: post
title: Python ASGI Middleware
menutitle: Python ASGI Middleware
kategori:
  - python
  - starlette
  - fastapi
  - ASGI
label:
  - api
---


## Usage Introduction

On making custom Middleware, we use starlette middleware abstract class `BaseHTTPMiddleware`.
To implement a middleware class using BaseHTTPMiddleware, 
you must override the `async def dispatch(request, call_next)` method.

<!--more-->


#### Example

Overriding `async def dispatch(request, call_next)` method.

```python
class CustomHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers['Custom'] = 'Example'
        return response
```

Add more configuration options (*optional*)

```python
class CustomHeaderMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, header_value='Example'):
        super().__init__(app)
        self.header_value = header_value

    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers['Custom'] = 'Example'
        return response
```

Then we include the middleware to `Starlette` application instance.

```python
middleware = [
    Middleware(CustomHeaderMiddleware)
]

app = Starlette(routes=routes, middleware=middleware)
```

Then we include the middleware to `FastAPI` application instance.

```python

from fastapi import FastAPI

app = FastAPI()

app.add_middleware(CustomHeaderMiddleware, header_value='custom_header')
```

Another way to use middleware for `FastAPI`.

```python
import time

from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

```


#### Docs

 - [Starlette/middleware](https://www.starlette.io/middleware/)
