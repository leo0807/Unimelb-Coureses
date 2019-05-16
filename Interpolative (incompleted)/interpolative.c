#include <stdio.h>
#include <stdlib.h>
#include <time.h>
void integer_to_bin(int num){

}
char *exp_golomb(int number, int expetional){
    char str[30];
    itoa(number,str,2);//2即是代表转换为2进制
    printf("%s ",str);
    return "";
}
int binary_code(int L, int low, int high){
    if(high + 1 - low <= 0){return -1;}
    else{
       int result = L - low;
       return result;
    }
}
int binary_interpolative(int L[], int f, int low, int high){
    if (f == 0){ return 0;}
    else if (f == 1) {return binary_code(L[0], low, high);}
    else{
        int h = floor((f + 1)/2);
        int f1 = h;
        int f2 = f - h - 1;

       // return (binary_code(m, low + f1, high - f2) ++ (binary_interpolative(L1, f1, low, m - 1) ++ binary_interpolative(L2, f2, m + 1, high)));
    }
    return 0;

}
int random(int range, int nums){
    if ((range < 1) || (range < nums) ||( nums < 1)){
        return "Inputs Error";
    }else{
        int result[nums], j = 0;
        srand((unsigned int)time(0));

        for(int i = 0; i <= nums; i++){
            result[i] = rand() % range + 1;
        }

        printf("%d ", result[0]);
        return result;
    }
}

int main()
{
    int b  = binary_code(12,4,17);
    printf("%d ", b);
    random(100,50);
    return 0;
}
