# Task #0 but by using Puppet

exec { '1':
command => 'apt-get -y update',
path    => '/usr/bin/',
}

-> package { 'nginx':
ensure   => 'installed',
provider => 'apt',
}

-> exec { '3':
command => 'mkdir -p /data/web_static/releases/test/',
path    => '/usr/bin/',
}

-> exec { '4':
command => 'mkdir -p /data/web_static/shared/',
path    => '/usr/bin/',
}

-> file { '/data/web_static/releases/test/index.html':
ensure  => 'present',
path    => '/data/web_static/releases/test/index.html',
content => 'Hello Holberton !\n',
}

-> exec { '6':
command => 'ln -sf /data/web_static/releases/test/ /data/web_static/current',
path    => '/usr/bin/',
}

-> exec { '7':
command => 'sudo chown -R ubuntu:ubuntu /data/',
path    => '/usr/bin/',
}

->exec { '8':
command => "sed -i '47i\\tlocation /hbnb_static { alias /data/web_static/current/; }' /etc/nginx/sites-available/default",
path    => '/usr/bin/',
}

-> service { 'nginx':
ensure  => 'running',
require => Package['nginx'],
}
