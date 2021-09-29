# DockerApp
#### A test Django application with production-level docker setup.

**Blog: https://medium.com/@siddharth.sahu/the-near-perfect-dockerfile-for-django-applications-8bc352a1e871**

This project is to document production-level Docker setup. Please note that Django application is rudimentary and not fit for production.

This project present docker setup of four component of a typical Django application i.e. web server, celery worker, celery beat and celery monitoring using flower.

## Docker Setup
Detailed documentation of Docker setup can be found in above blog.
It discusses in detail `Dockerfile`, `entrypoint.sh` and `start.sh`

#### Useful Commands
To be run from root of the project.

Note: Before running commands, copy `.sample-env` into `.env` in the same level `dockerapp/docker/`.
1. Build docker image with tag 'development':
`docker build -t dockerapp:development -f docker/Dockerfile .`

2. Start all containers including essential services(PostgreSQL and Redis):  `docker-compose -f docker/docker-compose.yml up`

3. Stop all containers: `docker-compose -f docker/docker-compose.yml down`

## Django application details
The Django application has a simple view `dockerapp/core/views.py` linked to url `/task-trigger/`, which picks a random integer between 1 and 100 and send to celery task(defined in `dockerapp/core/tasks.py`) which count next five integer at interval of one second.


## Development
This is a work in progress, hence further enhancements in all aspects of Docker in this project is expected. Any advice regarding improvement of Docker aspect is welcome and encouraged.

For detailed discussion please refer to corresponding blog https://medium.com/@siddharth.sahu/the-near-perfect-dockerfile-for-django-applications-8bc352a1e871.
 
