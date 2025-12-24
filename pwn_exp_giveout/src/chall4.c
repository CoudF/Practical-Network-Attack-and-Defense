// chall4.c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdint.h>

// 为 ROP 提供明确的 gadget
__attribute__((naked))
void useful_gadgets() {
    asm volatile("pop %rdi; ret\npop %rsi; ret\npop %rdx; ret");
}

// 我们的ROP目标函数
void gadget_func(uint8_t a, uint8_t b, uint8_t c) {
    char buf[16];
    buf[0] = a;
    buf[1] = b;
    buf[2] = c;
    buf[3] = '\0';
    system(buf);
}

void vulnerable_func() {
    char buffer[32];
    printf("Enter your payload: ");
    read(0, buffer, 100);
}

int main() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    vulnerable_func();
    return 0;
}