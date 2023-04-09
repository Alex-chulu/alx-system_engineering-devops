# Just as in task #0, we’d like you to automate the task of 
# creating a custom HTTP header response, but with Puppet.

class { 'nginx':
	http_extra_headers => {
		'X-Served-By' => $::hostname,
},
}
