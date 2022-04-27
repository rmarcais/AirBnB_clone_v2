#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
if [ ! -x /usr/sbin/nginx ]; then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi
if [ ! -d "/data/" ]; then
    mkdir /data/
fi
if [ ! -d "/data/web_static/" ]; then
    mkdir /data/web_static/
fi
if [ ! -d "/data/web_static/releases/" ]; then
    mkdir /data/web_static/releases/
fi
if [ ! -d "/data/web_static/releases/test" ]; then
    mkdir /data/web_static/releases/test/
fi
if [ ! -d "/data/web_static/shared/" ]; then
    mkdir /data/web_static/shared/
fi
echo "Hello Holberton !" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sed -i '/server_name _;/a location /hbnb_static { alias /data/web_static/current/; }' /etc/nginx/sites-available/default
sudo service nginx restart
