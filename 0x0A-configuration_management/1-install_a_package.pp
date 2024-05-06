# install flask package using pip3 provider
# If Flask is not installed, or if a different version is installed,
# Puppet will install or update Flask to the specified version.
package { 'flask':
    ensure   => '2.1.0', # pass version to ensure attribute
    provider => 'pip3',
}
