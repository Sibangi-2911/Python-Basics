print("🚶STEP COUNTER🚶")
daily_step_goal = int(input("🎯 What is your daily step goal?"))
today_steps = int(input("🚀 How many steps have you taken today?"))
if today_steps == daily_step_goal:
  print("🚩 Congratulations!! You have achieved your daily steps goal target.")
elif today_steps < daily_step_goal:
  steps_remaining = daily_step_goal - today_steps
  print(f"⏳ You need {steps_remaining} more steps to reach your daily goal.")
elif today_steps > daily_step_goal:
  steps_exceeded = today_steps - daily_step_goal
  print(f"💪 Congratulations! You have exceeded your goal by {steps_exceeded} steps!")
else:
  print("❓ Something went wrong. Please check your inputs.")