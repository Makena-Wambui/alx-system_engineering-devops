What are $0, $1, $2..
These are positional arguments of the script.

Executing

./script.sh Hello World
Will make

$0 = ./script.sh
$1 = Hello
$2 = World
Note

If you execute ./script.sh, $0 will give output ./script.sh but if you execute it with bash script.sh it will give output script.sh.
Positional parameter N may be referenced as ${N}, or as $N when N consists of a single digit.
When a positional parameter consisting of more than a single digit is expanded, it must be enclosed in braces.

Run man sudo:
-------------
sudo -u will run the command as the user specified other than the default user.
For ex sudo -u www-data whoami will run the cmd whoami as www-data
