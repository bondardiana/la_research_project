'This file finds most liked tweets'


def top_liked_tweets(twits, favs, user):
    # twits, favs, user = selecting_tweets()
    # print(max(favs))
    favs_copy = favs.copy()
    print(favs_copy)
    for i in range(11):
        print(i, user[favs_copy.index(max(favs_copy))])
        favs_copy[favs_copy.index(max(favs_copy))] = 0
