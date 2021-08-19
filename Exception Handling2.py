def vote(age):
    if age<18:
        raise ValueError("Invalid Voter")
    return "You are allow to vote"
try:
  # print(vote(16))
   #print(vote(17))
   print(vote(18))
   print(vote(21))
except ValueError as e:
    print(e)