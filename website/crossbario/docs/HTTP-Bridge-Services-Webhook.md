## Introduction

> The *HTTP Webhook* feature is available starting with Crossbar **0.11.0**.

The *HTTP Webhook Service* broadcasts incoming HTTP/POST requests on a fixed WAMP topic.

Webhooks are a method of "push notification" used by services such as GitHub and BitBucket to notify other services when events have happened through a simple HTTP POST.
The HTTP Webhook Service allows you to consume these events (providing it is accessible by the external service) through a WAMP PubSub channel (allowing potentially many things to occur from one webhook notification).


## Try it

Clone the [Crossbar.io examples repository](https://github.com/crossbario/crossbarexamples), and go to the `rest/webhooks` subdirectory.

Now start Crossbar:

```console
crossbar start
```

and open [http://localhost:8080](http://localhost:8080) in your browser.
Open the JavaScript console to see events received.

To submit an example webhook via HTTP/POST, you can use [curl](http://curl.haxx.se/):

```console
curl -H "Content-Type: text/plain" \
   -d 'fresh webhooks!' \
   http://127.0.0.1:8080/webhook
```


## With GitHub

If you set up Crossbar to have a Webhook service, and make it externally available, you can configure GitHub to send events to it.
Underneath Settings and "Services & Webhooks", you can add a new webhook, which just requires the URL of the externally-accessible Webhook service.
You can configure GitHub to send certain events, or all events.

When you have configured it, it will send a 'ping' for you to verify it.
As you have configured the Webhook service, you will recieve a message similar to this (most of the body cut out for brevity) on the WAMP topic it was configured with.


```json
{
    "body": "{\"zen\":\"Design for failure.\",[...more json...]}",
    "headers": {
        "Content-Length": [
            "6188"
        ],
        "X-Github-Event": [
            "ping"
        ],
        "X-Github-Delivery": [
            "7e87c300-462c-11e5-8008-e7623fda32a6"
        ],
        "Accept": [
            "*/*"
        ],
        "User-Agent": [
            "GitHub-Hookshot/4963429"
        ],
        "Host": [
            "atleastfornow.net:8080"
        ],
        "Content-Type": [
            "application/json"
        ]
    }
}
```

The message on the WAMP topic will be a dict containing the body as a string, and the headers as a dictionary of lists.

You will also see the following in the logs:

```
2015-08-19T04:44:43+0000 [Router        490] Successfully sent webhook from 192.30.252.34 to com.myapp.topic1
```

For more information on Webhooks, please see GitHub's [Webhooks Guide](https://developer.github.com/webhooks/).
