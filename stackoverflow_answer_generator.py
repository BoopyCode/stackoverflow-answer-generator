#!/usr/bin/env python3
# StackOverflow Answer Generator - Because real answers are too mainstream

import random
import sys
from datetime import datetime, timedelta

class StackOverflowAnswerGenerator:
    """Generates authentic StackOverflow answers that don't actually help."""
    
    def __init__(self):
        self.answers = [
            "This question is a duplicate of a question from 2008.",
            "Just use jQuery.",
            "Have you tried turning it off and on again?",
            "Works on my machine ¯\\_(ツ)_/¯",
            "You're doing it wrong. Use this 500-line framework instead.",
            "The real problem is that you're using Python 3.",
            "This is trivial in Haskell.",
            "\"It depends\" (proceeds to not explain on what)",
            "RTFM - it's clearly documented in the 1998 spec.",
            "Just use async/await (for your synchronous problem)"
        ]
        
        self.comments = [
            "-1 This doesn't answer the question",
            "Accepted answer is wrong but has 10k upvotes",
            "\"This is the way\" (from someone with 200k rep)",
            "Why would anyone use this?",
            "\"First post!\" (on a 9-year-old question)"
        ]
    
    def generate_answer(self, question):
        """Generate a perfectly unhelpful answer."""
        answer = random.choice(self.answers)
        
        # 30% chance of outdated version warning
        if random.random() < 0.3:
            answer += f"\n\nNote: This only works in Python {random.randint(1, 2)}.{random.randint(0, 7)}"
        
        # 40% chance of irrelevant code snippet
        if random.random() < 0.4:
            answer += f"\n\n```python\n# Here's some unrelated code\ndef solve_nothing():\n    return 'not your answer'\n```"
        
        # Add random upvotes (more if answer is wrong)
        upvotes = random.randint(-5, 1000)
        if "wrong" in answer.lower() or "jQuery" in answer:
            upvotes = random.randint(500, 5000)
        
        # Make it look old (but still accepted)
        years_ago = random.randint(1, 12)
        date = datetime.now() - timedelta(days=365*years_ago)
        
        return {
            "answer": answer,
            "upvotes": upvotes,
            "accepted": random.choice([True, False, False]),  # Mostly wrong answers
            "date": date.strftime("%b %d '%y at %H:%M"),
            "comments": random.sample(self.comments, k=random.randint(0, 3))
        }

def main():
    """Because real StackOverflow is too helpful sometimes."""
    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])
    else:
        question = input("What's your programming problem? ")
    
    print(f"\nQuestion: {question}\n")
    print("="*50)
    
    generator = StackOverflowAnswerGenerator()
    answer = generator.generate_answer(question)
    
    print(f"Answer ({answer['date']}):\n")
    print(answer['answer'])
    print(f"\n▲ {answer['upvotes']} votes")
    if answer['accepted']:
        print("✓ Accepted Answer (probably wrong)")
    
    if answer['comments']:
        print("\nComments:")
        for comment in answer['comments']:
            print(f"• {comment}")
    
    print("\n" + "="*50)
    print("Good luck with that! 🎯")

if __name__ == "__main__":
    main()
