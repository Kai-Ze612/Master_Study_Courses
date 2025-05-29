#include<print>

// Lambda function means anonymous function
// Which is a function without a name and will be used only once, it is a simple function only for convience

int main(){

    // lambda function
    auto add = [](int a, int b){
        return a + b;   
    };

    int a = 5;
    int b = 10;
    int sum = add(a, b);
    std::println("The sum of {} and {} is {}", a, b, sum);

    // lambda function with no parameter
    auto greet = [](){
        std::println("Hello, World!");
    };
    greet();

}