# django-websockets-no-dep
Django 3.0 with ASGI + web-sockets implementation with no dep

## Trying it out

### Prerequisite

You need to have installed in your system `docker` + `docker-compose`

### Running the project

First build the images, this can take some time based on your Mbps

    docker-compose build

Then start the containers

    docker-compose up

Now you will be able to access to your localhost on port 8000

### Testing it

Firts let's create a websocket connection, open your browser and in the console run

    ws = new WebSocket('ws://localhost:8000/')

Then set a on message function

    ws.onmessage = event => console.log(event.data)

Now from a http client (postman, curl, browser, etc) hit the endpoint `GET` `http://localhost:8000/trigger_event/`

You will get a json response
`{"status": "ok"}`

Now take a look at the console, you should see a console log `Event triggered`
