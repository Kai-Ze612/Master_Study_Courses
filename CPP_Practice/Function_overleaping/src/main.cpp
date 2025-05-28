#include<iostream>

// function overleaping means defining multiple functions with the same name but different parameters

void display(int a) {
    std::cout << "Integer: " << a << std::endl;
}
void display(double a) {
    std::cout << "Double: " << a << std::endl;
}
void display(std::string a) {
    std::cout << "String: " << a << std::endl;
}

// The above are funtions with the same name but different parameters

int main(){
    display(5);          // Calls the integer version
    display(3.14);       // Calls the double version
    display("Hello");     // Calls the string version
    // will call the corresponding function based on the argument type

    return 0;
}