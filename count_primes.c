#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <string.h>

int countPrimes(int);
void populate_array(int*, int);

int main(void){
	int input;
	scanf("%d", &input);
	printf("You asked for the number of primes less than %d\n", input);
	printf("There are %d primes less than %d\n", countPrimes(input), input);
	return 0;

}

int countPrimes(int n){
	printf("here");
	int *array = malloc(sizeof(int)*n);
	populate_array(array, n);
//	int i=0;
//	for(i=0;i<n-1;i++){printf("%d, ", *(array+i));}
	int *p = array;
	for(p=array; p<array+n-1; p++){
		int *q = p+1;
		while (q<array+n-1){
			if ((*q) % (*p) == 0){
				*q=0;
}
			q++;
			
}
}	
	int i=0;
	for(i=0;i<n-1;i++){printf("%d, ", *(array+i));}
	return 0;
}

void populate_array(int* array, int n) {
	int i=2;
	int *p = array;
	while (p<array+n-1){
		*p=i;
		i++;
		p++;
}
	*p='\0';
}
