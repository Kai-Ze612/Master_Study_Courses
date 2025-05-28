#include <iostream>

int add(int x, int y){
    return x + y;
}

int multiply(int x, int y){
    return x * y;
}

int main(){
    int a;
    int b;
    std::cout <<"Please enter two integers:";
    std::cin >> a >> b ;
    std::cout << "You entered: " << a << " and " << b << std::endl;
    std::cout << "The sum of " << a << " and " << b << " is: " << add(a, b) << std::endl;
    std::cout << "The product of " << a << " and " << b << " is: " << multiply(a, b) << std::endl;
    return 0;
}