#include <iostream>
#include <cmath>
#include <stdlib.h>
#include <cstdio>
#include <ctime>

#define PI 3.14159265


using namespace std;

double calculate_energy(int trial, int n1, int n2, int n3, int n4){
    return  -1.5*(pow(cos(PI*(trial-n1)/180), 2)
                 +pow(cos(PI*(trial-n2)/180), 2)
                 +pow(cos(PI*(trial-n3)/180), 2)
                 +pow(cos(PI*(trial-n4)/180), 2))+2;
}

int main(int argc, char *argv[]) {
    // Inputs
    string arg = argv[1];
    size_t pos;
    int L = stoi(arg, &pos);
    cout<<"L: "<<L;
    arg = argv[2];
    int steps = stoi(arg, &pos);
    cout<<" steps: "<<steps;
    arg = argv[3];
    double T = atof(arg.c_str());
    cout<<" Temp: "<<T;
    arg = argv[4];
    int delta = stoi(arg, &pos);
    cout<<" delta: "<<delta<<"\n";
    // Initialisation
    int lattice[L][L];
    for(int i = 0; i < L; i++){
        for(int j = 0; j < L; j++) lattice[i][j] = 0;
    }
    srand(time(NULL));
    // MCSes
    int trial;
    double energy;
    double energy0 = 0;
    double diff;
    for(int i = 0; i < steps; i++){
        for(int x = 0; x < L; x++){
            for(int y = 0; y < L; y++){
                //Single MCS
                //CURRENT ENERGY
                if(x == 0 and y ==0) energy0 = calculate_energy(lattice[x][y], lattice[((x+1)%L)][y]
                                                                             , lattice[L-1][y]
                                                                             , lattice[x][((y+1)%L)]
                                                                             , lattice[x][L-1]);
                else if(x == 0) energy0 = calculate_energy(lattice[x][y], lattice[((x+1)%L)][y]
                                                                        , lattice[L-1][y]
                                                                        , lattice[x][((y+1)%L)]
                                                                        , lattice[x][((y-1)%L)]);
                else if(y == 0) energy0 = calculate_energy(lattice[x][y], lattice[((x+1)%L)][y]
                                                                        , lattice[((x-1)%L)][y]
                                                                        , lattice[x][((y+1)%L)]
                                                                        , lattice[x][L-1]);
                else energy0 = calculate_energy(lattice[x][y], lattice[((x+1)%L)][y]
                                                             , lattice[((x-1)%L)][y]
                                                             , lattice[x][((y+1)%L)]
                                                             , lattice[x][((y-1)%L)]);
                //TRIAL ENERGY
                trial = lattice[x][y] + round((rand()%1000/1000.0-0.5)*delta);
                if(trial < -90) trial += 180;
                if(trial > 90) trial -= 180;
                if(x == 0 and y ==0) energy = calculate_energy(trial, lattice[((x+1)%L)][y]
                                                                    , lattice[L-1][y]
                                                                    , lattice[x][((y+1)%L)]
                                                                    , lattice[x][L-1]);
                else if(x == 0) energy = calculate_energy(trial, lattice[((x+1)%L)][y]
                                                               , lattice[L-1][y]
                                                               , lattice[x][((y+1)%L)]
                                                               , lattice[x][((y-1)%L)]);
                else if(y == 0) energy = calculate_energy(trial, lattice[((x+1)%L)][y]
                                                               , lattice[((x-1)%L)][y]
                                                               , lattice[x][((y+1)%L)]
                                                               , lattice[x][L-1]);
                else energy = calculate_energy(trial, lattice[((x+1)%L)][y]
                                                    , lattice[((x-1)%L)][y]
                                                    , lattice[x][((y+1)%L)]
                                                    , lattice[x][((y-1)%L)]);
                //FLIPPING
                diff = energy - energy0;
                if(diff < 0) lattice[x][y] = trial;
                else if(rand()%1000/1000.0 < exp(-diff/T)) lattice[x][y] = trial;
            }
        }
    }
    energy = 0;
    for(int x = 0; x < L; x++){
        for(int y = 0; y < L; y++){
            if(x == 0 and y ==0) energy += calculate_energy(lattice[x][y], lattice[((x+1)%L)][y]
                        , lattice[L-1][y]
                        , lattice[x][((y+1)%L)]
                        , lattice[x][L-1]);
            else if(x == 0) energy += calculate_energy(lattice[x][y], lattice[((x+1)%L)][y]
                        , lattice[L-1][y]
                        , lattice[x][((y+1)%L)]
                        , lattice[x][((y-1)%L)]);
            else if(y == 0) energy += calculate_energy(lattice[x][y], lattice[((x+1)%L)][y]
                        , lattice[((x-1)%L)][y]
                        , lattice[x][((y+1)%L)]
                        , lattice[x][L-1]);
            else energy += calculate_energy(lattice[x][y], lattice[((x+1)%L)][y]
                        , lattice[((x-1)%L)][y]
                        , lattice[x][((y+1)%L)]
                        , lattice[x][((y-1)%L)]);
        }

    }
    cout<<energy/(L*L);
    return 0;
}