STRACE
-------
A process monitoring tool.


Installation: sudo apt install strace

Examples:
To get the system call, argument, and the result of the call:
 1. strace ls -> 'Here “ls” is the command whose system call is to be traced.'

 2. +++ exited with 0 +++ -> 'exit status is 0 which means there was no error. In case of an error, the exit code is -1.'

 
 3. strace -c ls -> To count number of system calls: 
			NB: ls” is the command whose system call is to be traced.
                     it displays the number of times each system call was made and prints the total
		     and even showing the number and time spent in each call.
 
 4. strace -e trace=write ls:
	trace particular or specific system calls.
	“ls” is the command whose system call is to be traced.
	And the name of the system call which is to be traced is write.
 
 5. strace -e trace=network nc -v -n 127.0.0.1 801:
	trace network related system calls.
	“nc -v -n 127.0.0.1 801” is the command whose system call is to be traced.
	And the name of the system call which is to be traced is the network.

 6. strace -e trace=signal nc -v -n 127.0.0.1 801
	trace signal related system calls
	“nc -v -n 127.0.0.1 801” is the command whose system call is to be traced.
	And the name of the system call which is to be traced is signal.

 7. strace -r ls
	print timestamp of each call.

 8. strace -o output.txt ls
	print output to a file
	“ls” is the command whose system call is to be traced.
	And output.txt is the name of the file in which output is to be stored.
 9. strace -T ls
	“ls” is the command whose system call is to be traced.
