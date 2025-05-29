#include <print>
#include <tuple>
#include <string>

// The difference between tuple and dictionary:
// A tuple is a fixed-size collection of elements, where each element can be of a different type.
// A dictionary (or map) is a collection of key-value pairs, where each key is unique and maps to a value.
// A tuple is typically used for grouping related data, while a dictionary is used for fast lookups based on keys.

// The difference between std::tuple and std::pair:
// std::tuple can hold an arbitrary number of elements of different types, while std::pair is specifically designed to hold exactly two elements.

int main() {
    std::pair<std::string, int> persion_info{"Alice", 30};

    std::println("Name: {}, Age: {}", persion_info.first, persion_info.second);

    std::tuple<std::string, int, double> person_info{"Bob", 25, 5.9};
    std::println("Name: {}, Age: {}, Height: {}", 
                 std::get<0>(person_info),  // use to get the elements of the tuple
                 std::get<1>(person_info),  
                 std::get<2>(person_info));

    // More modern way to access

    auto [name, age, height] = person_info;  // structured binding
    std::println("Name: {}, Age: {}, Height: {}", name, age, height);

    
    return 0;
}