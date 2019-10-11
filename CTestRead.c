#include <stdio.h>

int main(int argc, char *argv[]){


	FILE *f = fopen("MNIST_Images/t10k-images-idx3-ubyte", "rb");
	int b;

	for (int i = 0; i < 20; i++){
		fread(&b, 1, 1, f);
		printf("%02x", b);
	}

	return 0;

}
