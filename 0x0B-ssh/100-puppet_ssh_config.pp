# Using Puppet to configure the client configuration file.
file { '/home/.ssh/config':
  ensure  => 'file',
  path    => '/home/.ssh/config',
  content => file('/etc/puppetlabs/code/environments/production/modules/ssh/templates/ssh_config.erb'),
}

file { '/home/.ssh':
  ensure => 'directory',
  path   => '/home/.ssh',

}
