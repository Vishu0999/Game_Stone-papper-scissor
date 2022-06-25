import random
def gamesnake(comp, user):
    if comp == user:
        return None
    if comp == 's':
        if user == 'p':
            return True
        if user == 'c':
            return False
    if comp == 'p':
        if user == 's':
            return False
        if user == 'c':
            return True
    if comp == 'c':
        if user == 's':
            return True
        if user == 'p':
            return False

print("comp turn: Stone(s) Papper(p) or scissor(c)")
randno = random.randint(1,3)
if randno == 1:
    comp = 's'
if randno == 2:
    comp = 'p'
if randno == 3:
    comp = 'c'
user = input("Your turn: Stone(s) Papper(p) or scissor(c)")
print(f"comp chose: {comp}")
print(f"you chose: {user}")

game = gamesnake(comp, user)
if game == None:
    print("game tie")
elif game:
    print("You win")
else:
    print("you lose")

