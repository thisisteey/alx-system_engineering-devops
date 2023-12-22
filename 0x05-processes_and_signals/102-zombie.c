#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
 * infinite_while - Starts an inifinty loop with a sleep of 1 second
 * Return: 0 if the loop is interrupted by a signal
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
 * create_zombie - creates a new child process and prints PID
 * Return: void
 */
void create_zombie(void)
{
	int child_pid = fork();

	if (child_pid == 0)
	{
		printf("Zombie process created, PID: %d\n", getpid());
		exit(0);
	}
}

/**
 * main - creates 5 zombie processes using create_zombie
 * Return: 0 on code success
 */
int main(void)
{
	create_zombie();
	create_zombie();
	create_zombie();
	create_zombie();
	create_zombie();
	return (infinite_while());
}
