#Fixing nginx so that it should serve 2000 requests
exec { 'increase-nginx':
  command => '/usr/bin/env sed -i s/4/2500/ /etc/default/nginx',
}
exec { '/usr/bin/env service nginx restart': }
