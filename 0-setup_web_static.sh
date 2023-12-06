#!/usr/bin/env bash
# Sets up my web servers for the deployment of web_static

# Install Nginx if it is not installed
sudo apt-get update
sudo apt-get install -y nginx

# Create folder /data/web_static/releases/test/ and /data/web_static?shared/
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file to test nginx configuration
echo "<html>
     <head>
     </head>
     <body>
       Holberton School
     </body>
  </html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create a symbolic link to link the following folders
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of data to user and group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx config to serve the content of /data/web_static/current/
# to hbnb_static

nginx_config='/etc/nginx/sites-available/default'
echo "server {
       listen 80;
       listen [::]:80;
       server_name _;

       location /hbnb_static {
         alias /data/web_static/current/;
       }
}" | sudo tee $nginx_config > /dev/null

# Restart nginx
sudo service nginx restart
