def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    results = {}
    cc = list(text.lower())
    for each in cc:
        if each in results:
            results[each] += 1
        else:
            results[each] = 1
    return results

def snorted(text):
    results = sorted(text.items(), key=lambda x: x[1], reverse=True)
    return results
