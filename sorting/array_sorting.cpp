// Use C++17 std 
#include <iostream>
#include <vector>

std::vector<int> BubbleSort(std::vector<int> a){
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

    return a;
}

std::vector<int> SelectionSort(std::vector<int> a){
    int n = a.size();
    int smallest_no, smallest_index;
    for (int i=0; i<(n-1); i++){
        smallest_index = i;
        smallest_no = a[smallest_index];
        // Find smallest number
        for (int j = (i+1); j<n; j++){
            if(smallest_no > a[j]){
                smallest_no = a[j];
                smallest_index = j;
            }
        }

        // Swap smallest no and i
        if (smallest_index != i){
            int temp = a[smallest_index];
            a[smallest_index] = a[i];
            a[i] = temp;
        }
    }

    return a;
}

int main(){
    std::vector<int> a = {100,99,98,97,96,10,31,5}; 

    // auto b = BubbleSort(a);
    auto b = SelectionSort(a);


    // Print array
    for (int i =0; i < b.size(); i++){
        std::cout << b[i] << std::endl;
    }
    

    return 0;
}