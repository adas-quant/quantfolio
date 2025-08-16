import asyncio
from twscrape import API, gather
from twscrape.logger import set_log_level
import json

async def main():
    api = API()  # or API("path-to.db") – default is `accounts.db`

    await api.pool.add_account("user1", "pass1", "u1@example.com", "mail_pass1")
    await api.pool.login_all() # try to login to receive account cookies

    # API USAGE

    # search (latest tab)
    query = '(#nifty50 OR #sensex OR #intraday OR #banknifty) lang:en'
    scraped_tweets = await gather(api.search(query, limit=20))  # list[Tweet]
    print(scraped_tweets)
    tweets_data_to_save = []
    for tweet in scraped_tweets:
        # Select only the fields you need, as per the assignment
        tweets_data_to_save.append({
            'id': tweet.id,
            'username': tweet.user.username,
            'timestamp_utc': tweet.date.isoformat(), # Use ISO format for universal compatibility
            'content': tweet.rawContent,
            'like_count': tweet.likeCount,
            'retweet_count': tweet.retweetCount,
            'reply_count': tweet.replyCount,
            'quote_count': tweet.quoteCount,
            'hashtags': tweet.hashtags,
            'mentioned_users': [user.username for user in tweet.mentionedUsers] if tweet.mentionedUsers else [],
            'url': tweet.url,
            'user_followers': tweet.user.followersCount,
            'user_location': tweet.user.location
        })

    # Save the list of dictionaries to a JSON file
    # JSON is great for storing raw, semi-structured data before processing
    raw_data_filename = 'raw_tweets.json'
    with open(raw_data_filename, 'w', encoding='utf-8') as f:
        json.dump(tweets_data_to_save, f, ensure_ascii=False, indent=4)

    print(f"Successfully saved raw data to {raw_data_filename}")

if __name__ == "__main__":
    asyncio.run(main())
