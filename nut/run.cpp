#include "algorithm.h"
#include <string.h>
#include <iostream>
#include <fstream>
#include <ctime>
#include <unistd.h>
#include <stdio.h>

using namespace std;

int main(){
    // Time
    int c[] = {0,1,2,6,24,120,720,5040,40320,362800,3628000};
    int time = 0;
    int length = 4;
    clock_t start;
    double duration;
    int num = 0;
    Permutation P = Permutation(length);
    start = clock();
    char* p = "";
    while(num < c[length]){
        p = P.pNext();
        
        if (num == c[length] / 2){
            char cmd[30];
            pid_t pid = getpid();
            sprintf(cmd, "vmmap %d > temp", (int)pid);
            cout << cmd << endl;
            system(cmd);
        }
        
        num = num + 1;
    }
    duration = (clock() - start) / (double) CLOCKS_PER_SEC;
    time = (int) (1000000 * duration);

    string line, later, far;
    ifstream fin("temp");
    while( getline(fin, far)){
        line = later;
        later = far;
    }
    string line1 = line.substr(0, line.rfind("K"));
    string space = line1.substr(line1.rfind(" ")+1, line1.length());


    ofstream fout("evaluate");
    fout << time << "," << space << "," << endl;

    return 0;
}
