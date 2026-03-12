print("AI-Based Exam Anxiety Detector")

text = input("Enter your exam thoughts: ")

if "scared" in text or "nervous" in text:
    print("Anxiety Level: High")
elif "worried" in text:
    print("Anxiety Level: Moderate")
else:
    print("Anxiety Level: Low")
