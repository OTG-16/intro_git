#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) 
{
	char nombre[100];
	
	printf("Hola mundo!\n");
	printf("Nombre: ");
	fgets(nombre, sizeof(nombre), stdin);
	printf("Hola %s\n", nombre);
	
	system("pause");	
	return 0;
}
