// Use C++17 std 
#include <iostream>
#include <vector>

void BubbleSort(std::vector<int> a){
    int n = a.size();
    for (int j = 1; j < n; j++){
        for (int i = 0; i < (n-j); i++){
            if (a[i] > a[i+1]){ // Swap elements
                int t = a[i+1];
                a[i+1] = a[i];
                a[i] = t;
            }
        }
    }
}

int main(){
    std::vector<int> a = {100,99,98,97,96,10,31,5}; 

    //Bubble sort
    BubbleSort(a);


    // Print array
    for (int i =0; i < a.size(); i++){
        std::cout << a[i] << std::endl;
    }
    

    return 0;
}