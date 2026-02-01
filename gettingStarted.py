### welcome_assignment_answers
### Input - All nine questions given in the assignment.
### Output - The right answer for the specific question.

def welcome_assignment_answers(questions):
    answers = {}

    for x in questions:
        if x == "Are encoding and encryption the same? - Yes/No":
            answers[x] = "No"
        elif x == "Is it possible to decrypt a message without a key? - Yes/No":
            answers[x] = "No"
        elif x == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
            answers[x] = "pcap"
        elif x == "Is it possible to decode a message without a key? - Yes/No":
            answers[x] = "Yes"
        elif x == "Is a hashed message supposed to be un-hashed? - Yes/No":
            answers[x] = "No"
        elif x == "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
            answers[x] = "1d2ccd5d77a740544c75ebc15b51249e2110ff217a8e4ca84a6e982272b76a40"
        elif x == "Is MD5 a secured hashing algorithm? - Yes/No":
            answers[x] = "No"
        elif x == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
            answers[x] = int(4)
        elif x == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
            answers[x] = int(2)
        else:
            answers[x] = "This is not my beautiful wife! This is not my beautiful car! How did I get here?"
    return answers

if __name__ == "__main__":
# use this space to debug and verify that the program works
    debug_questions = [
            "Are encoding and encryption the same? - Yes/No",
            "Is it possible to decrypt a message without a key? - Yes/No",
            "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?",
            "Is it possible to decode a message without a key? - Yes/No",
            "Is a hashed message supposed to be un-hashed? - Yes/No",
            "What is the SHA256 hashing value of your NYU email and use the answer in your code - ",
            "Is MD5 a secured hashing algorithm? - Yes/No",
            "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number",
            "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number"
        ]

    result = welcome_assignment_answers(debug_questions)

    for x, y in result.items():
        print(x, ":", y)
