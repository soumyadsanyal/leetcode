bool isPowerOfThree(int n) {
    if (n<1) {return 0;}
    while (n>1){
    if (n%3==0) {n=n/3; continue;}
    else{
        return 0;
    }
    }
    return 1;
}