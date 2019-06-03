#include <iostream>
#include <cmath>
#include <stdlib.h>
#include <cstdio>
#include <ctime>

using namespace std;

#define L 100
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
double avg_spin(){
    double sum = 0;
    for(int i = 0; i < L; i++)
        for(int j = 0; j< L; j++) sum += LATTICE[i][j];
    return sum/pow(L, 2);
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
    double magtmp = 0;
    double mag = 0;
    double mag2 = 0;
    double ener = 0;
    double ener2 = 0;
    double enertmp = 0;
    double binder2 = 0;
    double binder4 = 0;
    double bindertmp = 0;


    for(int n = 0; n < CONFIGS; n++){
        MCS(50, T);
        magtmp = abs(avg_spin());
        mag += magtmp;
        mag2 += pow(magtmp, 2);

        for(int x = 0; x < L; x++)
            for(int y = 0; y < L; y++){
                if(x == 0 and y ==0) enertmp = calculate_energy(LATTICE[x][y], LATTICE[((x+1)%L)][y]
                            , LATTICE[L-1][y]
                            , LATTICE[x][((y+1)%L)]
                            , LATTICE[x][L-1]);
                else if(x == 0) enertmp = calculate_energy(LATTICE[x][y], LATTICE[((x+1)%L)][y]
                            , LATTICE[L-1][y]
                            , LATTICE[x][((y+1)%L)]
                            , LATTICE[x][((y-1)%L)]);
                else if(y == 0) enertmp = calculate_energy(LATTICE[x][y], LATTICE[((x+1)%L)][y]
                            , LATTICE[((x-1)%L)][y]
                            , LATTICE[x][((y+1)%L)]
                            , LATTICE[x][L-1]);
                else enertmp = calculate_energy(LATTICE[x][y], LATTICE[((x+1)%L)][y]
                            , LATTICE[((x-1)%L)][y]
                            , LATTICE[x][((y+1)%L)]
                            , LATTICE[x][((y-1)%L)]);
                bindertmp += LATTICE[x][y];
            }
        ener -= enertmp/4;
        ener2 += pow(enertmp, 2)/4;
        binder2 += pow(bindertmp, 2);
        binder4 += pow(bindertmp, 4);
    }
    mag /= CONFIGS;
    double sus = CONFIGS*(mag2/CONFIGS-pow(mag, 2))/T;
    ener /= CONFIGS;
    double sheat = (ener2/CONFIGS-pow(ener, 2))/pow(T, 2);
    double binder = 1- ((binder4/CONFIGS)/(3*pow(binder2/CONFIGS, 2)));
    cout<<T<<", "<<mag<<", "<<ener<<", "<<sus<<", "<<sheat<<", "<<binder<<"\n";

    // print_lattice();
    /* FLIPS CODE
    for(int i = 0; i < CONFIGS; i++){
        MCS(100, T);
        cout<<avg_spin()<<"\n";
    }
    FLIPS CODE */
    return 0;

}