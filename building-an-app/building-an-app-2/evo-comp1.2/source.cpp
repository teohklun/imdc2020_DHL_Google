#include <iostream>
#include <ctime>
#include <stdlib.h>
#include <stdio.h>
#include <fstream>
#include <time.h>
#include <sstream>

using namespace std;
//declare constant - problem specification, population size

const int HUMANSIZE = 60;
const int GENE = HUMANSIZE * 2;

//gene after add human and luggage

// 60 person // website show 62

// aeroplane payload weight 5XXX kg after reduce pilot etc.
const int CAPACITY = 5000;
const int CAPACITYH = 4000;
const int CAPACITYL= 1000;

const int POP_SIZE = 30; // two version

const float CO_probability = 0.9; // two version, this 0.9 
const float MUT_PROBABILITY = 0.15 ; // two version, this 0.15
const int MAX_GENERATION = 10; // roughly stable ()
// const double thresholdStop = 0.00001; 
// not important anymore, because evaluate performance measure with fitnessvalue, not solution found within X times of run
// so set 0.00001 from 0.15

const int SEAT_OCCUPIED_CHANCE = 50;
const int intToRunSametimes = 3;
double bestFitness = 99.9;
double avgFitness = 0.0;
int bestChromosome[GENE];

const int minHumanWeight = 20;
const int maxHumanWeight = 100; // to make 20 - 120

const int minLuggageWeight = 5;
const int maxLuggageWeight = 25; // to make 5 - 30

const double weightChromosomeH = 0.75; // 6/7
const double weightChromosomeL = 0.25; // 1/7

string filePrefix = "0.8";

ofstream bestFitnessFile, avgFitnessFile, bestChromosomeFile, timeExecutionFile, parameterFile;

//declare chromosomes human data structure
int chromosomeH[POP_SIZE][GENE];

//declare chromosomes luggage data structure
int chromosomeL[POP_SIZE][GENE];

int chromosome[POP_SIZE][GENE * 2];

//declare fitness data structure
double fitness[POP_SIZE];
//declare parents data structure
int parents[2][GENE];
//declare children data structure
int children[2][GENE];
//declare chromosomes data structure = buffer
int newChromosome[POP_SIZE][GENE];
//declare the new hromosome counter
int newChromoCounter = 0;

