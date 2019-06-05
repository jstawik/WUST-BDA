#include <iostream>
#include <cmath>
#include <stdlib.h>
#include <cstdio>
#include <ctime>

using namespace std;
// a new binary must be compiled for each lattice size
#define L 10
int LATTICE [L][L];
int SKIPSTEPS = 30000;
int CONFIGS = 5000;

double calculate_energy(int trial, int n1, int n2, int n3, int n4){
    return 2 * trial * (n1 + n2 + n3 + n4);
}
void print_lattice(){
    for(int i = 0; i<L; i++){
        for(int j = 0; j<L; j++){
            cout<<LATTICE[i][j]<<"\t";
        }
        cout<<"\n";
    }
}
void MCS(int steps, double T){
    int trial;
    double energy;
    double diff;
    for(int i = 0; i < steps; i++){
        for(int x = 0; x < L; x++){
            for(int y = 0; y < L; y++){
                //Single MCS
                //TRIAL ENERGY
                if(x == 0 and y ==0) energy = calculate_energy(LATTICE[x][y], LATTICE[((x+1)%L)][y]
                                                                            , LATTICE[L-1][y]
                                                                            , LATTICE[x][((y+1)%L)]
                                                                            , LATTICE[x][L-1]);
                else if(x == 0) energy = calculate_energy(LATTICE[x][y], LATTICE[((x+1)%L)][y]
                                                                       , LATTICE[L-1][y]
                                                                       , LATTICE[x][((y+1)%L)]
                                                                       , LATTICE[x][((y-1)%L)]);
                else if(y == 0) energy = calculate_energy(LATTICE[x][y], LATTICE[((x+1)%L)][y]
                                                                       , LATTICE[((x-1)%L)][y]
                                                                       , LATTICE[x][((y+1)%L)]
                                                                       , LATTICE[x][L-1]);
                else energy = calculate_energy(LATTICE[x][y], LATTICE[((x+1)%L)][y]
                                                            , LATTICE[((x-1)%L)][y]
                                                            , LATTICE[x][((y+1)%L)]
                                                            , LATTICE[x][((y-1)%L)]);
                //FLIPPING
                if(energy < 0) LATTICE[x][y] *= -1;
                else if(rand()%1000/1000.0 < exp(-energy/T)) LATTICE[x][y] = -LATTICE[x][y];
            }
        }
    }
}
double calculate_avg_energy(){
    double energy = 0;
    for(int x = 0; x < L; x++){
        for(int y = 0; y < L; y++){
            if(x == 0 and y ==0) energy -= LATTICE[x][y] * (LATTICE[((x+1)%L)][y] + LATTICE[L-1][y] + LATTICE[x][((y+1)%L)] + LATTICE[x][L-1]);
            else if(x == 0) energy -= LATTICE[x][y] * (LATTICE[((x+1)%L)][y] + LATTICE[L-1][y] + LATTICE[x][((y+1)%L)] + LATTICE[x][((y-1)%L)]);
            else if(y == 0) energy -= LATTICE[x][y] * (LATTICE[((x+1)%L)][y] + LATTICE[((x-1)%L)][y] + LATTICE[x][((y+1)%L)] + LATTICE[x][L-1]);
            else energy -= LATTICE[x][y] * (LATTICE[((x+1)%L)][y] + LATTICE[((x-1)%L)][y] + LATTICE[x][((y+1)%L)] + LATTICE[x][((y-1)%L)]);
        }
    }
    return energy/(2*pow(L, 2));
}
double calculate_avg_spin(){
    double sum = 0;
    for(int i = 0; i < L; i++)
        for(int j = 0; j< L; j++) sum += LATTICE[i][j];
    return sum/pow(L, 2);
}
double calculate_tot_mag(){
    double sum = 0;
    for(int i = 0; i < L; i++)
        for(int j = 0; j< L; j++) sum += LATTICE[i][j];
    return sum;
}

int main(int argc, char *argv[]) {
    // Temperature read & initialisation
    string arg = argv[1];
    double T = atof(arg.c_str());
    for(int i = 0; i < L; i++){
        for(int j = 0; j < L; j++) LATTICE[i][j] = 1;
    }
    srand(time(NULL));

   // Skip to stable
    MCS(SKIPSTEPS, T);
    // Calculations
    double mag = 0, mag2 = 0, magtmp = 0;
    double ener = 0, ener2 = 0, enertmp = 0;
    double binder = 0, binder2 = 0, binder4 = 0, bindertmp = 0;
    double susc = 0;
    double sheat = 0;

    for(int n = 0; n < CONFIGS; n++){
        MCS(50, T);
        magtmp = abs(calculate_avg_spin());
        mag += magtmp;
        mag2 += pow(magtmp, 2);
        enertmp = calculate_avg_energy();
        ener += enertmp;
        ener2 += pow(enertmp, 2);
        bindertmp = calculate_tot_mag();
        binder2 += pow(bindertmp, 2);
        binder4 += pow(bindertmp, 4);
    }
    mag /= CONFIGS;
    mag2 /= CONFIGS;
    ener /= CONFIGS;
    ener2 /= CONFIGS;
    binder2 /= CONFIGS;
    binder4 /= CONFIGS;
    // Thermodynamics quantities
    susc = (pow(L, 2)/T)*(mag2-pow(mag, 2));
    sheat = pow(L, 2)/pow(T, 2)*(ener2-pow(ener, 2));
    binder = 1 - (binder4/(3*pow(binder2, 2)));
    cout<<T<<", "<<mag<<", "<<ener<<", "<<susc<<", "<<sheat<<", "<<binder<<"\n";

    // print_lattice();
    /* FLIPS CODE
    for(int i = 0; i < CONFIGS; i++){
        MCS(100, T);
        cout<<avg_spin()<<"\n";
    }
    FLIPS CODE */
    return 0;
}