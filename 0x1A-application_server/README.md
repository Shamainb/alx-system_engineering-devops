Task Descriptions

1. Set up development with Python

- Clone the AirBnB clone v2 project onto your server.
- Configure Flask application to serve content from a specific route and port.
- Run the Flask application using `python3 -m` command.

2. Set up production with Gunicorn

- Install Gunicorn and any necessary libraries.
- Bind Gunicorn to serve content from the same route and port as the development environment.
- Use Gunicorn as the WSGI entry point into the Flask application.

3. Serve a page with Nginx

- Configure Nginx to serve content from the Flask application.
- Proxy requests to the Flask application listening on a specific port.
- Serve the page both locally and on the public IP on port 80.

4. Add a route with query parameters

- Expand the Flask application to handle additional routes.
- Configure Nginx to proxy requests to different routes to separate Gunicorn instances.

5. Serve your AirBnB clone

- Clone the AirBnB clone v4 project onto your server.
- Configure Gunicorn to serve content from a specific route and port.
- Setup Nginx to serve static assets and proxy requests to the Gunicorn instance.
Notes

- Each task requires careful configuration of the Flask application, Gunicorn, and Nginx to ensure proper functionality.
- Follow the provided examples and instructions for each task to verify the setup.
- Ensure that Nginx is properly configured to handle incoming requests and proxy them to the correct Gunicorn instances.

