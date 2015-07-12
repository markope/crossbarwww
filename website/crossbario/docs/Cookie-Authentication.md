Cookie authentication works like this.

With cookie tracking enabled, a browser client or generally any WAMP client connecting via WAMP-over-WebSocket is handed out a randomly assigned cookie by Crossbar.io.

When the client then authenticates using a WAMP authentication method such as WAMP-CRA, upon successful authentication, Crossbar.io will attached the authentication information to the cookie stored in the cookie store (either transiently or persistently).

When the client then comes back later, and sends the cookie handed out previously, Crossbar.io will look up the cookie, and if the cookie has attached authentication information, it will immediately authenticate the client using the previously stored information.
