#This manifest creates a file in /tmp directory with the name school
file { '/tmp/school':
        ensure  => present,
        mode    => 0744,
        owner   => 'www-data',
        group   => 'www-data',
        content => 'I love Puppet',
        }
}
