### LIST OF THE BEST PRACTICES FOR A DOCKERFILE:

1. Not using `COPY . .`. It creates a possible security breach.

2. Exposing ports, so that the users of our container know whcoh ports to bind to.
3. Using `.dockerignore`. This helps us not carry different cache and unused files to the container, thus reducing it's size and saving money.
4. Rootless container. Creating a user and limiting it's access rights helps avoiding unnecessary privileges, which makes the container more secure.
5. Using `COPY` instead of `ADD`. Both the ADD and COPY instructions provide similar functions in a Dockerfile. However, COPY is more explicit. It is better to COPY unless you really need the ADD functionality, like to add files from an URL or from a tar file. 
6. Smashing RUN, COPY and ADD commands together will create less layers. It also makes it easier to cache.
7. Using linters is also a great idea. I've already written about them in `PYTHON.md`. This timje is used `hadolint`.