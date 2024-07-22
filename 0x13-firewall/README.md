Make sure you have the latest version of ufw installed
	apt install ufw

check its status
ufw status	---ufw is inactive by default---

default ufw configuration file is /etc/default/ufw
ufw is by default configured to allow all outgoing traffic but deny all incoming traffic -> ssh, http
if you enable the firewall before setting an exception, your current ssh session will be terminated and you will not be able to conn+ ect to your server anymore.
To avoid this, allow incoming ssh connections: 
ufw allow ssh

default ufw policies can be changed with the following command pattern:
+ ufw default <policy> <chain>
+ for example to allow all incoming traffic:
+ ufw default allow incoming
+ to deny all outgoing traffic:
+ ufw default deny outgoing
 A confirmation message will be displayed after each policy change.

ufw allow ssh  ---opens port 22 which is the default port---

if you have ssh configured to use another port,
+ then use a more specific command to create an allow rule for ssh connections.

ufw allow 4444/tcp  ---this firewall rule allows tcp connections to port 4444---

to enable ufw firewall at system startup
ufw enable

ufw status
double check that ufw daemon is running using the systemctl service manager
systemctl status ufw

1.Target Application Profiles
------------------------------
To check applications registered at ufw:
ufw app list

to allow incoming and outgoing access to any of these applications, use this command pattern:
+ ufw allow [app name]

to allow OpenSSH connections:
ufw allow OpenSSH  ---This firewall rule allows all incoming and outgong traffic for OpenSSH application---

You can be more specific and only allow incoming SSH traffic:
 ufw allow in OpenSSH

The best practice for enabling ssh access in a remote server is to use the limit ruleset.
It allows only 6 connections from the same ip address within a 30 second window.
 Saves you from a potential brute force attack.
use limit instead of allow rule for OpenSSH application in production environment.
 ufw limit OpenSSH

2. Target IP Addresses
------------------------
+ You can allow or deny specific ip addresses using:
+ ufw [rule] from [ip address]

 For ex if you see some malicious activity from 192.168.100.20, you may block all traffic from it:
 ufw deny from "ipaddress"
 even though you have blocked this malicious ip address, it may still reach your server in some cases.
 This is because ufw applies its rules from top to bottom.
 For ex your first rule may allow all incoming traffic to port 22,
+ while your deny from "ipaddress" rule may be one step below.
To avoid this,
+ use the prepend option to add the most specific firewall rules to the very top of your rules list.
 Final command would look like this:

 ufw prepend deny from "ipaddress"

3. Target ports
----------------
+ You can target specific ports or port ranges with ufw
+ You may allow connections to port 8080 using any protocol.
+ ufw allow 8080

However you may want to be more specific.
+ Only allow connections to a particular port using a specific network protocol
 For ex to only allow tcp connections to port 8080:
 ufw allow 8080/tcp

sometimes your application may use a range of ports for different activities
To whitelist that port range:
ufw allow 8080:9090/tcp

If you did not want to block all incoming traffic from an ip address:
You may block traffic from that ip address to a specific port
ufw deny from "ipaddress" to any port 53 proto udp -> you block all traffic from "ipaddress" to port 53 using UDP protocol.
This port is usually reserved for a DNS Service

4. Target Network Interfaces
-----------------------------
Some systems have multiple network interfaces configured that may require distinct firewall rules.
ufw allows you to target a specific network interface and only apply the firewall rule to it.
ip addr --to list your system's network interfaces eg eth0, docker etc--

For ex to target the eth0 network interface, you use the eth0 option in your ufw command
	ufw allow in on eth0 from "ipaddress" -> all traffic from ip address is only allowed to the eth0 network interface.

Check your active ufw rules by using this command --ufw status--

To see a more detailed version of the ufw firewall rules: --ufw status verbose--

To see a list of rules in a way that you first typed them --ufw show added--

In contrast to ufw status, ufw show cmd displays firewall rules even when ufw is disabled.


