# Puppet script to configure nginx for webstatic deployment

$server_config = "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By ${hostname};
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location /redirect_me {
        return 301 https://github.com/itsoluwatobby/;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}"

$my_html = "<html>
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
  content => $my_html
} ->

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  force => 'yes'
} ->

exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}

file { '/var/www':
  ensure => 'directory'
} ->

file { '/var/www/html':
  ensure => 'directory'
} ->

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => $my_html
} ->

file { '/var/www/html/404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page\n"
} ->

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $server_config
} ->

exec { 'nginx restart':
  path => '/etc/init.d/',
}
