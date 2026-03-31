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

# ---------------- NUMEROLOGY CORE ----------------
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

# ---------------- AUTO-GENERATED NUMEROLOGY PROFILES ----------------
traits_mulank = {
    1: "independent and a natural leader",
    2: "sensitive and cooperative",
    3: "creative and expressive",
    4: "practical and disciplined",
    5: "adventurous and energetic",
    6: "caring and responsible",
    7: "analytical and spiritual",
    8: "ambitious and powerful",
    9: "compassionate and wise"
}

traits_bhagyank = {
    1: "driven towards success",
    2: "guided by emotions and harmony",
    3: "destined for creativity and communication",
    4: "focused on stability and hard work",
    5: "full of change and excitement",
    6: "centered around love and responsibility",
    7: "inclined towards knowledge and spirituality",
    8: "oriented towards power and achievement",
    9: "connected to humanitarian goals"
}

traits_kua = {
    1: "with strong leadership energy",
    2: "with calm and nurturing energy",
    3: "with growth and creative energy",
    4: "with stable and practical energy",
    5: "with dynamic and unpredictable energy",
    6: "with protective and guiding energy",
    7: "with introspective and wise energy",
    8: "with powerful and ambitious energy",
    9: "with universal and giving energy"
}

career_fields = {
    1: ["Leadership", "Entrepreneurship"],
    2: ["Counseling", "Support roles"],
    3: ["Arts", "Media"],
    4: ["Engineering", "Management"],
    5: ["Travel", "Marketing"],
    6: ["Healthcare", "Education"],
    7: ["Research", "Spiritual fields"],
    8: ["Business", "Finance"],
    9: ["Social work", "Creative arts"]
}

love_traits = {
    1: "need independence in relationships",
    2: "are romantic and emotional",
    3: "are fun-loving and expressive",
    4: "are loyal and stable",
    5: "seek excitement in love",
    6: "are caring and committed",
    7: "are deep and thoughtful",
    8: "are intense and passionate",
    9: "are selfless and giving"
}

# Generate all 729 combinations
numerology_profiles = {}

for m in range(1, 10):
    for b in range(1, 10):
        for k in range(1, 10):
            numerology_profiles[(m, b, k)] = {
                "personality": f"You are {traits_mulank[m]}, {traits_bhagyank[b]}, {traits_kua[k]}.",
                "career": list(set(career_fields[m] + career_fields[b])),
                "love": f"In love, you {love_traits[m]} and your destiny makes you {love_traits[b]}."
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
profile = numerology_profiles[key]

print("👤 Personality:", profile["personality"])
print("💼 Career Options:", ", ".join(profile["career"]))
print("❤️ Love Compatibility:", profile["love"])

print("\n✨ Thank you for using ZodiNum Predictor ✨")
