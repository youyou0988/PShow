struct Node{
    char current;

    char* suffix;

    bool repeat[20];
    struct Node* son[20];
};

/*
 * 0 for True
 */ 
int addP(struct Node* n, char* p);

int char2index(char c);

void init(struct Node* n);
