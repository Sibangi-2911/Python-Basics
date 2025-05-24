print("🔠 TEXT CAPITALIZER 🔠")
text = input("📝 Please enter your text:")
print("🅰️ 1. UPPERCASE")
print("🔤 2. lowercase")
print("🗨 3. Title Case")
print("👆 4. Sentence case")

choice = input("✔️ Please enter your choice (1-4):" )
if choice == "1":
  print(text.upper())
elif choice == "2":
  print(text.lower())
elif choice == "3":
  print(text.title())
elif choice == "4":
  print(text.capitalize())
else:
  print("❌ Invalid choice. Please enter a number between 1 and 4.")