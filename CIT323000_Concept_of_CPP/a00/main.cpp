#include <print>

int main(int argc, char** argv) {
    if (argc > 1) {
        std::println("Hello {}!", argv[1]);
    } else {
        std::println("Hello World!");
    }
    return 0;
}
