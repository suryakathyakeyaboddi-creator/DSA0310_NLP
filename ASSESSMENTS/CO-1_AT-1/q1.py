
import re
import json

# Sample resumes in text format
resumes = [
    """
    Name: Rahul Sharma
    Email: rahul.sharma@gmail.com
    Mobile: +91 9876543210
    Skills: Python, SQL, Machine Learning, NLP
    Experience: 3 years
    """,
    """
    Name: Priya Reddy
    Email: priya.reddy@yahoo.com
    Mobile: 9123456789
    Skills: Java, SQL, NLP
    Experience: 4 years
    """,
    """
    Name: Arjun Kumar
    Email: arjun.kumar@outlook.com
    Mobile: 9988776655
    Skills: Python, Java, SQL
    Experience: 1 year
    """,
    """
    Name: Sneha Patel
    Email: sneha.patel@gmail.com
    Mobile: +91-9876501234
    Skills: Python, Java, Machine Learning
    Experience: 2 years
    """
]

# Regular expression patterns
name_pattern = r"Name\s*:\s*([A-Za-z]+(?:\s+[A-Za-z]+)*)"
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
mobile_pattern = r"(?<!\d)(?:\+91[-\s]?)?[6-9]\d{9}(?!\d)"
experience_pattern = (
    r"Experience\s*:\s*(\d+(?:\.\d+)?)\s*"
    r"(?:years?|yrs?)\b"
)

# Technical skills to detect
technical_skills = [
    "Python",
    "Java",
    "SQL",
    "Machine Learning",
    "NLP"
]

def extract_resume_info(resume):
    # Extract candidate name
    name_match = re.search(name_pattern, resume, re.IGNORECASE)
    name = name_match.group(1).strip() if name_match else "Not found"

    # Extract email
    email_match = re.search(email_pattern, resume)
    email = email_match.group(0) if email_match else "Not found"

    # Extract mobile number
    mobile_match = re.search(mobile_pattern, resume)
    mobile = mobile_match.group(0) if mobile_match else "Not found"

    # Extract technical skills
    skills_found = []
    for skill in technical_skills:
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"
        if re.search(pattern, resume, re.IGNORECASE):
            skills_found.append(skill)

    # Extract years of experience
    exp_match = re.search(
        experience_pattern, resume, re.IGNORECASE
    )
    experience = float(exp_match.group(1)) if exp_match else 0

    # Eligibility: at least 2 years and Python skill
    eligible = experience >= 2 and "Python" in skills_found

    # Return structured candidate profile
    return {
        "Name": name,
        "Email": email,
        "Mobile": mobile,
        "Technical Skills": skills_found,
        "Experience (Years)": experience,
        "Eligible": "Yes" if eligible else "No"
    }


# Process all resumes
candidate_profiles = []

for index, resume in enumerate(resumes, start=1):
    profile = extract_resume_info(resume)
    profile["Candidate ID"] = index
    candidate_profiles.append(profile)

# Display all candidate profiles
print("=" * 65)
print("       RESUME INFORMATION EXTRACTION SYSTEM")
print("=" * 65)

for profile in candidate_profiles:
    print("\nCandidate ID:", profile["Candidate ID"])
    print(json.dumps(profile, indent=4))

# Display eligible candidates
print("\n" + "=" * 65)
print("CANDIDATES WHO MEET MINIMUM ELIGIBILITY CRITERIA")
print("Criteria: Experience >= 2 years AND Python skill")
print("=" * 65)

eligible_candidates = [
    candidate for candidate in candidate_profiles
    if candidate["Eligible"] == "Yes"
]

if eligible_candidates:
    for candidate in eligible_candidates:
        print(
            f"Name: {candidate['Name']} | "
            f"Experience: {candidate['Experience (Years)']} years | "
            f"Skills: {', '.join(candidate['Technical Skills'])}"
        )
else:
    print("No eligible candidates found.")

print("\nTotal resumes processed:", len(candidate_profiles))
print("Eligible candidates:", len(eligible_candidates))