void initializePopulation() {

	ifstream file("initiazeChromosome.txt");
	if (!file) // if no file, create new
	{
		int randNum;
		//initialize random seed
		srand(time(NULL)); //SOURCE;http://www.cplusplus.com/reference/cstdlib/srand/
		for (int c = 0; c < POP_SIZE; c++) {
			for (int i = 0; i < HUMANSIZE; i++) {
				randNum = rand() % 99;
				if (randNum >= SEAT_OCCUPIED_CHANCE) { // 50% a seat does not have occupy
					randNum = rand() % maxHumanWeight + minHumanWeight;
					chromosome[c][i] = randNum;
					randNum = rand() % maxLuggageWeight + minLuggageWeight;
					chromosome[c][HUMANSIZE + i] = randNum;

				}
				else {
					chromosome[c][i] = 0;

					chromosome[c][HUMANSIZE + i] = 0;
				}
			}
		}

		ofstream file;
		//write file
		file.open("initiazeChromosome.txt");
		for (int c = 0; c < POP_SIZE; c++) {
			for (int i = 0; i < GENE; i++) {
				file << chromosome[c][i] << " ";
			}
			file << endl;
		}
		file.close();
	} else {

		//read file
		std::string tmp_gene;

		string line;
		string delimiter = " ";
		int counter = 0 ;
		while (getline(file, line)) { // read line
			int index = 0;
			istringstream ss(line);
			string token;

			while(std::getline(ss, token, ' ')) { // read every string in the line
				chromosome[counter][index] = stoi(token);
				index ++;
			}
			counter++;
		}
		file.close();
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
	cout << "\nPRINT POPULATION HUMAN \n";
	for (int c = 0; c < POP_SIZE; c++) {
		cout << "\tC" << c << "\t";
		for (int i = 0; i < GENE; i++) {
			cout << chromosome[c][i] << " ";
		}
		cout << endl;
	}

}

void evaluateChromosome() {
	int accumulatedHWeight = 0;
	int accumulatedLWeight = 0;

	double fitnessH = 0;
	double fitnessL = 0;

	for (int c = 0; c < POP_SIZE; c++) {
		accumulatedHWeight = 0;
		accumulatedLWeight = 0;
		for (int i = 0; i < HUMANSIZE; i++) {
			if (chromosome[c][i] != 0) {
				// accumulatedWeight = accumulatedWeight + WEIGHT[i];
				accumulatedHWeight = accumulatedHWeight + chromosome[c][i];
				accumulatedLWeight = accumulatedLWeight + chromosome[c][i + HUMANSIZE];
			}
		}

		fitnessH = (abs(CAPACITYH - accumulatedHWeight) / (float)CAPACITYH) * weightChromosomeH;
		fitnessL = (abs(CAPACITYL - accumulatedLWeight) / (float)CAPACITYL) * weightChromosomeL;

		fitness[c] = fitnessH + fitnessL;

		cout << "\tC" << c << "\tDifference\t" << abs(CAPACITY - accumulatedHWeight - accumulatedLWeight) << "\tFV\t" << fitness[c] << endl;

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
		co_point = rand() % HUMANSIZE;
		cout << "\nChildren crossover at =" << co_point;

		for (int g = co_point; g < HUMANSIZE; g++)
		{
			children[0][g] = parents[1][g];
			children[1][g] = parents[0][g];

			children[0][g + HUMANSIZE] = parents[1][g + HUMANSIZE];
			children[1][g + HUMANSIZE] = parents[0][g + HUMANSIZE];

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
	int mut_point, gotCustomer, randomMutate;
	for (int c = 0; c < 2; c++) {
		prob = (rand() % 11) / 10.0;
		if (prob < MUT_PROBABILITY) {
			mut_point = rand() % GENE;
			cout << "Mutation at gene " << mut_point << endl;

			//modify here
			gotCustomer = rand() % 99;
			if (gotCustomer >= SEAT_OCCUPIED_CHANCE) {
				if (mut_point > HUMANSIZE) {
					randomMutate = rand() % maxLuggageWeight + minLuggageWeight;
					children[c][mut_point] = randomMutate; // luggage got weight mean sure got customer at that seat
				}
				else {
					randomMutate = rand() % maxHumanWeight + minHumanWeight;
					children[c][mut_point] = randomMutate;
					randomMutate = rand() % maxLuggageWeight + minLuggageWeight;
					children[c][mut_point + HUMANSIZE] = randomMutate; // luggage got weight mean sure got customer at that seat
				}
			}
			else {

				if (mut_point > HUMANSIZE) {
					children[c][mut_point] = 0;
				}
				else {
					// if customer empty, luggage should empty
					children[c][mut_point + HUMANSIZE] = 0;
					children[c][mut_point] = 0;
				}

			}
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
		cout << bestChromosome[g] << " ";
	}
	cout << endl;

	//output for the file
	bestFitnessFile << bestFitness << endl ;
	for (int g = 0; g < GENE; g++) {
		bestChromosomeFile << bestChromosome[g] << " ";
	}
	// bestChromosomeFile << endl;
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
	// avgFitnessFile << avgFitness << endl;
	avgFitnessFile << avgFitness << endl;


}

void runEvoProgram() {
	bestFitnessFile.open("bestFitness" + filePrefix + ".txt", fstream::app);
	avgFitnessFile.open("avgFitness" + filePrefix + ".txt", fstream::app);
	bestChromosomeFile.open("bestChromosome" + filePrefix + ".txt", fstream::app);
	cout << "\nGA START! \n";
	cout << "First generation \n\n";
	cout << "\nINITIALIZATION... \n";
	initializePopulation();

	// for (int g = 0; g < MAX_GENERATION; g++) {//start of generation
	for (int g = 0; g < MAX_GENERATION; g++) {//start of generation

		cout << "\n GENERATION" << g + 1 << endl;
		cout << "\nPRINT POPULATION \n";
		printChromosome();
		//LAB 4
		cout << "\nEVALUATE CHROMOSOME \n";
		evaluateChromosome();
		recordBestFitness();
		calcAvgFitness();

		// if (avgFitness < thresholdStop && avgFitness > 0) {
		// 	break;
		// } removed not planning to judge it

		// getchar();
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
	}
	bestFitnessFile << endl;
	bestFitnessFile.close();
	avgFitnessFile << endl;
	avgFitnessFile.close();
	bestChromosomeFile << endl;
	bestChromosomeFile.close();

}

void writeParameterFile() {
	parameterFile.open("paramUsed" + filePrefix + ".txt");
	parameterFile << "HUMANSIZE : " << HUMANSIZE << endl;
	parameterFile << "GENE : " << GENE << endl;
	parameterFile << "CAPACITY : " << CAPACITY << endl;
	parameterFile << "POP_SIZE : " << POP_SIZE << endl;
	parameterFile << "CO_probability : " << CO_probability << endl;
	parameterFile << "MUT_PROBABILITY : " << MUT_PROBABILITY << endl;
	parameterFile << "MAX_GENERATION : " << MAX_GENERATION << endl;
	// parameterFile << "thresholdStop : " << thresholdStop << endl;
	parameterFile << "SEAT_OCCUPIED_CHANCE : " << SEAT_OCCUPIED_CHANCE << endl;
	parameterFile << "minHumanWeight : " << minHumanWeight << endl;
	parameterFile << "maxHumanWeight : " << maxHumanWeight << endl;
	parameterFile << "minLuggageWeight : " << minLuggageWeight << endl;
	parameterFile << "maxLuggageWeight : " << maxLuggageWeight << endl;
	parameterFile << "weightChromosomeH : " << weightChromosomeH << endl;
	parameterFile << "weightChromosomeL : " << weightChromosomeL << endl;
	parameterFile.close();
}

int main() {

	for (int i = 0; i < intToRunSametimes; i++) // do same run x times so later can calculate average
	{
		time_t begin, end;
		ifstream my_file("paramUsed" + filePrefix + ".txt");
		if (!my_file)
		{
			writeParameterFile();
		}
		time(&begin);
		runEvoProgram();
		time(&end);
		time_t elapsed = end - begin;

		cout << "\nTime measured: " << elapsed << " seconds.\n";
		timeExecutionFile.open("timeExecution" + filePrefix + ".txt", fstream::app);
		timeExecutionFile << elapsed << endl;
		timeExecutionFile.close();
	}
	return 0;
}
