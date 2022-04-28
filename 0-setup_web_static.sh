#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Hello Holberton !" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sed -i '47i\\tlocation /hbnb_static { alias /data/web_static/current/; }' /etc/nginx/sites-available/default
sudo service nginx restart
