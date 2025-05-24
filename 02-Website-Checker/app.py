print("🔎WEBSITE URL CHECKER🔎")
url = input("\n Enter a URL to check:")
if url.startswith("https://"):
  print("🔒 This website uses HTTPS {secure}")
elif url.startswith("http://"):
  print("⚠️ This website uses HTTP {not secure}")
else:
  print("❌ This doesn't look like a URL. Please enter a valid URL starting with 'http://' or 'https://'.")
if url.endswith(".com"):
  print("✅ This is a commercial website.")
elif url.endswith(".org"):
  print("✅ This is an organization website.")
elif url.endswith(".edu"):
  print("✅ This is an educational website.")
elif url.endswith(".gov"):
  print("✅ This is a government website.")
elif url.endswith(".net"):
  print("✅ This is a network website.")
else:
  print("❌ This is an unknown type of website.")