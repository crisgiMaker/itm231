#include <iostream>
using namespace std;
int main (){
cout <<"*********************************************************************"<<endl;
cout <<"*                Bienvenido al Juego de la Adivinanza               *"<<endl;
cout <<"*********************************************************************"<<endl;

const int NUMERO_SECRETO = 42;
int adivina;

cout << "¿ cual es el numero secreto?";
cin >> adivina;
cout <<"Elvalor de su numero es;  " << adivina  <<endl;

bool acerto = adivina == NUMERO_SECRETO;
bool mayor = adivina > NUMERO_SECRETO;

	if(acerto){
		cout << "Felicitaciones!!! ... adivino el numero secreto"<<endl;
	}

	else if(mayor){
		cout << "Elnumero ingresado es mayor que el numero secreto"<<endl;
	}
	else{
		cout << "El numero ingresado es mayor que el numero secreto"<<endl;
	}
}


/*int numero_secreto = 42;
cout <<"El numero secreto es ..." <<numero_secreto <<  " No lo diga a nadie! "<<endl;

int adivina;
cout << "¿ cual es el numero secreto?";
cin >> adivina;
cout <<"Elvalor de su numero es;  " << adivina  <<endl;

if (adivina == numero_secreto){
	cout <<"Elnumero ingresado es mayor que el numero secreto"<<endl;
	}

	else if(adivina > numero_secreto){
	cout <<"el numero ingresado es mayor que el numero secreto"<<endl;
	}

	else{
	cout <<"El numero ingresado es menor que el numero secreto"<<endl;
	}
}*/

