# streamcreator
Shows how easy it is to create a stream at https://www.microprediction.org/

### To do something similar

0. Fork
1. Open the [notebook](https://github.com/microprediction/streamcreator/blob/main/New_Key_12.ipynb) in colab and run to make a key. 
2. Create a GitHub secret called WRITE_KEY and put it there
3. Create a new GitHub action, cut and paste [this example](https://github.com/microprediction/streamcreator/blob/main/.github/workflows/daily.yml)
4. Modify cron schedule in your new action
5. Modify set.py to get the data you care about

Your stream(s) will appear [here](https://www.microprediction.org/browse_streams.html) sooner or later. 
