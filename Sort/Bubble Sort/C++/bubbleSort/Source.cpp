#include <iostream>
#include <string>


using namespace std;


int readInt(const char* msn) {
	int number;
	while (true) {
		try {
			cout << msn;
			if (!(cin >> number)) {
				throw invalid_argument("Please enter proper interger");
			}
			return number;
		}
		catch (invalid_argument e) {
			cout << "INVALID ARGUMENT CATCHED: " << e.what() << endl;
			cin.clear();
			cin.ignore(std::numeric_limits <std::streamsize>::max(), '\n');
		}
	}
	cout << "Returning ErrorValue: -100" << endl;
	return -100;
}


void addNumber(int intArray[]) {
	int i;
	for (i = 0; i <= sizeof(intArray); i++) {
		if (intArray[i] == NULL) {
			string str = "Type a number to add it in the position a[" + to_string(i) + "]: ";
			intArray[i] = readInt(str.c_str());
			break;
		}
	}
	if (i > sizeof(intArray)) {
		cerr << "Error: Out of bounds" << endl;
	}
}


void printArray(int intArray[]) {
	for (int i = 0; i <= sizeof(intArray); i++) {
		cout << "a[" << i << "] = " << intArray[i] << endl;
	}
}


void changePosition(int intArray[],int a, int b) {
	int aux = intArray[a];
	intArray[a] = intArray[b];
	intArray[b] = aux;
}


void creacentWayBubbleSort(int intArray[]) {
	for (int i = 0; i < sizeof(intArray);i++) {
		for (int j = 0; j < (sizeof(intArray)-i); j++) {
			if (intArray[j] > intArray[j+1]) {
				changePosition(intArray, (j), (j+1));
			}
		}
	}
}


void decreacentWayBubbleSort(int intArray[]) {
	for (int i = 0; i < sizeof(intArray);i++) {
		for (int j = 0; j < (sizeof(intArray) - i); j++) {
			if (intArray[j] < intArray[j + 1]) {
				changePosition(intArray, (j), (j + 1));
			}
		}
	}
}


void run() {
	cout << "Welcome to the program that applies the bubble sort in the c++ lenguage..." << endl;

	const int numbers = readInt("How many numbers do you want to evaluate?: ");
	int intArray[5]{ NULL };
	cout << "filling the array" << endl;
	for (int i = 0;i < 5; i++) {
		addNumber(intArray);
	}

	cout << "Type:\n1) If you want to sort the array in creacent way" << endl;
	cout << "2) If you want to sort the array in decreacent way" << endl;
	int opc = readInt("Ans: ");
	if (opc == 1) {
		cout << "Original" << endl;
		printArray(intArray);
		creacentWayBubbleSort(intArray);
		cout << "Creacent" << endl;
		printArray(intArray);
	}
	if (opc == 2) {
		cout << "Original" << endl;
		printArray(intArray);
		decreacentWayBubbleSort(intArray);
		cout << "Decreacent" << endl;
		printArray(intArray);
	}
}


int main(int args, char* argsv[]) {
	run();
	return 0;
}