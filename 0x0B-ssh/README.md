
What is a server:
A computer, physical orvirtual, running an operating system, that provides information(serves up data)=> services, to other computers on a computer network.

Where servers usually live:
They live in datacentres.

What is SSH:
Secure Shell. A secure communication protocol that provides a safe and secure way(encrypted traffic)
to execute commands, make changes and configure services remotely.

How to create an SSH RSA key pair:
Use the ssh-keygen command.

How to connect to a remote host using an SSH RSA key pair:
Use the ssh command, the name of the account in the remote server, and the remote server's ip address or hostname.

The advantage of using #!/usr/bin/env bash instead of /bin/bash
The advantage of using #!/usr/bin/env bash over #!/bin/bash in the shebang line at the beginning of a script is portability.

Environment Lookup: The env command will search for the bash executable in the user’s PATH environment variable. This means that it will find bash no matter where it is installed on the system, which can vary between Unix-like operating systems.
Flexibility: If there are multiple versions of bash installed, #!/usr/bin/env bash will ensure that the user’s preferred version is the one being used to execute the script.
User Preferences: Users can have a custom version of bash installed in their home directory or another non-standard location, and env will find it as long as the directory containing the executable is in the PATH.
However, it’s important to note that while #!/usr/bin/env bash provides flexibility and portability, #!/bin/bash gives you explicit control over which executable is called, assuming you know the path to bash and it doesn’t change across environments. This can be important for scripts that require specific bash features that are only available in certain versions.
