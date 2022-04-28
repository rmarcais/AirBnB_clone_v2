# Task #0 but by using Puppet

exec { '1':
command => 'apt-get -y update',
path    => '/usr/bin/',
}

exec { '2':
command => 'apt-get -y install nginx',
path    => '/usr/bin/',
}

exec { '3':
command => 'mkdir -p /data/web_static/releases/test/',
path    => '/usr/bin/',
}

exec { '4':
command => 'mkdir -p /data/web_static/shared/',
path    => '/usr/bin/',
}

exec { '5':
command => 'echo "Hello Holberton !" > /data/web_static/releases/test/index.html',
path    => '/usr/bin/',
}

exec { '6':
command => 'ln -sf /data/web_static/releases/test/ /data/web_static/current',
path    => '/usr/bin/',
}

exec { '7':
command => 'sudo chown -R ubuntu:ubuntu /data/',
path    => '/usr/bin/',
}

exec { '8':
command => "sed -i '47i\\tlocation /hbnb_static { alias /data/web_static/current/; }' /etc/nginx/sites-available/default",
path    => '/usr/bin/',
}

exec { '9':
command => 'service nginx restart',
path    => '/usr/sbin/',
}
