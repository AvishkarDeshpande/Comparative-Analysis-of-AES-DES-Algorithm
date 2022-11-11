import des_block


msg=input("Enter a message ... ")
msg_list=msg.split()
print(msg_list)

for i in msg_list:
    des_block.dec2hex(i)
print()

final_msg=' '.join(msg_list)
print(final_msg)
