Crossbar.io is under active development. Below are features which are under development or planned. 

Since we are resource-constrained we cannot give a precise roadmap for these features. We try to consider user interest when prioritizing features. So please contact us if you need something - or better yet, help us in implementing it!

### Support for Python 3

We're supporting the porting of the Twisted framework to Python 3, and have already gotten Crossbar.io to run on Python 3. 

### Database Integration

Adds connectors for 

* PostgreSQL
* Oracle

These allow databases to become WAMP clients. They offer all four WAMP client roles:

* *Publisher*
* *Subscriber*
* *Caller*
* *Callee*

(Note: Caller functionality may be limited due to lack of support for async operations in PL/SQL.)

### Features from the WAMP Advanced Profile
   
* forced subscriber unsubscribe
* event history
* call timeouts
* forced callee unregister
* cancelling calls

### Additional Features

* automatic reloading of components

### Multi-core and Multi-node Support

WAMP messages are routed between routers. This allows to scale Crossbar and/or increase system availability by scaling up to multiple cores and/or scaling out to multiple nodes (clustering, federation).

### Partitioned Calls and Events

Partitioned calls enable using e.g. database sharding.

-----------------------------------

Additionally, Tavendo, the maintainers of the Crossbar.io project, are planning commercial offerings to be used with Crossbar:

* Cloud Management Service

  * manage your Crossbar instances centrally
  * instances connect to a central cloud management service run by Tavendo

* Hosted Crossbar Realms (Routing-as-a-Service)

and are already offering commercial support (see their [website](http://tavendo.com) for contact details).