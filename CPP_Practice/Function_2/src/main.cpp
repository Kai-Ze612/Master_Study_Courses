#include<iostream>

std::string name(std::string first_name, std::string last_name){
    std::string full_name = first_name + "," + last_name;
    return full_name;
}

int main(){
    std::string first_name;
    std::string last_name;

    std::cout <<"please enter your first name:";
    std::cin >> first_name;

    std::cout <<"please enter your last name:";
    std::cin >> last_name;

    std::string full_name = name(first_name, last_name);

    std::cout << "Your full name is: " << full_name << std::endl;

    return 0;
}