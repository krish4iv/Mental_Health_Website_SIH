def assess_mental_illness_stage():
    # Initialize a variable to keep track of the user's score.
    score = 0
    print("Hey there! I'm here to assist you in this survey.")
    print("Please answer the following questions with 'yes' or 'no'.")
    # Questions for Stage 1: Mild Depression
    questions_stage1 = [
        "Have you been feeling down or sad lately?",
        "Are you finding it harder to enjoy things you used to enjoy?",
        "Have you experienced any changes in your sleep patterns, like difficulty falling asleep or waking up too early?",
        "Have you noticed any changes in your appetite or weight?",
        "Do you often feel fatigued or lacking in energy?",
        "Have you been more irritable or impatient than usual?",
        "Do you find it difficult to concentrate on tasks or conversations?",
        "Have you withdrawn from social activities or spending time with friends?",
        "Do you frequently experience feelings of self-doubt or worthlessness?",
        "Have you had thoughts about seeking professional help for your mood?",
    ]
    # Loop through the questions and assess the user's responses.
    for question in questions_stage1:
        response = input(f"{question} (yes/no): ").lower()
        if response == "yes":
            score += 1
    # Determine the stage based on the score.
    if score <= 3:
        return "Stage 0: No Depression"
    elif score <= 6:
        return "Stage 1: Mild Depression"
    
    # Questions for Stage 2: Moderate Depression
    questions_stage2 = [
        "Do you often feel guilty or worthless?",
        "Are you frequently experiencing physical symptoms like aches or pains?",
        "Have you noticed changes in your social interactions, such as withdrawing from friends or family?",
        "Is it becoming harder to maintain your work or school responsibilities?",
        "Do you experience mood swings or sudden bursts of sadness or irritability?",
        "Have you thought about seeking help for your emotional state?",
        "Do you engage in self-criticism or negative self-talk?",
        "Have you experienced any changes in your appetite or weight?",
        "Have you been avoiding social situations or gatherings?",
        "Are you often overwhelmed by daily tasks or responsibilities?",
    ]
    # Loop through the questions for Stage 2 and assess the user's responses.
    for question in questions_stage2:
        response = input(f"{question} (yes/no): ").lower()
        if response == "yes":
            score += 1
    # Determine the stage based on the score.
    if score <= 9:
        return "Stage 2: Moderate Depression"
    # Questions for Stage 3: Severe Depression
    questions_stage3 = [
        "Do you ever have thoughts of hurting yourself or ending your life?",
        "Have you experienced a loss of interest in everything, including things you used to love?",
        "Is it difficult to carry out basic self-care activities, like bathing or dressing?",
        "Do you often feel detached from reality or like you're in a fog?",
        "Have you been unable to experience joy or happiness for an extended period?",
        "Do you engage in self-destructive behaviors or substance abuse?",
        "Are you frequently overwhelmed by thoughts of death or dying?",
        "Is it impossible for you to concentrate or make decisions?",
        "Are you neglecting important responsibilities, like work, school, or family obligations?",
        "Have you been avoiding friends and family for an extended period?",
    ]
    # Loop through the questions for Stage 3 and assess the user's responses.
    for question in questions_stage3:
        response = input(f"{question} (yes/no): ").lower()
        if response == "yes":
            score += 1
    # Determine the stage based on the score.
    if score >= 10:
        return "Stage 3: Severe Depression"
    return "Stage undetermined (consider seeking professional help)."
def provide_depression_support(stage):
    if "Stage 0" in stage:
        return [
            "Maintain a balanced lifestyle with regular sleep, exercise, and a healthy diet.",
            "Engage in stress-reduction activities like mindfulness or meditation.",
            "Stay connected with friends and family for emotional support.",
            "Participate in enjoyable activities and hobbies.",
        ]
    elif "Stage 1" in stage:
        return [
            "Consider self-help resources like self-help books or online courses.",
            "Set small, achievable goals to regain a sense of accomplishment.",
            "Reach out to a counselor or therapist for support and guidance.",
            "Join support groups or communities focused on well-being and mental health.",
        ]
    elif "Stage 2" in stage:
        return [
            "Seek professional therapy or counseling to address moderate symptoms.",
            "Discuss medication options with a psychiatrist if recommended.",
            "Develop a structured daily routine to maintain stability.",
            "Engage in regular exercise to boost mood and reduce symptoms.",
            "Lean on a trusted support network for emotional support.",
        ]
    elif "Stage 3" in stage:
        return [
            "Contact a mental health crisis hotline or a healthcare provider immediately.",
            "Share your feelings with a trusted friend or family member.",
            "Avoid isolation and stay in a safe environment.",
            "Consider hospitalization if recommended by a healthcare professional.",
            "Remember that help is available, and recovery is possible.",
        ]
    else:
        return ["Stage undetermined. Seek professional evaluation."]
# Call the function to assess the mental illness stage.
user_stage = assess_mental_illness_stage()
# Print the depression stage.
print(f"Depression Stage: {user_stage}")
# Get and print the strategies for the user's stage.
strategies = provide_depression_support(user_stage)
print("\nStrategies:")
for i, strategy in enumerate(strategies, start=1):
    print(f"{i}. {strategy}")
