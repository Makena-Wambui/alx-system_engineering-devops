Local host - this is the default name used to establish connection with your computer using the loopback IP Address.

You can look at it as to mean "this computer"

etc/hosts file is a plain text file that is used by the OS to translate host names/ URLS/ web addresses into IP Addresses.
The host name is looked for here first before the system looks it up in the DNS Servers defined in your network settings.

Because of the first priority that this file is given, we can use it to add to what the DNS Servers can not provide
or to override IP Addresses that the DNS Servers can provide.

Always have a backup copy coz mistakes can lead to problems with network access, in which case you can always restore it.
I had fun testing nc on two consoles.

