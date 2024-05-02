#include <bits/stdc++.h>
using namespace std;

void selectionSort(int arr[],int n){
  for(int i=0;i<n-1;i++){
    int minIdx=i;
    for(int j=i+1;j<n;j++){
      if(arr[minIdx]>arr[j]){
        minIdx=j;
      }
    }
    swap(arr[i],arr[minIdx]);
  }
}
int main() {
  int arr[]={64, 25, 12, 22, 11 };
  selectionSort(arr,5);
  for(int i=0;i<5;i++){
    cout<<arr[i]<<" ";
  }
  return 0;
}
