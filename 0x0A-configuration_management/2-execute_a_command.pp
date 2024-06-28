# a puppet manifest that kills the process 'killmenow' using the exec resource

exec { 'kill process':
    command => 'pkill killmenow', # command to execute
    path    => ['/usr/bin'], # directories to search for the pkill command
    onlyif  => 'pgrep killmenow', # only run exec if the process is running
}
