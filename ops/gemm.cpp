#include <iostream>
using namespace std;

const int N = 1000;

// Heap
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
    }
  }
  return 0;
}
