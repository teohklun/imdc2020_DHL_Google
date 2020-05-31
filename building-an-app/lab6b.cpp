#include <iostream>
#include <ctime>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

// declare constant - problem specification, population size
const int GENE = 8;
const int CAPACITY = 104;
const int POP_SIZE = 10;
const int WEIGHT[GENE] = { 25, 35, 45, 5, 25, 3, 2, 2 };
const float CO_probability = 0.1; // By right, the smaller the Co_probability will triggered less chance of cross-over
const float MUT_PROBABILITY = 0.5; // Mutation chances, how big or small the chances mutation will occur
const int MAX_GENERATION = 3;

// declare chromosomes data structure
int chromosome[POP_SIZE][GENE];
int newChromosome[POP_SIZE][GENE];

// declare new chromosome counter
int newChromoCounter = 0;

// declare fitness data structure
double fitness[POP_SIZE];

// declare parents data structure
int parents[2][GENE];

// declare children data structure
int children[2][GENE];

void initializePopulation() {
	int randNum;
	//initialize random seed
	srand(time(NULL)); //SOURCE;http://www.cplusplus.com/reference/cstdlib/srand/
	for (int c = 0; c < POP_SIZE; c++) {
		for (int i = 0; i < GENE; i++) {
			randNum = rand() % 2;
			chromosome[c][i] = randNum;
		}
	}
}

void parentSelection() {
	// declare necessary variable
	int player1, player2; // for players
	int indexParents[2]; // index of selected players

	for (int i = 0; i < 2; i++) {
		// selecting 2 parents
		player1 = rand() % POP_SIZE; // this is index
		player2 = rand() % POP_SIZE; // this is index

		if (fitness[player1] <= fitness[player2])
		{
			indexParents[i] = player1;
		}
		else
		{
			indexParents[i] = player2;
		}

		cout << "\n\t Players" << player1 << "vs" << player2;
		cout << "\n\t Fitness" << fitness[player1] << "vs" << fitness[player2];
		cout << "\n\t Winner" << indexParents[i];
	}

	for (int p = 0; p < 2; p++)
	{
		cout << "\n\t parents " << p + 1 << ":";

		for (int g = 0; g < GENE; g++)
		{			
			parents[p][g] = chromosome[indexParents[p]][g];
			cout << parents[p][g] << " ";	
		}
	}
}

// One-Point CrossOver
void crossover() {

	float prob = 0.0;
	int co_point;

	// 1st Step: Copy Parents to Children 
	// For every parents p, copy it into childrens g
	for (int p = 0; p < 2; p++)
	{
		for (int g = 0; g < GENE; g++)
		{
			children[p][g] = parents[p][g];
		}
	}

	// 2nd: Generate random number form 0 to 1
	// Generate random number 0 to 1
	prob = ((rand() % 10) + 1) / 10;
	if (prob < CO_probability)
	{
		co_point = rand() % GENE;
		cout << "\n\t Children crossover at " << co_point;

		for (int g = co_point; g<GENE; g++)
		{
			children[0][g] = parents[1][g];
			children[1][g] = parents[0][g];
		}
	}
	else 
	{
		cout << "\n\t CrossOver did not happen";
	}

	
	for (int c = 0; c < 2; c++)
	{
		cout << "\n\t Children " << c + 1 << ":";
		for (int g = 0; g < GENE; g++)
		{
			cout << children[c][g] << " ";
		}
	}


}

// Mutation
void mutation() 
{
	float prob;
	int mut_point;

	for (int c = 0; c < 2; c++)
	{
		prob = (rand() % 11)/10.0; // generate the probability value

		if (prob < MUT_PROBABILITY)
		{
			// bit-flip mutation
			mut_point = rand() % GENE;
			cout << "\n\tMuatation Gene at " << mut_point;

			if (children[c][mut_point] == 0)
			{
				children[c][mut_point] = 1;
			}
			else
			{
				children[c][mut_point] = 0;
			}
		}
		else 
		{
			cout << "\n\tMutation do not occur";
		}
	}

	// Print Children
	for (int c = 0; c < 2; c++)
	{
		cout << "\n\t Children " << c + 1 << " after mutation:";
		for (int g = 0; g < GENE; g++)
		{
			cout << children[c][g] << " ";
		}
	}

}

/*
rand(): Returns a pseudo-random integral number in the range between 0 and RAND_MAX.
RAND_MAX: This value is library-dependent, but is guaranteed to be at least 32767 on any standard library implementation.
example:
v1 = rand() % 100;         // v1 in the range 0 to 99
v2 = rand() % 100 + 1;     // v2 in the range 1 to 100
v3 = rand() % 30 + 1985;   // v3 in the range 1985-2014
*/
void printChromosome() {
	for (int c = 0; c < POP_SIZE; c++) {
		cout << "\tC" << c << "\t";
		for (int i = 0; i < GENE; i++) {
			cout << chromosome[c][i] << " ";
		}
		cout << endl;
	}
}

void evaluateChromosome() {
	int accumulatedWeight = 0;
	for (int c = 0; c < POP_SIZE; c++) {
		accumulatedWeight = 0;
		for (int i = 0; i < GENE; i++) {
			if (chromosome[c][i] == 1) {
				accumulatedWeight = accumulatedWeight + WEIGHT[i];
			}
		}
		fitness[c] = abs(CAPACITY - accumulatedWeight) / (float)CAPACITY;
		cout << "\tC" << c << "\tDifference\t" << abs(CAPACITY - accumulatedWeight) << "\tFV\t" << fitness[c] << endl;
	}

}

void survivalSelection()
{
	for (int c = 0; c < 2; c++)
	{
		for (int g = 0; g < GENE; g++)
		{
			newChromosome[newChromoCounter][g] = children[c][g];
		}

		newChromoCounter++;
	}

	for (int c = 0; c < newChromoCounter; c++)
	{
		cout << "\tNew chromosome " << c << ": ";
		for (int g = 0; g < GENE; g++)
		{
			cout << " " << newChromosome[c][g];
		}
		cout << "\n";
	}
}

void copyChromosome()
{
	for (int c = 0; c < POP_SIZE; c++)
	{
		for (int g = 0; g < GENE; g++)
		{
			chromosome[c][g] = newChromosome[c][g];
		}
	}
}

int main() {
	cout << "\nGA START! \n";
	cout << "First generation \n\n";
	cout << "\nINITIALIZATION... \n";

	//LAB 3
	initializePopulation();
	getchar();

	for (int g=0;g<MAX_GENERATION;g++)
	{
		cout << "GENERATION" << g + 1 << endl;
		cout << "\nPRINT POPULATION \n";
		//LAB 3
		printChromosome();
		getchar();

		//LAB 4
		cout << "\nEVALUATE CHROMOSOME \n";
		evaluateChromosome();
		getchar();
		
		newChromoCounter = 0;

		for (int i = 0; i < POP_SIZE/2; i++)
		{
			// LAB 5a
			cout << "\nPARENT SELECTION \n";
			parentSelection();

			// LAB 5b
			cout << "\nCROSS-OVER SELECTION \n";
			crossover();

			// LAB 6
			cout << "\nMUTATION \n";
			mutation();

			// LAB 7
			cout << "\nSURVIVAL SELECTION \n";
			survivalSelection();
		}

		cout << "\nNEW CHROMOSOME COPIED to CHROMOSOME";
		copyChromosome();
		getchar();
	}

}