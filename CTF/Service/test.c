#include <stdio.h>
#include <string.h>

main()
{
  char str[BUFSIZ];
  int pass = 100;
  char flag[9];
  strcpy(flag, "flgAAAAA");
  printf("Hello World\n");
  scanf("%s", str);
  if (pass==200){
      printf("OK!");
  }

  printf(str);
}
