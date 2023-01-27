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
	pid_t proid;

	while (processes_1 < 5)
	{
		proid = fork();
		if (!proid)
			break;
		printf("Zombie process created, PID: %i\n", (int)proid);
		processes_1++;
	}
	if (proid != 0)
		infinite_while();
	return (0);
}
