'This file finds most liked tweets'


def top_liked_tweets(twits, favs, user):
    favs_copy = favs.copy()
    print(favs_copy)
    result = []
    for i in range(11):
        ind = favs_copy.index(max(favs_copy))
        result.append([i, user[ind],
                       ':', twits[ind], favs_copy[ind]])
        print(i, user[ind],
              ':', twits[ind], favs_copy[ind])
        favs_copy[ind] = 0
    return result
