import random
def rps():
  user=input('Rock(r),Paper(p),Scissors(s),What do you choose ')
  user.lower()
  options=['r','p','s','shaktimaaan']
  weights=[0.3,0.3,0.3,0.1]
  comp=random.choices(options,weights,k=1)[0]
  print(f"Your choice: {user}, Computer choice: {comp}")

  if comp=='shaktimaaan':
    print("I choose shaktimaaan, I make the rules , I win.")
  elif user==comp:
    print('Its a tie')
  elif (user=='r'and comp=='p') or (user=='r' and comp=='s') or (user=='s' and comp=='p'):
    print('You won!!')
  else:
    print('You lost..')


rps()
