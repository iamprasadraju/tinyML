#include <stdio.h>

#define N 1024

float A[N][N];
float B[N][N];
float C[N][N];

int main(){
	for(int i = 0; i < N; i++){
    	for(int j = 0; j < N; j++){
      		float acc = 0;
      		for(int k = 0; k < N; k++){
        		acc += A[j][k] * B[k][i];
      		}                                
      		C[i][j] = acc;
    	}	
   	}
   	return 0;

}