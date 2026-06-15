def generate_answer(question):
    question = question.lower()

    if "ai" in question:
        return "AI stands for Artificial Intelligence. It enables machines to think and learn."

    elif "python" in question:
        return "Python is a beginner-friendly programming language used in web development, AI, and data science."

    elif "hello" in question:
        return "Hello! Nice to meet you."

    else:
        return "Sorry, I don't know the answer yet."