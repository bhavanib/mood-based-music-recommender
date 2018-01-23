The aim of the project is to recommend Music based on the mood of the target user. The proposed method takes user's post as input from Facebook data, along with the user profile details (such as age, gender, country). In this approach, we have a two-step categorization wherein the first categorization of the user post identifies the human emotion and categorizes it into a particular emotion. The post is then passed through the second level of categorization wherein the sentiment of the post is identified. We then combine these two category buckets to obtain a mood represented in an emotion-sentiment space.

This mood representation is passed to a classifier which also uses the user profile parameter to build a prediction model of songs for the user.


