# Use a base image with Nginx pre-installed
FROM nginx:alpine

# Remove the default Nginx configuration
RUN rm -rf /etc/nginx/conf.d/*

# Copy your custom Nginx configuration
COPY nginx.conf /etc/nginx/conf.d/

# Copy your application files to the web root directory
COPY . /usr/share/nginx/html
