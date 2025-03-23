def tweet_1():
    prompt = input("Enter your tweet: ")
    your_tweet = ""
    for c in prompt:
        if c in {"a","e","i","o","u","A","E","I","O","U"}:
            your_tweet = your_tweet + ""
        else:
            your_tweet = your_tweet + c
    
    return your_tweet

def tweet_2():
    prompt = input("Enter your tweet: ")
    vowels = "AEIOUaeiou"
    return ''.join(c for c in prompt if c not in vowels)

def main():
    
    prompt = tweet_1()

    prompt = tweet_2()
    print (prompt)

main()