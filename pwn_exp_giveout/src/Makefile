all: chall1 chall2 chall3 chall4
chall1: chall1.c
	gcc -static-pie -o chall1 chall1.c
chall2: chall2.c
	gcc -static-pie -o chall2 chall2.c
chall3: chall3.c
	gcc -o chall3 chall3.c
chall4: chall4.c
	gcc -fno-stack-protector -static -o chall4 chall4.c
clean:
	rm -f chall1 chall2 chall3 chall4


