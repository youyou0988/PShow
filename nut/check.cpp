#include <string.h>
#include <stddef.h>
#include "check.h"
#include <iostream>

using namespace std;

// 0 correct
// 1 wrong
// 2 repeat
int addP(struct Node* n, char* p){
    cout << "----------------------------------" << endl;
    cout << p << " insert" << endl;
    char c = p[0];
    int i = char2index(c);
    
    // Find which node should be split
    while(n->son[i] != NULL || (n->son[i] == NULL && n->suffix[0] == c)){
        cout << "current n : " << n->current << endl;
        // Go Next
        if (n->son[i] != NULL){
            n = n->son[i];
            p = p + 1;
            c = p[0];
            i = char2index(c);
        // Sink current node Down    
        } else {
            if (strlen(n->suffix) == 1){
                return 2;
            }
            // Create new node from the father node
            struct Node* node = new Node();
            node->current = c;
            i = char2index(c);
            node->suffix = n->suffix + 1;
            memcpy(node->repeat, n->repeat, sizeof(n->repeat));
            if (node->repeat[i]){
                return 1;
            } else {
                node->repeat[i] = true;
            }
            if (strlen(node->suffix) == 1){
                cout << "old, Last suffix: " << node->suffix[0] << endl;
                int last = char2index(node->suffix[0]);
                if (node->repeat[last])
                    return 1;
                else
                    node->repeat[last] = true;
            }
            // Sink current node down
            n->son[i] = node;
    
            // Find Again
            n = n->son[i];
            p = p + 1;
            c = p[0];
            i = char2index(c);
        }
    }
    
    cout << p << endl;
    cout << c << endl;
    cout << n->current << endl;
    cout << n->suffix << endl;

    // If n is head, then will not sink down
    if (n->current != ' ' && strlen(n->suffix) > 1) {
        struct Node* node = new Node();
        node->current = n->suffix[0];
        i = char2index(n->suffix[0]);
        node->suffix = n->suffix + 1;
        memcpy(node->repeat, n->repeat, sizeof(n->repeat));

        // Maybe permutation is wrong
        if (node->repeat[i]){
            return 1;
        } else {
            node->repeat[i] = true;
        }
        n->son[i] = node;

        if (strlen(node->suffix) == 1){
            cout << "old, Last suffix: " << node->suffix[0] << endl;
            int last = char2index(node->suffix[0]);
            if (node->repeat[last])
                return 1;
            else
                node->repeat[last] = true;
        } else if (strlen(node->suffix) == 0){
            return 0;
        }
    }

    // Insert new node as n's son
    // Maybe the permutaion is wrong
    struct Node* node = new Node();
    node->current = c;
    i = char2index(c);
    node->suffix = p + 1;
    memcpy(node->repeat, n->repeat, sizeof(n->repeat));
    if (node->repeat[i])
        return 1;
    else
        node->repeat[i] = true;
    n->son[i] = node;

    if (strlen(node->suffix) == 1){
        cout << "new, Last suffix: " << node->suffix[0] << endl;
        int last = char2index(node->suffix[0]);
        if (node->repeat[last])
            return 1;
        else
            node->repeat[last] = true;
    } else if (strlen(node->suffix) == 0){
       return 0;
    }
    
    return 0;
}

int char2index(char c){
    int i = c - '0';
    return i;
}

void init(struct Node* n){
    n->current = ' ';
    n->suffix = " ";
    memset(n->repeat, false, sizeof(n->repeat));
    memset(n->son, NULL, sizeof(n->son));
}
