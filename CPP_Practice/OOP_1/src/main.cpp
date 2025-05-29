#include <iostream>
#include <string>

class Robot{
    // Private define the variables that are not accessible outside the class
    private:
        std::string robot_name;
        double battery_level;

    // Public define the methods that are accessible outside the class
    public:
        // Constructor - called when object is created
        Robot(std::string& name, double default_battery = 100.0):
            robot_name(name), battery_level(default_battery) {
                std::cout << "Robot " << robot_name << " with battery level " << battery_level << " created successfully." << std::endl;
            }
        
        // Destructor - called when object is destroyed
        ~Robot() {
            std::cout << "Robot " << robot_name << " is being destroyed." << std::endl;
        }
        
        // Member function to operate computation within the class
        void movement() {
            if (battery_level > 0){
                std::cout << "Robot " << robot_name << " is moving." << std::endl;
                battery_level -= 10; // Decrease battery level by 10
            } else {
                std::cout << "Robot " << robot_name << " has no battery left to move." << std::endl;
            }
        }

        void fly(){
            if (battery_level > 20){
                std::cout << "Robot " << robot_name << " is flying." << std::endl;
                battery_level -= 20; // Decrease battery level by 20
            } else {
                std::cout << "Robot " << robot_name << " does not have enough battery to fly." << std::endl;
            }
        }

        void recharge(double amount) {
            battery_level += amount;
            std::cout << "Robot " << robot_name << " recharged. New battery level: " << battery_level << std::endl;
        }

        // Getter function - marked as const because it does not modify the object
        double getBatteryLevel() const {
            std::cout << "Getting battery level for robot " << robot_name << ": " << battery_level << std::endl;
            return battery_level;
        }

};

int main(){
    // create an object

    std::string name = "Optimus";
    double battery_level = 10;

    // Create a Robot object using the constructor
    Robot Optimus(name, battery_level);
    std::cout << name << "robot is being created with battery level: " << battery_level << std::endl;
    
    // Call the movement method
    Optimus.movement();
    // Call the fly method
    Optimus.fly();
    // Call the recharge method
    Optimus.recharge(30);

    // To get the current battery level
    double current_battery = Optimus.getBatteryLevel();

    // The destructor will be called automatically when the object goes out of scope
    // It means after the main function ends, the destructor will be called
    // The object will be destroyed and the destructor will print a message
    return 0;
}