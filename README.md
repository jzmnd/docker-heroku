# docker-heroku

A simple example of a Flask web app using Docker and Heroku container deployment. We use miniconda for library installs.

This approach solves this issues of using advanced machine learning and scientific libraries (such as sklearn or scipy) with Heroku which often lead to large slug sizes. It requires Docker to form a container with all the dependencies and then to push that container to Heroku.

It extends the basic [python-miniconda](https://github.com/heroku-examples/python-miniconda) example to work on apps that have a modular structure i.e. "app" is a module rather than a single ".py" file.

Usage...

1. Install [Docker](https://www.docker.com)
1. Clone this repo `git clone https://github.com/jzmnd/docker-heroku.git`
1. Install container plugin `heroku plugins:install heroku-container-registry`
1. Login to Heroku `heroku login`
1. Login to Heroku registry `heroku container:login`
1. Create your heroku app `heroku create`
1. Push the container `heroku container:push web`
1. Run app `heroku open`
