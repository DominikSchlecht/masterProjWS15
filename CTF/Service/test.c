#include <stdio.h>
#include <string.h>

main(int argc, char *argv[])
{
  char str[1024];
  int pass = 100;
  char *a = "AAAAAAAAA";
  char flag[9];
  int len, i;
  strcpy(flag, "flgAAAAA");
  strcpy(str, argv[1]);
  printf("Hello World\n");

  len = strlen(a);
  for (i = 0; i < len; i++){
    __asm__ volatile (  "push  %%rax\n"
                    //"popq   %%rax\n"

                  :           /* OUTPUT values         */
                  : "a"(a[i])           /* INPUT  values         */
                  :    /*No need for the clobber list, since the compiler knows
                      which registers have been modified            */
              );
  }
  printf(str);
  __asm__ volatile (  //"pushq  %%rax\n"
                  "pop   %%rax\n"

                :           /* OUTPUT values         */
                : //"a"(x)           /* INPUT  values         */
                :    /*No need for the clobber list, since the compiler knows
                    which registers have been modified            */
            );

  if (pass==200){
      printf("OK!");
  }


}
