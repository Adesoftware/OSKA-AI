def business_letter_prompt(topic):
    return f"""
Write a professional business letter about {topic}.

Requirements:
- Use today's date.
- Include a subject line.
- Use a professional greeting.
- Write 3 paragraphs.
- Use a professional closing.
- Do not use placeholders.
"""

def memo_prompt(topic):
    return f"""
Write a professional office memo.

Topic: {topic}

Format:
MEMORANDUM
To:
From:
Date:
Subject:

Write a complete memo without placeholders.
"""

def summarize_prompt(text):
    return f"""
Summarize the following text clearly and briefly:

{text}
"""