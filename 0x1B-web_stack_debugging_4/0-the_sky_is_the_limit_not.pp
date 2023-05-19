#Fixing nginx so that it should serve 2000 requests
exec { 'increase_nginx_limit':
  command => 'sed -i "s/4/2500/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin'
}

#Nginx restarting
exec { 'restart_nginx':
  command => 'restart nginx',
  path    => '/etc/init.d/'
}
