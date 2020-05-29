// ConsoleApplication5.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <stdio.h>      /* printf, scanf, puts, NULL */
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */

using namespace std;

const int POPULATION_SIZE = 10;
const int GENE = 8;
const double TARGET = 104;
const int WEIGHT_GENE[GENE] = { 25, 35, 45, 5, 25, 3, 2, 2 };
double CHROMOSOME_FITNESS_VALUE[POPULATION_SIZE] = {};
int CHROMOSOME[POPULATION_SIZE][GENE] = {};

void initializePopulation() {
	//1. For every chromosome, c
	 //1.1 For every genes, g, in the chromosome, c
	 //1.1.1 Generate either 0 or 1
	 //1.1.2 Assign to the g of c
	srand(time(NULL));
	for (int c = 0; c < POPULATION_SIZE; c++)
	{
		int g_v = 0;
		for (int g = 0; g < GENE; g++)
		{
			/* initialize random seed: */
			g_v = rand() % 2;
			CHROMOSOME[c][g] = g_v;
		}
	}

}

void printChromosome() {
	//1. For every chromosome, c
	 //1.1 Print Chromosome number
	 //1.2 For every genes g, in the chromosome, c
	 //1.2.3 Print g of c
	for (int c = 0; c < POPULATION_SIZE; c++)
	{
		for (int g = 0; g < GENE; g++)
		{
			cout << CHROMOSOME[c][g];
		}
		cout << "\n";
	}
}

void evaluateChromosome() {
	//1. For every chromosome, c
	//1.1 set accumulatedWeight to 0
	//1.2 for every genes, g in chromosome c
	//1.2.1 If g==1, implement the multiplication and addition process
	//1.3 Print fitness value of c
	for (int c = 0; c < POPULATION_SIZE; c++)
	{
		double accumulatedWeight = 0;
		double fitnessFunction = 0;
		for (int g = 0; g < GENE; g++)
		{
			if (CHROMOSOME[c][g] == 1) {
				accumulatedWeight += WEIGHT_GENE[g];
			}
		}
		CHROMOSOME_FITNESS_VALUE[c] = fitnessFunction;
		cout << "Chromosome ";
		cout << c+1 << endl;
		cout << " accumulatedWeight = ";
		cout << accumulatedWeight << endl;
		fitnessFunction = (TARGET - accumulatedWeight) / TARGET;
		cout << " Fitness function = ";
		cout << fitnessFunction << endl;
	}
}

int main()
{
	initializePopulation();
	printChromosome();
	evaluateChromosome();
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
