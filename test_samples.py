from evaluator import evaluate_answer

TESTS = [
    {
        "name": "Full marks",
        "question": "Explain the process of photosynthesis.",
        "model": "Photosynthesis occurs in chloroplasts. Light energy is absorbed by chlorophyll, "
                 "water is split to release oxygen, and CO2 is fixed into glucose via the Calvin cycle.",
        "student": "Plants use chlorophyll in chloroplasts to absorb light. Water is split, releasing "
                   "oxygen, and carbon dioxide is converted into glucose in the Calvin cycle.",
        "marks": 5,
    },
    {
        "name": "Partial marks",
        "question": "Explain the process of photosynthesis.",
        "model": "Photosynthesis occurs in chloroplasts. Light energy is absorbed by chlorophyll, "
                 "water is split to release oxygen, and CO2 is fixed into glucose via the Calvin cycle.",
        "student": "Photosynthesis is how plants make food using sunlight. It uses chlorophyll.",
        "marks": 5,
    },
    {
        "name": "Wrong answer",
        "question": "Explain the process of photosynthesis.",
        "model": "Photosynthesis occurs in chloroplasts. Light energy is absorbed by chlorophyll, "
                 "water is split to release oxygen, and CO2 is fixed into glucose via the Calvin cycle.",
        "student": "Photosynthesis is how animals breathe by taking in oxygen through their lungs.",
        "marks": 5,
    },
    {
        "name": "Long but vague (should not get more marks for length)",
        "question": "Explain the process of photosynthesis.",
        "model": "Photosynthesis occurs in chloroplasts. Light energy is absorbed by chlorophyll, "
                 "water is split to release oxygen, and CO2 is fixed into glucose via the Calvin cycle.",
        "student": "Photosynthesis is a very important and fascinating process that has been studied "
                   "for many years by many scientists around the world. It is essential for life on "
                   "Earth and many organisms depend on it in various ways and it is really amazing.",
        "marks": 5,
    },
    {
        "name": "Blank answer",
        "question": "Explain the process of photosynthesis.",
        "model": "Photosynthesis occurs in chloroplasts.",
        "student": "   ",
        "marks": 5,
    },
]

if __name__ == "__main__":
    for t in TESTS:
        r = evaluate_answer(t["question"], t["model"], t["student"], t["marks"])
        print(f"\n--- {t['name']} ---")
        print(f"Score: {r['score']}/{r['max_marks']}")
        print("Missing:", r["missing_points"])
        print("Feedback:", r["feedback"])