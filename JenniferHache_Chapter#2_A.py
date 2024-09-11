# This program will check for spam words in emails
# Create list that contains common spam words from emails
mySpam = [
    'Best Rates','As seen on','Cash bonus','Act now!','Limited time','Don’t hesitate!','Now only',
    'Order now','Urgent','All new','Congrats!','Guaranteed','Satisfaction','Free Trial','Free Membership',
    'Free Sample','Deal','No Strings Attached','Trial','Winner!','Unlimited','Offer','Solution','Chance',
    'Full Refund','Click Below','Best Price','Cheap','Buy Direct'
    ]

# Create a function that will calculate the spam score
# Function will detect spam words from list
def spam_scores(email_message):
    score = 0
    words_found = []

# Change email message to lowercase for case-sensitivity
    email_message = email_message.lower()

# check spam words in emails and return the score and spam words found
    for spam in mySpam:
        if spam.lower() in email_message:
            score += 1
            words_found.append(spam)

    return score, words_found

# Create a function that will rate likelihood of the spam score. add score as parameter to the function
def rate_spam(score):
    if score == 0:
        return "Not a spam email, safe to continue."
    elif score <= 5:
        return "Low chance of this being a spam email."
    elif score <= 10:
        return "Email could be a spam, moderate risk."
    else:
        return "High risk email. Most likely a spam!"

# Create main function that user can input email message and run application
def main():
    email_message = input("Enter your email message here: ")
    score, words_found = spam_scores(email_message)
    spam_likelihood = rate_spam(score)

    print(f"Spam score is: {score}")
    print(f"Spam likelihood is: {spam_likelihood}")
    # Use if statement to display the spam words that were found in the email message
    if words_found:
        print("Words found in email message are: ")
        for spam in words_found:
            print(f" {spam}")

if __name__ == "__main__":
    main()

