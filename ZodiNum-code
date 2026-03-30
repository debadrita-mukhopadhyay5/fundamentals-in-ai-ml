import random

# ---------------- ZodiNum Predictor 🔮🔢 ----------------
# AI-based Zodiac + Numerology + NLP System

# ---------------- NLP DATASET ----------------
dataset = [
    "Today is a great day to take new opportunities and grow",
    "You will find happiness in small things today",
    "Challenges may arise but your strength will guide you",
    "Love and positivity will surround you",
    "A new career opportunity may come your way",
    "Your hard work will soon pay off",
    "Stay calm and trust your instincts",
    "You may meet someone important today"
]

# ---------------- NLP MODEL ----------------
def build_model(data):
    model = {}
    for sentence in data:
        words = sentence.lower().split()
        for i in range(len(words)-1):
            if words[i] not in model:
                model[words[i]] = []
            model[words[i]].append(words[i+1])
    return model

def generate_text(model, length=10):
    word = random.choice(list(model.keys()))
    result = word.capitalize()

    for _ in range(length):
        if word in model:
            word = random.choice(model[word])
            result += " " + word
        else:
            break

    return result + "."

# ---------------- NUMEROLOGY ----------------
def reduce_number(num):
    while num > 9:
        num = sum(int(d) for d in str(num))
    return num

def get_mulank(day):
    return reduce_number(day)

def get_bhagyank(dob):
    total = sum(int(d) for d in dob if d.isdigit())
    return reduce_number(total)

def get_kua(year, gender):
    total = sum(int(d) for d in str(year))
    kua = reduce_number(total)

    if gender == "male":
        kua = 11 - kua
    else:
        kua = kua + 4

    return reduce_number(kua)

# ---------------- NUMEROLOGY PROFILES ----------------
numerology_profiles = {
    (6, 4, 3): {
        "personality": "You are caring, responsible and practical with a creative side.",
        "career": ["Management", "Design", "Education", "Business"],
        "love": "You are loyal and supportive. Best compatibility with 2, 6, and 9."
    }
}

# ---------------- EXTRA FEATURES ----------------
lucky_colors = ["Red", "Blue", "Green", "Yellow", "Purple"]
fortune_levels = ["⭐⭐⭐⭐⭐ Very Lucky", "⭐⭐⭐⭐ Lucky", "⭐⭐⭐ Average", "⭐⭐ Challenging"]

# ---------------- BUILD MODEL ----------------
model = build_model(dataset)

# ---------------- USER INPUT ----------------
print("🔮 Welcome to ZodiNum Predictor 🔮🔢\n")

zodiac = input("Enter your zodiac sign: ")
dob = input("Enter DOB (DDMMYYYY): ")
gender = input("Enter gender (male/female): ").lower()

# ---------------- EXTRACT DATA ----------------
day = int(dob[:2])
year = int(dob[4:])

mulank = get_mulank(day)
bhagyank = get_bhagyank(dob)
kua = get_kua(year, gender)

# ---------------- OUTPUT ----------------
print("\n🔮 ZodiNum AI Prediction 🔮\n")

print("🌟 General:", generate_text(model))
print("❤️ Love:", generate_text(model))
print("💼 Career:", generate_text(model))

print("\n🍀 Lucky Number:", random.randint(1, 99))
print("🎨 Lucky Color:", random.choice(lucky_colors))
print("⭐ Fortune Level:", random.choice(fortune_levels))

# ---------------- NUMEROLOGY ----------------
print("\n🔢 Numerology Details 🔢")
print("Mulank:", mulank)
print("Bhagyank:", bhagyank)
print("Kua Number:", kua)

# ---------------- PERSONALITY INSIGHTS ----------------
print("\n🧠 ZodiNum Insights 🧠")

key = (mulank, bhagyank, kua)

if key in numerology_profiles:
    profile = numerology_profiles[key]

    print("👤 Personality:", profile["personality"])
    print("💼 Career Options:", ", ".join(profile["career"]))
    print("❤️ Love Compatibility:", profile["love"])

else:
    print("👤 Personality: You are a unique mix of traits with both emotional and practical qualities.")
    print("💼 Career Options: Suitable for creative and analytical roles.")
    print("❤️ Love Compatibility: Best with understanding partners.")

print("\n✨ Thank you for using ZodiNum Predictor ✨")
