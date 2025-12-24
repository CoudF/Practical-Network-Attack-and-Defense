// chall3.c
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>

uint64_t notes[10];

void menu() {
    puts("=== Note System ===");
    puts("1. Read a note");
    puts("2. Write a note");
    puts("3. Exit");
    puts("4. Secret");
    printf(">> ");
}

void read_note() {
    int64_t idx;
    printf("Index: ");
    scanf("%ld", &idx);
    printf("Note[%ld] = %lu\n", idx, notes[idx]);
}

void write_note() {
    int64_t idx;
    uint64_t val;
    printf("Index: ");
    scanf("%ld", &idx);
    printf("Value: ");
    scanf("%lu", &val);
    notes[idx] = val;
}

void secret_func() {
    puts("sh");
}

int main() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    int choice;
    while(1) {
        menu();
        scanf("%d", &choice);
        switch(choice) {
            case 1: read_note(); break;
            case 2: write_note(); break;
            case 3: exit(0);
            case 4: secret_func(); break;
            default: puts("Invalid choice!"); break;
        }
    }
    return 0;
}