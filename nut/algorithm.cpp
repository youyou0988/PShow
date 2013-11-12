#include "algorithm.h"
#include <algorithm>

Permutation::Permutation(int length){
    this->length = length;
    this->index = 0;
}

char* Permutation::pNext(){
    char* p = "";
    switch (this->index){
        case 0:
            p = "133";break;
        case 1:
            p = "132";break;
        case 2:
            p = "231";break;
        case 3:
            p = "213";break;
        case 4:
            p = "312";break;
        case 5:
            p = "321"; break;
        defult:
            break;
    }

    this->index = this->index + 1;
    return p;
}
