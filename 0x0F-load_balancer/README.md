 USAGE OF {HOSTNAME} IN FIRST TASK
-----------------------------------
The {HOSTNAME} variable in most Unix-like systems refers to the environment variable HOSTNAME. This variable holds the name of the host or the computer. It is commonly used in scripts to dynamically obtain the name of the machine on which the script is running.

For example:
echo "This script is running on ${HOSTNAME}"

Same as typing hostname command on the CL.


Steps to Install And Configure HAproxy on your Ubuntu server:
--------------------------------------------------------------
1. Log in to server via ssh

2. Run this command to check whether you have the proper Ubuntu version installed on your server:
	lsb_release -a
	
	This is the output you should see:
		No LSB modules are available.
		Distributor ID: Ubuntu
		Description: Ubuntu 20.04.3 LTS
		Release: 20.04
		Codename: focal
3. Run this command to update all installed packages to the latest availbale version:
	sudo apt-get -y update && sudo apt-get -y upgrade

4. Install HAproxy
	HAproxy is available on the default Ubuntu 20.04 repository.
	But the available package is not the most recent stable version.
	We can check the HAProxy version if we want to install it from the Ubuntu 20.04 repository.
	Run this: sudo apt show haproxy

6. Run this command to install the software-properies-common package, which is likely already installed on your server:
	sudo apt install software-properties-common

7. Run this: sudo add-apt-repository ppa:vbernat/haproxy-2.5
	The above command adds the Personal Package Archive(PPA) into the list of apt sources.
8. Then run this command to complete the installation.
	sudo apt update
	sudo apt install haproxy
9. Check HAProxy version by running:
	sudo haproxy -v

CONFIGURING HAPROXY
------------------------
HAproxy, by default is not configured to listen on a port number.
We will be configuring HAProxy as a load balancer and reverse proxy.
So we will modify the default HAProxy configuration.

First we copy the HAProxy configuration file to another as backup
sudo cp -a /etc/haproxy/haproxy.cfg etc/haproxy/haproxy.cfg.orig

Now we open the file and modify it.
sudo vi /etc/haproxy/haproxy.cfg

Then we append these lines:
<frontend defines how requests are forwarded to the backend servers>
frontend my_frontend
	bind *:80
	option forwardfor
	mode http
	default_backend nginx_backend

backend nginx_backend
	balance roundrobin
	mode http
	server 499808-web-01 18.235.243.79
	server "tobeincluded later"

Restart haproxy: sudo service haproxy restart

TESTING:
You can test that haproxy is properly distributing the load across the two servers:
Invoke a one liner command in your HAProxy server => while true; do curl localhost; sleep 1; done


Adding Header using Puppet
------------------------------
Explanation:
Update and Upgrade:

The exec resource named update_upgrade runs apt-get update and apt-get upgrade commands. This ensures the system is up-to-date.
Install Nginx:

The package resource installs the nginx package and ensures it is installed before proceeding with the configuration.
Manage Nginx Service:

The service resource ensures that the Nginx service is running and enabled to start on boot. It also subscribes to changes in the nginx package, so the service will be restarted if the package is updated.
Add Custom Header:

The file_line resource adds the X-Served-By header to the Nginx configuration file. It matches the line sendfile on; and adds the header directly after it. This resource requires the Nginx package to be installed first and notifies the nginx service to restart if the configuration changes.
Restart Nginx:

The exec resource named restart_nginx restarts the Nginx service only if the file_line resource makes a change. The refreshonly => true parameter ensures this command runs only when notified.

NOTE TO SELF: MY ORIGINAL SCRIPTS WERE GOOD. DO NOT LET AI CONFUSE YOU.
