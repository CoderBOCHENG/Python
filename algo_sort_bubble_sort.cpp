#include <bits/stdc++.h>
using namespace std;


void bubbleSort(int array[], int size) {

}



// print array
void printArray(int array[], int size) {
    for (int i = 0; i < size; i++) {
        cout << " " << array[i];
    }
    cout << "\n";
}


int main() {

    int data[] = {5, 8, 6, 3, 9, 2, 1, 7};

    int size = sizeof(data) / sizeof(data[0]);

    bubbleSort(data, size);

    cout << "Sorted array in ascending order: " << endl;
    printArray(data, size);


    return 0;
}
