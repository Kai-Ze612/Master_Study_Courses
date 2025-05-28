#include <print>
#include <map> // For dictionary functionality
#include <string>

int main(){
    // create a dictionary using std::map
    std::map<std::string, int> sensor_data;

    // insert some key-value pairs into the dictionary
    sensor_data["temperature"] = 25;
    sensor_data["humidity"] = 60;
    sensor_data["pressure"] = 1013;
    sensor_data["wind_speed"] = 15;

    // First, we can access individual elements
    std::println("Temperature:{}", sensor_data["temperature"]);
    std::println("Humidity:{}", sensor_data["humidity"]);
    std::println("Pressure:{}", sensor_data["pressure"]);

    
    // Second, we can iterate over the dictionary
    // We use const const auto& to avoid copying the key-value pairs, & is pointer
    // const is used to ensure that we do not modify the dictionary while iterating
    // we can also modify the values if needed, but not the keys
    for (const auto& [key, value]: sensor_data) {
        std::println("Key:{}, Value:{}", key, value);
    }

    // Third, we can check if a key exists in the dictionary
    if (sensor_data.find("wind_speed") == sensor_data.end()) {
        std::println("Wind speed data not found.");
    } else {
        std::println("Wind Speed:{}", sensor_data["wind_speed"]);
    }

    // Fourth, we can remove a key-value pair from the dictionary
    sensor_data.erase("pressure");
    std::println("After removing pressure data:");
    for (const auto& [key, value]: sensor_data) {
        std::println("Key:{}", key, ", Value:{}", value);
    }

    // Finally, we can clear the entire dictionary
    sensor_data.clear();
    std::println("Dictionary cleared. Size:{}", sensor_data.size());
    
    return 0;

}