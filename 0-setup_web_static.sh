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
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" | sudo tee $nginx_config > /dev/null

# Restart nginx
sudo service nginx restart
