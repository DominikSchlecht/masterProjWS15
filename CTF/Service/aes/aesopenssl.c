#include <stdlib.h>
#include <stdio.h>


char *randstring(size_t length) 
{

    static char charset[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";        
    char *randomString = NULL;
    int n = 0;
    if (length) {
        randomString = malloc(sizeof(char) * (length +1));

        if (randomString) {            
            for (n = 0;n < length;n++) {            
                int key = rand() % (int)(sizeof(charset) -1);
                randomString[n] = charset[key];
            }

            randomString[length] = '\0';
        }
    }

    return randomString;
}

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
		else if(strcmp(argv[1], "decrypt")==0)
		{
			char* randName = randstring(15);
			FILE* f = NULL;
			char* tmp = malloc(sizeof(char)*2000);
			char* remove = malloc(sizeof(char)*200);
			sprintf(tmp, "openssl aes-256-cbc -d -in %s.enc -out %s -pass pass:Â§acf578?#*+-463-{{}av@wer637,,..", argv[2], randName);
			printf("%s\n", randName);
			f = popen(tmp, "w");
			pclose(f);
			FILE* output=fopen(randName, "r");
			char* encryptedData[1500];
			int i = 0;
			encryptedData[0] = malloc(sizeof(char)*500);
			char line[1024];
			while(fgets(line, 1024, output)!=NULL)
			{
				sprintf(encryptedData[i], "%s", line); 
				i++;
				encryptedData[i] = malloc(sizeof(char)*500);
			}
			int p = 0;
			for(p = 0; p < 15; p++)
				printf("---------------------------------------->%s\n", encryptedData[p]);
			
			
			/*
			FILE *test = fopen("Bayrisch.csv.out");
			char line[1024];
			fgets();*/
			/*
			 *	Hier kommt was hin was die Datei weitergibt!
			 * 
			 *
			 */
			sprintf(remove, "rm %s", randName);
			popen(remove, "w");
			return 0;
		}

	}
	else
	{
		printf("too few or too many arguments");
		
	}

}
