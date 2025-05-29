#include<print>
#include<array>
#include<vector>

int main(){
    // Array is fixed size
    std::array<int, 5> arr = {1, 2, 3, 4, 5};

    // vector is dynamic size
    std::vector<int> vec = {1, 2, 3, 4, 5};

    // add an element in the end of the vector
    vec.push_back(6);
    vec.push_back(7);
    // remove the last element of the vector
    vec.pop_back();
    // print the vector
    std::print("Vector: ");
    for (const auto& i : vec) {
        std::print("{} ", i);
    }
    std::print("\n");

    // print the array
    std::print("Array: ");
    for (const auto& i : arr) {
        std::print("{} ", i);
    }
    std::print("\n");

    // get the size of the array
    std::print("Size of array: {}\n", arr.size());

    // get the size of the vector
    std::print("Size of vector: {}\n", vec.size());

    // get the first element of the array
    std::print("First element of array: {}\n", arr[0]);
    // get the first element of the vector
    std::print("First element of vector: {}\n", vec[0]);
    // get the last element of the array
    std::print("Last element of array: {}\n", arr[arr.size() - 1]);
    // get the last element of the vector
    std::print("Last element of vector: {}\n", vec[vec.size() - 1]);

    return 0;
}