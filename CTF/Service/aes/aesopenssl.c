#include <stdlib.h>
#include <stdio.h>

int main(int argc, char* argv[])
{
	if (argc == 3)
	{
		if(strcmp(argv[1], "encrypt") == 0)
		{
			char* tmp = malloc(sizeof(char)*2000);
			sprintf(tmp, "openssl aes-256-cbc -in %s -out %s.enc -pass pass:Â§acf578?#*+-463-{{}av@wer637,,..", argv[2], argv[2]);
			popen(tmp, "w");
			return 0;		
		}
		else if(argv[1], "decrypt")
		{
			char* tmp = malloc(sizeof(char)*2000);
			char* remove = malloc(sizeof(char)*200);
			sprintf(tmp, "openssl aes-256-cbc -d -in %s.enc -out %s.out -pass pass:Â§acf578?#*+-463-{{}av@wer637,,..", argv[2], argv[2]);
			FILE* f = popen(tmp, "w");
			pclose(f);
			/*
			FILE *test = fopen("Bayrisch.csv.out");
			char line[1024];
			fgets();*/
			/*
			 *	Hier kommt was hin was die Datei weitergibt!
			 * 
			 *
			 */
			sprintf(remove, "rm %s.out", argv[2]);
			popen(remove, "w");
			return 0;
		}

	}
	else
	{
		printf("too few or too many arguments");
		
	}

}
