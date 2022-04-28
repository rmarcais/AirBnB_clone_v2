# Task #0 but by using Puppet

exec { '1':
command => 'sudo apt-get -y update',
}

exec { '2':
command => 'sudo apt-get -y install nginx',
}

exec { '3':
command => 'mkdir -p /data/web_static/releases/test/',
}

exec { '4':
command => 'mkdir -p /data/web_static/shared/',
}

exec { '5':
command => 'echo 'Hello Holberton !' > /data/web_static/releases/test/index.html',
}

exec { '6':
command => 'ln -sf /data/web_static/releases/test/ /data/web_static/current',
}

exec { '7':
command => 'sudo chown -R ubuntu:ubuntu /data/',
}

exec { '8':
command => "sed -i '47i\\tlocation /hbnb_static { alias /data/web_static/current/; }' /etc/nginx/sites-available/default",
}

exec { '9':
command => 'sudo service nginx restart',
}
