api_key= 'qkqNVgABDfX1zstZeoFlUzpyQ'
api_secret_key= '6e3WCd4pyjTyUvmKv6C8JEfsSWfIhE4vk0ktA0eE1Xc8lK9EAw'
access_token_key= '825851349535436801-gYIN9Pkjd39lTFoieCFnec5bnxNGj9c'
access_token_secret= 'VWSvb1T0OsgrNoEUa46amqCWcC0lLEphFoOqNOPjurPWO'

import twitter
import twitter_config

api = twitter.Api(consumer_key = twitter_config.api_key,
                  consumer_secret = twitter_config.api_secret_key,
                  access_token_key = twitter_config.access_token_key,
                  access_token_secret = twitter_config.access_token_secret,
                  tweet_mode = 'extended',
                  sleep_on_rate_limit = True)