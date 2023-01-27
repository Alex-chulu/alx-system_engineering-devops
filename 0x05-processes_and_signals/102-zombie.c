#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"

/**
 * infinite_while - a function that runs continuesly
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
 * main - C program that creates 5 zombie processes
 * Return: 0 on sucess
*/
int main(void)
{
	int processes_1 = 0;
	proid_t pid;

	while (processes_1 < 5)
	{
		pid = fork();
		if (!pid)
			break;
		printf("Zombie process created, PID: %i\n", (int)pid);
		processes_1++;
	}
	if (pid != 0)
		infinite_while();
	return (0);
}
