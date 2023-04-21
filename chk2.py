import snscrape.modules.twitter as sntwitter
import json
tweets=[]

print("****** TWITTER TWEET SCRAPER ******")

profile_name=input("Enter profile to scrape: ")

txt = sntwitter.TwitterUserScraper(profile_name)

no_of_tweet=int(input("Enter no tweet: "))

for i, tweet in enumerate(txt.get_items()):
    if i> no_of_tweet:
        break
    tweets.append(["Tweet id", tweet.id, "Tweet Content", tweet.rawContent])
f=open("tweets.json", "w")
j=json.dumps(tweets)
f.write(j)
print("Successfully scraped please check JSON file named as tweets.json")
f.close()
