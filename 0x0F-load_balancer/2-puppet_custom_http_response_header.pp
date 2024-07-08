# Ensure the system is up to date
exec { 'update_upgrade':
  command  => 'sudo apt-get update -y && sudo apt-get upgrade -y',
  provider => shell,
  path     => '/usr/bin:/bin:/usr/sbin:/sbin',
}

# Install Nginx package
package { 'nginx':
  ensure  => installed,
  require => Exec['update_upgrade'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => Package['nginx'],
}

# Add the X-Served-By header to the Nginx configuration
file_line { 'add_x_served_by_header':
  path    => '/etc/nginx/nginx.conf',
  line    => "add_header X-Served-By ${facts['networking']['hostname']};",
  match   => 'sendfile on;',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Restart Nginx to apply the configuration change
exec { 'restart_nginx':
  command     => '/usr/bin/sudo service nginx restart',
  refreshonly => true,
  subscribe   => File_line['add_x_served_by_header'],
}
