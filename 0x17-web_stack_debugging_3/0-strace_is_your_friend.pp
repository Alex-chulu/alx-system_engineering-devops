# Using strace, find out why Apache is returning a 500 error

file_line { 'fix_phpp':
  path   => '/var/www/html/wp-settings.php',
  line   => "define('WP_DEBUG', false);",
  match  =>'phpp',
  replace => 'php',
}
