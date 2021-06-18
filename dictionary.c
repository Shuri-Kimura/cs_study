// Implements a dictionary's functionality

#include <stdbool.h>
#include <string.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>


#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 10001;
bool loaded_dict;
unsigned num_words;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    struct node *ptr;
    char s_word[strlen(word)];
    strcpy(s_word, word);

    for (int i = 0; word[i] != '\0'; i++)
    {
            s_word[i] = tolower(word[i]);
    }
    int hashval = hash(word);
    ptr = malloc(sizeof(struct node));
    ptr = table[hashval];
    while(ptr != NULL)
    {
        if (ptr->word == s_word)
        {
            //free(ptr);
            return true;
        }
        ptr = ptr->next;
    }
    free(ptr);
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO
    int hashval = 0;
    int shift = 1;
    for (int i = 0; word[i] != '\0'; i++)
    {
        hashval += word[i] << shift;
        shift++;
    }

    return hashval % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *fp;
    char word[LENGTH + 1];
    struct node *ptr;
    fp = fopen(dictionary,"r");
    if (fp == NULL)
    {
        return false;
    }
    ptr = malloc(sizeof(struct node));
    while(fscanf(fp,"%s",word) != EOF)
    {
        num_words++;
        for (int i =0; word[i] != '\0'; i++)
        {
            word[i] = tolower(word[i]);
        }
        printf("word: %s",word);
        int hashval =  hash(word);
        strcpy(ptr->word, word);
        ptr->next = table[hashval];
        table[hashval] = ptr;
    }
    fclose(fp);
    loaded_dict = true;
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    if (!loaded_dict)
    {
        return 0;
    }
    return num_words;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    if (!loaded_dict)
    {
        return false;
    }
    for (int i = 0; i < N; i++)
    {
        struct node *ptr;
        ptr = malloc(sizeof(struct node));
        ptr = table[i];
        while (ptr != NULL)
        {
            struct node *tmp = ptr;
            ptr = ptr->next;
            free(tmp);
        }
        free(ptr);
    }
    return true;

}
