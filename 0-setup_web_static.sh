#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static.
# It must:
#	install nginx if it doesn't exist
#	create folder /data/web_static/releases, /data/web_static/shared/
#	and also /data/web_static/releases/test

if [[ ! -x /usr/sbin/nginx ]];
then
    sudo apt-get -y update
    sudo apt-get install -y nginx
fi

sudo ufw allow 'Nginx HTTP'

# create the following the folders if they don't exist
if [[ ! -d "/data/web_static/releases/releases/" ]];
then
    sudo mkdir -p /data/web_static/releases/releases/
fi

if [[ ! -d "/data/web_static/releases/test/" ]];
then
    sudo mkdir -p /data/web_static/releases/test/
fi

if [[ ! -d "/data/web_static/shared/" ]];
then
    sudo mkdir -p /data/web_static/shared/
fi

# create an html file and save it in the file below
sudo echo "
<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    Hello ALX SE!
  </body>
</html>
" > /data/web_static/releases/test/index.html

# A symbolic link should created or recreated on every run
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# update ngnix config file
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# restart nginx to effect changes
sudo service nginx reload
