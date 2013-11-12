#include "check.h"
#include "algorithm.h"
#include <iostream>

using namespace std;

int main(){
    struct Node* head = new Node();
    init(head);

    /*
    for (int i=0; i<20; i++){
        cout << head->repeat[i] << endl;
        if (head->son[i] == NULL)
            cout << true << endl;
        cout << head->son[i] << endl;
    }
    */
    /*
    char* p = "1234";
    char* pp = p + 1;
    cout << p << endl;
    cout << pp << endl;
    cout << p[0] << ' ' << pp[0] << endl;
    cout << strlen(p) << endl;
    cout << strlen(pp) << endl;
    */
    int error = 0;

    int num = 0;
    int length = 3;
    Permutation P = Permutation(length);
    char* p = P.pNext();
    int c[] = {0,1,2,6,24,120,720,5040,40320,362800,3628000};
    while(num < c[length] && error == 0){
        num = num + 1;
        switch(addP(head, p)){
            case 0:
                p = P.pNext(); break;
            case 1:
                error = 1; break;
            case 2:
                error = 2; break;
            default:
                break;
        }
    }
    
    if (num < 1){
        error = 3;
    }

    switch(error){
        case 0:
            cout << "Correct" << endl; break;
        case 1:
            cout << "Wrong" << endl; break;
        case 2:
            cout << "Repeat" << endl; break;
        case 3:
            cout << "Too Few" << endl; break;
        default:
            break;
    }

    return 0;
}
