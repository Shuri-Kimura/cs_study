#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
}
pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    // TODO
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(candidates[i], name) == 0)
        {
            ranks[rank] = i;
            return true;
        }
    }

    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    // TODO
    for (int i = 0; i < candidate_count - 1; i++)
    {
        for (int j = i + 1; j < candidate_count; j++)
        {
            preferences[ranks[i]][ranks[j]] += 1;
        }
    }
    // printf("%d\n",preferences[0][0]);
    // printf("%d\n",preferences[0][1]);
    // printf("%d\n",preferences[0][2]);
    // printf("\n");
    // printf("%d\n",preferences[1][0]);
    // printf("%d\n",preferences[1][1]);
    // printf("%d\n",preferences[1][2]);
    // printf("\n");
    // printf("%d\n",preferences[2][0]);
    // printf("%d\n",preferences[2][1]);
    // printf("%d\n",preferences[2][2]);
    return;
}


void print_pairs(pair pairs1[], int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("winner: %d\n", pairs1[i].winner);
        printf("loser: %d\n", pairs1[i].loser);
        printf("\n");
    }
    printf("\n");
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            if (preferences[i][j] > preferences[j][i])
            {
                pairs[pair_count].winner = i;
                pairs[pair_count].loser = j;
                pair_count += 1;
            }
        }
    }
    //print_pairs(pairs, pair_count);
    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    // TODO
    pair tmp;
    int exchange;
    do
    {
        exchange = 0;
        for (int i = 0; i < pair_count - 1; i++)
        {
            if (preferences[pairs[i].winner][pairs[i].loser] < preferences[pairs[i + 1].winner][pairs[i + 1].loser])
            {
                tmp = pairs[i];
                pairs[i] = pairs[i + 1];
                pairs[i + 1] = tmp;
                exchange++;
            }
        }
    }
    while (exchange > 0);
    //print_pairs(pairs,pair_count);
    return;
}

bool has_cycle_helper(int index, bool visited[])
{
    if (visited[index])
        return true;
    visited[index] = true;
    for (int i = 0; i < candidate_count; i++)
    {
        if (locked[index][i] && has_cycle_helper(i, visited))
        {
            return true;
        }
    }
    return false;
}

bool has_cycle(int strating_index)
{
    bool visited[candidate_count];
    for (int i = 0; i < candidate_count; i++)
        visited[i] = false;
        return has_cycle_helper(starting_index, visited);
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    // TODO
    for (int i = 0; i < pair_count; i++)
    {
        locked[pairs[i].winner][pairs[i].loser] = true;

        if (has_cycle(i))
            locked[pairs[i].winner][pairs[i].loser] = false;
    }
}

void print(bool flag)
{
    if (flag == true)
    {
        printf("true\n");
    }
    else
    {
        printf("false\n");
    }
}

// Print the winner of the election
void print_winner(void)
{
    // TODO
    int winner = 0;
    int exchange;
    // print(locked[0][1]);
    // print(locked[0][2]);
    // print(locked[1][0]);
    // print(locked[1][2]);
    // print(locked[2][0]);
    // print(locked[2][1]);
    do
    {
        exchange = 0;
        for (int i = 0; i < candidate_count; i++)
        {
            if (locked[i][winner] == true)
            {
                winner = i;
                exchange++;
            }
        }
    }
    while (exchange > 0);
    printf("%s\n", candidates[winner]);
    return;
}

