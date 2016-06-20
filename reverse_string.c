#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int length(char*);
void reverse_it(char*, char*);

int main(void){

char* a;

scanf("%s", a);
int l = length(a);
//printf("length is %d\n", l);
char* b = malloc(l);
reverse_it(a, b);
printf("You entered %s, which gives %s\n", a, b);


return 0;


}


void reverse_it(char* a, char* b ){

	int i;
	int l=length(a);
	char* c = b;

	while(*a != '\0'){a++;}

	for(i=0; i<l; i++){
	a--;
	*b = *a;
//	printf("pointer b holds %c\n", *b);
	b++;
	}
	*(b++)='\0';
	b=c;
	printf("%s\n", b);

return;
}


int length(char* a){

	int i;
	int length = 0;
	while ((*a) != '\0'){
		length++; 
		a++;
	}

	a=a-length;

	return length;

}


