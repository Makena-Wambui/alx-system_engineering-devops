# Change limit to requests that Nginx can handle

exec { 'change_limit_and_restart':
    command  => 'sudo sed -i "s/15/4096/g" /etc/default/nginx; sudo service nginx restart',
    provider => shell,
}
