#!/usr/bin/env python3
from werkzeug.wrappers import Request, Response


## similar to click, using a decator to wrap our code
## the application is where our app does stuff. 
## In the example, they printed the remote address and
## a webpage that displays text
@Request.application
def application(request):
    print(f"This web server is running at {request.remote_addr}")
    return Response('A WSGI generated this response!')


## in the main section, they run a simple server with
## with the following settings
if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple(
        hostname = "localhost",
        port = 5555,
        application=application
    )