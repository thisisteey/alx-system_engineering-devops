# Using Puppet, install flask from pip3
package { 'python3-pip':
  ensure => installed,
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0 werkzeug==2.0.3',
  path    => ['/usr/bin'],
  require => Package['python3-pip'],
}
