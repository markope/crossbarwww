**Crossbar**.io has best-in-class compliance to the WebSocket protocol (RFC6455).

> Compliance is testified via the [**Autobahn**Testsuite](http://autobahn.ws/testsuite/), the [industry standard](http://autobahn.ws/testsuite/#users) WebSocket compliance testsuite which includes more than 500 automated test cases. **Crossbar**.io passed *all* tests - 100% strict. No matter what WebSocket server you use, we encourage you to run the testsuite against it and compare.

Protocol compliance is very important for two reasons:
* interoperability
* security

You don't want an evil client disturb or break your servers, or fail to serve clients because of interoperability issues.

**Check out the compliance reports for Crossbar.io [here](http://crossbar.io/download/reports/20140319/index.html).**

## Testing yourself

Install the testsuite:

```
pip install -U autobahntestsuite
```

Create a **Crossbar**.io node with a node configuration starting a WebSocket testee transport:

```json
{
   "workers": [
      {
         "type": "router",
         "transports": [
            {
               "type": "websocket.testee",
               "endpoint": {
                  "type": "tcp",
                  "port": 9001,
                  "backlog": 1024
               },
               "options": {
                  "compression": {
                     "deflate": {
                     }
                  }
               }
            }
         ]
      }
   ]
}
```

Now create a file `fuzzingclient.json`:

```json
{
   "servers": [
                  {
                     "agent": "Crossbar.io",
                     "url": "ws://127.0.0.1:9001"
                  }
               ],
   "cases": ["*"],
   "exclude-cases": [],
   "exclude-agent-cases": {}
}
```

This test specification defines which test cases to run against what servers.

Then, start **Crossbar**.io in a first terminal

```
crossbar start
```

and start the testsuite in a second terminal

```
wstest -m fuzzingclient -s fuzzingclient.json
```

Testing will take some time. It runs over 500 test cases. In the end, it'll generate HTML report files. Open the `reports/servers/index.html` overview page in your browser - click on the green "Pass" links to view the case detail reports.