
url = input("Enter a sample URL: ").lower()

suspicious_words = ["login", "verify", "free", "update", "account"]
score = 0

if "http://" in url:
    score += 1

if "@" in url:
    score += 1

if url.count("-") >= 2:
    score += 1

for word in suspicious_words:
    if word in url:
        score += 1

if score >= 3:
    print("Warning: This URL has suspicious patterns.")
else:
    print("No listed suspicious patterns found.")

print("Pattern score:", score)
