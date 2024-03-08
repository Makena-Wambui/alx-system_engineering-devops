#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - this function  runs indefinitely in a loop
 * and in each iteration, sleeps for one second
 *
 * Serves as a placeholder to keep the program running
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - this function is the entry point of the program.
 * calls on fork to create five child processes.
 *
 *
 * Return: 0
 */
int main(void)
{
	int i;
	pid_t pid;

	for (i = 0; i < 5; i++)
	{	/* for each iteration call fork to create a child process.*/
		pid = fork();
		/*if a child process..*/
		if (pid == 0)
			/* exit immediately to become a zombie.*/
			break;
		printf("Zombie process created, PID: %d\n", pid);
	}
	/* parent process enters infinite loop.*/
	if (pid != 0)
	{	/* ensures it remains alive and not exit.*/
		infinite_while();
	}
	return (0);
}
