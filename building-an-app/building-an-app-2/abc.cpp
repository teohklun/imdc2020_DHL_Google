#include <iostream>
#include <ctime>
#include <stdlib.h>
#include <stdio.h>
#include <fstream>
using namespace std;
//declare constant - problem specification, population size
const int GENE = 8;
const int CAPACITY = 104;
const int POP_SIZE = 30;
const int WEIGHT[GENE] = { 25, 35, 45, 5, 25, 3, 2, 2 };
const float CO_probability = 0.9;
const float MUT_PROBABILITY = 0.9;
const int MAX_GENERATION = 10;

double bestFitness = 99.9;
double avgFitness = 0.0;
int bestChromosome[GENE];

ofstream bestFitnessFile, avgFitnessFile, bestChromosomeFile;


//declare chromosomes data structure
int chromosome[POP_SIZE][GENE];
//declare fitness data structure
double fitness[POP_SIZE];
//declare parents data structure
int parents[2][GENE];
//declare children data structure
int children[2][GENE];
//declare chromosomes data structure = buffer
int newChromosome[POP_SIZE][GENE];
//declare the new hromosome counter
int newChromoCounter=0;

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
void parentSelection() {
	int player1, player2;//for players
	int indexParents[2];//index of selected players

	do {
		for (int i = 0; i < 2; i++) {

			do {
				player1 = rand() % POP_SIZE;
				player2 = rand() % POP_SIZE;
			} while (player1 == player2);

			cout << "Round" << i << "Player1:" << player1 << endl;
			cout << "Round" << i << "Player2:" << player2 << endl;

			if (fitness[player1] <= fitness[player2])
			{
				indexParents[i] = player1;
			}
			else
			{
				indexParents[i] = player2;
			}
			cout << "Winner Chromosome: Chromosome " << indexParents[i] << " " << fitness[indexParents[i]] << endl << endl;
		}
	} while (indexParents[0] == indexParents[1]);


	for (int p = 0; p < 2; p++)
	{
		cout << "Parents" << p + 1;
		for (int g = 0; g < GENE; g++)
		{
			parents[p][g] = chromosome[indexParents[p]][g];
			cout << " " << parents[p][g];
		}
		cout << endl;
	}
}
void crossover() {
	float prob = 0;
	int co_point;

	for (int p = 0; p < 2; p++)
	{
		for (int g = 0; g < GENE; g++)
		{
			children[p][g] = parents[p][g];
		}
	}
	prob = ((rand() % 10) + 1) / 10.0;

	if (prob < CO_probability) {
		co_point = rand() % GENE;
		cout << "\nChildren crossover at =" << co_point;

		for (int g = co_point; g < GENE; g++)
		{
			children[0][g] = parents[1][g];
			children[1][g] = parents[0][g];
		}
	}
	else {
		cout << "\nCrossover did not happen ";
	}

	for (int c = 0; c < 2; c++)
	{
		cout << "\nChildren" << c + 1 << ": ";
		for (int g = 0; g < GENE; g++)
		{
			cout << children[c][g] << " ";
		}
		cout << endl;
	}
}
void mutation() {
	float prob;
	int mut_point;
	for (int c = 0; c < 2; c++) {
		prob = (rand() % 11) / 10.0;
		if (prob < MUT_PROBABILITY) {
			mut_point = rand() % GENE;
			cout << "Mutation at gene " << mut_point << endl;
			if (children[c][mut_point] == 1)
				children[c][mut_point] = 0;
			else
				children[c][mut_point] = 1;
		}
		else
			cout << "\nMutation did not happen.\n";
	}
	for (int c = 0; c < 2; c++)
	{
		cout << "\nChildren" << c + 1 << "after mutation: ";
		for (int g = 0; g < GENE; g++)
		{
			cout << children[c][g] << " ";
		}
		cout << endl;
	}
}
void survivalSelection() {
	for (int c = 0; c < 2; c++) {//copy children to newChromosome
		for (int g = 0; g < GENE; g++) {
			newChromosome[newChromoCounter][g] = children[c][g];
		}
		newChromoCounter++;
	}
	for (int c = 0; c < newChromoCounter; c++)
	{
		cout << "\nNew Chromosome " << c << ": ";
		for (int g = 0; g < GENE; g++)
		{
			cout << newChromosome[c][g] << " ";
		}
	}
}
void copyChromosome() {
	for (int c = 0; c < POP_SIZE; c++) {
		for (int g = 0; g < GENE; g++) {
			chromosome[c][g] = newChromosome[c][g];
		}
	}
}
void recordBestFitness() {
	for (int c = 0; c < POP_SIZE; c++) {
		if (bestFitness > fitness[c]) {
			bestFitness = fitness[c];
			for (int g = 0; g < GENE; g++) {
				bestChromosome[g] = chromosome[c][g];
			}//close for gene
		}//close for if
	}//close for c

	//output for the best chromosome to monitor
	cout << "\n Best Fitness = " << bestFitness;
	cout << "\n Best Chromosome = ";
	for (int g = 0; g < GENE; g++) {
		cout << bestChromosome[g];
	}
	cout << endl;

	//output for the file
	bestFitnessFile << bestFitness << endl;
	for (int g = 0; g < GENE; g++) {
		bestChromosomeFile << bestChromosome[g];
	}
	bestChromosomeFile << endl;
}
void calcAvgFitness() {
	double sum = 0;
	for (int c = 0; c < POP_SIZE; c++) {
		sum += fitness[c];
	}
	avgFitness = sum / POP_SIZE;

	//output to monitor
	cout << "\n Average Fitness = " << avgFitness << endl;
	
	//output to file
	avgFitnessFile << avgFitness << endl;

}

int main() {
	bestFitnessFile.open("bestFitness.txt");
	avgFitnessFile.open("avgFitness.txt");
	bestChromosomeFile.open("bestChromosome.txt");
	cout << "\nGA START! \n";
	cout << "First generation \n\n";
	cout << "\nINITIALIZATION... \n";
	//LAB 3
	initializePopulation();
	//getchar();
	//LAB 3
	for (int g = 0; g < MAX_GENERATION; g++) {//start of generation
		cout << "\n GENERATION" << g + 1 << endl;
		cout << "\nPRINT POPULATION \n";
		printChromosome();
		//LAB 4
		cout << "\nEVALUATE CHROMOSOME \n";
		evaluateChromosome();
		recordBestFitness();
		calcAvgFitness();
		//getchar();
		newChromoCounter = 0;
		for (int i = 0; i < POP_SIZE / 2; i++) {
			cout << "\nPARENT SELECTION \n";
			parentSelection();
			cout << "\nCROSSOVER \n";
			crossover();
			cout << "\nMUTATION \n";
			mutation();
			cout << "\nSURVIVAL SELECTION \n";
			survivalSelection();
		}
		cout << "\nNEW CHROMOSOMES COPIED TO CHROMOSOME\n";
		copyChromosome();
		//getchar();
	}
	bestFitnessFile.close();
	avgFitnessFile.close();
	bestChromosomeFile.close();
}