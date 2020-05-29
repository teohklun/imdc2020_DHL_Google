//lab a
// teoh kah lun
// b031810069
#include <iostream>
#include <ctime>
#include <stdlib.h>
#include <stdio.h>
using namespace std;
//declare constant - problem specification, population size
const int GENE = 10; // 10 items
const int CAPACITY = 300; // weight 300
const int POP_SIZE = 10; // self declare
const int WEIGHT[GENE]={20, 15, 30, 42, 10, 5, 7, 8, 9, 13};
int chromosome[POP_SIZE][GENE]; // collection of chromosome, the population

void initializeChromosome(){
	int randNum; // local variable, because only use at this function
	//initialize random seed
	srand (time(NULL)); 
	for (int c=0; c<POP_SIZE; c++){ // loop 10 times
		for (int i=0; i<GENE; i++){ // loop 10 times
            if(i % 2 != 0){ // if item is even
			    randNum = rand() % 26; // generate number from 0 to 25
            }
            else { // if item is odd
			    randNum = rand() % 11; // generate number from 0 to 10
            }
    	    chromosome[c][i] = randNum; // add this random to put in to bag quantity to the chromosome
		}
	}
}

void printChromosome(){
	for (int c=0; c<POP_SIZE; c++){ // loop the 10 chromosme
		cout << "\tC" << c+1 << "\t";
		for (int i=0; i<GENE; i++){ // loop the chromsome 's gene to get back its value
			cout << chromosome[c][i] << " ";
		}
		cout << endl;
	}
}

int main () {
	cout <<"\nGA START! \n";
	cout <<"\nINITIALIZATION... \n";
	initializeChromosome();
	cout <<"\nPRINT INITIAL POPULATION \n";
	printChromosome();
}