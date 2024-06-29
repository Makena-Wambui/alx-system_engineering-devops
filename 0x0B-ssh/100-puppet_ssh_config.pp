# Puppet manifest for seting  up your client SSH configuration file so that you can connect
# to a server without typing a password.

file_line { 'password_auntheticate':
    path => '~/.ssh/config',
    line => 'PasswordAuthentication no', # ensures line is in file specified in path
}

file_line { 'identity_file':
    path => '~/.ssh/config',
    line => 'IdentityFile ~/.ssh/school',
}
