#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//int length(char*);
void reverse_it(char*, char*);

int main(void){

char* a;
char* b;

scanf("%s", a);
//int l = length(a);
//printf("length is %d\n", l);
int l=0;
char* temp = a;
while (*a!='\0') {a++; l++;}
a=temp;
b = malloc(l);
reverse_it(a, b);
printf("You entered %s, which gives %s\n", a, b);


return 0;


}


void reverse_it(char* a, char* b ){

	int i;
	char* temp_1 = a;
	char* temp_2 = b;

//move to end of first string
	while(*a != '\0'){a++;}

// backtrack and copy to b
	while(a>temp_1){
	a--;
	*(b) = *(a);
	printf("pointer a holds %c\n", *a);
	printf("pointer b holds %c\n", *b);
	b++;
	}
	*(b++)='\0';
	b=temp_2;
	printf("%s\n", b);

return;
}

/*
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
*/

