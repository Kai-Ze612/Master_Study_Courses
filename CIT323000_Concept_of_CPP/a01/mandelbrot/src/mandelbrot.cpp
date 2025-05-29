#include <iostream>

void mandelbrot(double realCenter, double imagCenter, double width, double height) {
    int maxSteps = 200;
    double fontAspect = 0.4; 
    
    double pixelWidth = 200;
    double pixelHeight = 200 * height / width * fontAspect; 
    
    for (int y = 0; y < pixelHeight; ++y){
        for (int x = 0; x < pixelWidth; ++x){
            // Map pixel coordinates to the complex plane
            double real_iter = realCenter - width / 2 + x * width / pixelWidth;
            double imag_iter = imagCenter + height / 2 - y * height / pixelHeight;

            // Initialize z = 0 for the Mandelbrot iteration
            double realZ = 0.0;
            double imagZ = 0.0;
            
            int step = 0;
            
            // Mandelbrot iteration: z = z² + c
            while (step < maxSteps) {
                // Calculate |z|² = realZ² + imagZ²
                double magnitude = realZ * realZ + imagZ * imagZ;
                
                // If magnitude > 4, the point escapes
                if (magnitude > 4.0) {
                    break;
                }
                
                // Calculate new z = z² + c
                double newRealZ = realZ * realZ - imagZ * imagZ + real_iter;
                double newImagZ = 2 * realZ * imagZ + imag_iter;
                
                realZ = newRealZ;
                imagZ = newImagZ;
                step++;
            }

            // Print either '*' or ' ' based on the number of steps
            std::cout << (step == maxSteps ? '*' : ' ');
        }
        std::cout << "\n";
    }
}

// Add main function for testing
int main(){
    mandelbrot(0.01, 0.0, 3.0, 2.0);
    return 0;
}