#include <stdio.h>
#include <stdint.h>

int main(int argc, char *argv[]){

	// Code adapted from the tutorial on Moodle
	// https://web.microsoftstream.com/video/dfdc58cb-da0c-411b-a9d7-b1199252c312?referrer=https:%2F%2Flearnonline.gmit.ie%2Fcourse%2Fview.php%3Fid%3D135

	FILE *f = fopen("../MNIST_Images/t10k-images-idx3-ubyte", "rb");
	
	// Ensures that b will only have 8 bits.
	uint8_t b;
	
	int i, j, k;

	// Print out the first 20 bytes of the file
	for (i = 0; i < 20; i++){
		fread(&b, 1, 1, f);
		printf("%02x ", b);
	}
	printf("\n");

	// Print out a visual representation of the first three images (7)
	for (k = 0; k < 3; k++){
		for (i = 0; i < 28; i++){
			for (j = 0; j < 28; j++){
				fread(&b, 1, 1, f);
				printf("%s", (b > 127) ? "0" : ".");
			}
			printf("\n");
		}
	}

	printf("\n");


	return 0;
}
