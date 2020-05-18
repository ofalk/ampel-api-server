# ampel-api-server
Simlistic/minimalistic API server for my Cleware (Nagios) Ampel

# Install

Clone the repo, install a virtual env if you want/need.

Install Flask - via pip:

    $ pip install -r requirements.txt

or on your Raspbian via apt-get:

    # apt-get install python3-flask

And make sure you have the clewarecontrol [1] tool in ~/clewarecontrol/clewarecontrol.

And run the API server:

    $ ./api_server.py

The server has no security or so and is going to listen on 0:8080.

You can therefore access it for example:

    $ curl -XPOST -H "Content-type: application/json" \
      -d '{ "green": 0, "red": 1, "yellow": 1 }' \
      <replace-with-your-ip>:8080/set

The above line will set red/yellow to on and green to off. If you do not
specify one color, the current state will not be changed.

To query the states:

    $ curl -XGET <replace-with-your-ip>:8080/red
    $ curl -XGET <replace-with-your-ip>:8080/yellow
    $ curl -XGET <replace-with-your-ip>:8080/green

# Further work.

I'd be very interested if someone has an idea how to *query* the different
colors using pure Python USB - at the moment this tool uses the
clewarecontrol [1] tool to query tht states, since the
cleware-traffic-light [2] Python module doesn't do that and I'm not too
familiar with USB programming.

# License

This is licensed under MIT - so feel free to do with it whatever you like, but
I'd appreciate if you could share your patches with me.


# References

[1] https://github.com/flok99/clewarecontrol.git
[2] https://github.com/ofalk/cleware-traffic-light.git
    cloned from https://github.com/joshrost/cleware-traffic-light.git
    with small adaptions.
