#Fixing nginx so that it should serve 2000 requests
exec { 'increase_nginx_limit':
  command => 'sed -i "s/4/2500/" /etc/default/nginx',
  path    => '/usr/bin/env'
}

#Nginx restarting
exec { 'restart_nginx':
  command => 'service nginx restart',
  path    => '/usr/bin/env'
}
