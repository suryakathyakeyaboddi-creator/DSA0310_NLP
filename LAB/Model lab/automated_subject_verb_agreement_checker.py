print("SUBJECT-VERB AGREEMENT CHECKER")

sentence = input("Enter sentence: ").lower().replace(".", "").split()

if len(sentence) < 2:
    print("Please enter at least a subject and a verb.")
else:
    subject, verb = sentence[0], sentence[1]

    singular_subjects = ["he", "she", "it"]
    plural_subjects = ["they", "we", "you"]
    singular_verbs = ["is", "has", "does"]
    plural_verbs = ["are", "have", "do"]

    if subject in singular_subjects and verb in singular_verbs:
        print("Correct: Subject and verb agree.")
    elif subject in plural_subjects and verb in plural_verbs:
        print("Correct: Subject and verb agree.")
    elif subject in singular_subjects + plural_subjects:
        print("Grammar Error: Subject-verb disagreement!")
    else:
        print("Unable to identify subject or verb.")
