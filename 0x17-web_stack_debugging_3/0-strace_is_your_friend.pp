# Using strace, find out why Apache is returning a 500 error

exec { 'fix_E500':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/bin', '/usr/bin', '/usr/local/bin',],
}
