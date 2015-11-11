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
	char* content = argv[2];	// the flag itself


	// save flag in file and encrypt file
	FILE *f = fopen("flagfile", "w");
	fprintf(f, "%s", content);

	fclose(f);

	// save flag_id in Fahrzeugnummern.csv
	f = fopen("flag_id_file", "w");
	fprintf(f, "%s", flag_id);

	// TODO
	// TODO
	// TODO

	fclose(f);

	// hash password and save it somewhere
	char cmd[80];
	sprintf(cmd, "echo %s | openssl sha1 > pwfile", password);
	system(cmd);
//	printf("%s", cmd);
}
