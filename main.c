#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) 
{
	char nombre[100];
	unsigned int edad;
	
	printf("Hola mundo!\n");
	printf("Nombre: ");
	fgets(nombre, sizeof(nombre), stdin);
	printf("Hola %s", nombre);
	printf("Edad: ");
	scanf("%u", &edad);
	printf("Vas a cumplir %u\n", edad + 1);
	
	system("pause");	
	return 0;
}
