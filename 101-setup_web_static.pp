# Task #0 but by using Puppet

exec { 'apt-get -y update':
path    => '/usr/bin/env',
}

-> exec { 'apt-get -y install nginx':
path    => '/usr/bin/env',
}

-> exec { 'mkdir -p /data/web_static/releases/test/':
path    => '/usr/bin/env',
}

-> exec { 'mkdir -p /data/web_static/shared/':
path    => '/usr/bin/env',
}

-> exec { 'echo "Hello Holberton !" > /data/web_static/releases/test/index.html':
path    => '/usr/bin/env',
}

-> exec { 'ln -sf /data/web_static/releases/test/ /data/web_static/current':
path    => '/usr/bin/env',
}

-> exec { 'chown -R ubuntu:ubuntu /data/':
path    => '/usr/bin/env',
}

-> exec { 'sed -i '47i\\tlocation /hbnb_static { alias /data/web_static/current/; }' /etc/nginx/sites-available/default':
path    => '/usr/bin/env',
}

-> exec { 'service nginx restart':
path    => '/usr/sbin/env',
}
