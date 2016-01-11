#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <unistd.h>
#include <string.h>
#include <time.h>
#include <openssl/sha.h> 	// sudo apt-get install libssl-dev


main(int argc, char *argv[])
{
	char* flag_id = argv[0];	//
	char* password = argv[1];	//

	// ----- read flag_id in Fahrzeugnummern.csv -----
	// ----- read flag_id in Fahrzeugnummern.csv -----
	// ----- read flag_id in Fahrzeugnummern.csv -----
	// ----- read flag_id in Fahrzeugnummern.csv -----

	FILE *f = fopen("flag_id_file", "r");

	// TODO

	fclose(f);

        // ----- hash password and compare it with stored hash ------
        // ----- hash password and compare it with stored hash ------
        // ----- hash password and compare it with stored hash ------
        // ----- hash password and compare it with stored hash ------
        char cmd[80];
        sprintf(cmd, "echo %s | openssl sha1", password);
//        system(cmd);

	// http://stackoverflow.com/questions/646241/c-run-a-system-command-and-get-output
	FILE *fp;
	char sentpw[1035];

	/* Open the command for reading. */
	fp = popen(cmd, "r");

	if (fp == NULL) {
	  printf("Failed to run command\n" );
	  exit(1);
	}

	/* Read the output a line at a time - output it. */
	fgets(sentpw, sizeof(sentpw)-1, fp);
	printf("gelesen1: %s\n", sentpw);

	/* close */
	pclose(fp);


	// read stored hash
	f = fopen("pwfile", "r");
	char storedpw[1035];
	
	fgets(storedpw, 500, f);
	printf("gelesen2: %s\n", storedpw);
	fclose(f);

	// compare hashes
	if (strncmp(sentpw, storedpw, strlen(sentpw))) {
		printf("Wrong password! \n");
	}
	else {
		printf("password correct!\n");
	}







	// decrypt flagfile and read flag
	f = fopen("flagfile", "r");
	char flag[50];
	fgets(flag, sizeof(flag)-1, f);
	printf("flag read: %s\n", flag);

	fclose(f);
}
