#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

/*
 * Outline of solution by dynamic programming:
 * first make an list of perfect squares <= n
 * then start to build a cached result as follows:
 * f(1)=1
 * f(2)=2
 * f(3)=3
 * f(4)=1
 * ...
 * for each i, search through the list of perfect squares that are <=i, and define
 *
 * f(i) = i in squares? 1 : min{f(p)+f(i-p) | p in squares and p<i}
 *
 *
 *
 *
 *
 *
 * */

int compute_best_hash(int *squares, int n){
// compute this pointwise for i from 1 to n
// for i=1, 2, 3, set result[i]=i
// for other i= 4..n, do:
// 	set temp=n+1
// 	for each square <=i, do:
// 		int throwaway
// 		compute throwaway = result[square] + result[i-square]
// 		set temp = temp<throwaway? temp : throwaway
//	set result[i]=temp
// return result[n]	
//
//
//
	int result[n];
	int index=1;
	for (index=1; index<=n; index++){
		int *s = squares;
		if (index<=3){
			result[index]=index;
}
		else{
			int value=n+1;
			int throwaway;
			while ((*s)<=index){
//				printf("this square up is %d and index is %d\n", *s, index);
				if ((*s)==index){result[index]=1; break;}
				else{
//					printf("currently at index %d, we're looking at the points %d and %d which contain values %d and %d\n", index, *s, index-*s, result[*s], result[index-*s]);
					throwaway = result[*s] + result[index - (*s)];
					value = ((throwaway<value) ? throwaway : value);
//					printf("throwaway is %d, value is %d\n", throwaway, value);
					s++;
//					printf("next square up is %d and index is %d\n", *s, index);
			result[index]=value;
}
}
//			printf("the optimal value for index %d is %d\n", index, result[index]);
}
}
//	for (index=0; index<=n; index++){
//		printf("%d, ", result[index]);
//}
	return result[n];
}


int get_largest_square(int *p, int length, int n){
	if (length<1 || n<1){
		return -1;
}
	int *q=p;
	while (((q-p)<=length) && (*q)<=n){
		q++;	
}
	return *(--q);
}

int *initialize_squares_array(int *p, int n){
	int i=1, *q=p;
	while (i<=n){
		*(q++)=i*i;
		i++;	
}
//	q=p;
//	printf("squares are:\n");
//	while (q-p<n){
//		printf("%d, ", *(q++));
//}
//	printf("Done printing the squares.\n");
	return p;
}

int *initialize_results_array(int *p, int n){
	int i=1, *q=p;
	while (i<=n){
		if (i<=3) {
			*(q++)=i++;
}
		else{
			*(q++)=-1;
			i++;
}
						
}
		
	return p;
}

int main(int n){

printf("Enter a number: ");
scanf("%d", &n);

int squares[n];
int result[n];
int *p_result = result;
int *p_squares = squares;

p_squares = initialize_squares_array(p_squares, n);
p_result = initialize_results_array(p_result, n);

int *q=p_squares;

printf("answer is %d\n", compute_best_hash(squares, n));

return result[n];


}




