import time
print("COUNTDOWN TIMER")
print("Count from your choosen seconds!")
while True:
  count = int(input("Enter seconds to countdown from: "))
  if count<=0:
    print("Please enter a positive number")
    continue
  print(f"Starting countdown from {count} seconds!!")
  for i in range(count,0,-1):
    print(f"{i} seconds remaining...")
    time.sleep(1)
  print("COUNTDOWN COMPLETE!")
  count_down = input("Start another countdown? (yes/no): ")
  if count_down.lower()!='yes':
    print("Thanks for using the countdown timer.")
    break
