# Puppet script to configure nginx for webstatic deployment


$server_block = "server {
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
        return 301 http://fkadeal.com/;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}"

$dummy_html = "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

package { 'nginx':
  ensure   => 'present',
  provider => 'apt'
} ->

file { '/data':
  ensure  => 'directory'
} ->

file { '/data/web_static':
  ensure => 'directory'
} ->

file { '/data/web_static/releases':
  ensure => 'directory'
} ->

file { '/data/web_static/releases/test':
  ensure => 'directory'
} ->

file { '/data/web_static/shared':
  ensure => 'directory'
} ->

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => $dummy_html
} ->

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  force => 'yes'
} ->

exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $server_block
} ->

service { 'nginx':
  ensure => 'running',
}
