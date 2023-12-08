#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static.
# It must:
#	install nginx if it doesn't exist
#	create folder /data/web_static/releases, /data/web_static/shared/
#	and also /data/web_static/releases/test

sudo apt-get update
sudo apt-get install -y nginx
sudo ufw allow 'Nginx HTTP'

# create the following the folders if they don't exist
sudo mkdir -p /data
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

# create an html file and save it in the file below
sudo echo "
<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    Hello ALX SE!
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# A symbolic link should created or recreated on every run
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# update ngnix config file
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# restart nginx to effect changes
sudo service nginx reload
