// Use C++17 std 
#include <iostream>

int main(){
    int a[] = {100,99,98,97,96,10,31,5}; 
    int n = std::size(a);
    std::cout<< "Array size" << n << std::endl;

    //Bubble sort
    for (int j = 1; j < n; j++){
        for (int i = 0; i < (n-j); i++){
            if (a[i] > a[i+1]){ // Swap elements
                int t = a[i+1];
                a[i+1] = a[i];
                a[i] = t;
            }
        }
    }

    // Print array
    for (int i =0; i < n; i++){
        std::cout << a[i] << std::endl;
    }
    

    return 0;
}