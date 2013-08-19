#!/usr/bin/python

from collections import defaultdict
from nltk.corpus import brown as corpus
import itertools

def ngrams(wordlist, n):
    """For list of words, generate sequences of n length
    >>> list(ngrams(['a', 'b', 'c', 'd'], 2))
    [('a', 'b'), ('b', 'c'), ('c', 'd')]

    >>> list(ngrams(['a', 'b', 'c', 'd'], 3))
    [('a', 'b', 'c'), ('b', 'c', 'd')]"""
    for index in range(len(wordlist[:-n])+1):
        yield tuple(wordlist[index:index+n])


def probability_map(ngrams):
    """ Calculate the probability of each n-gram occurring
    >>> ngrams =  [('a', 'b'), ('b', 'c'), ('c', 'd'), ('b', 'c')]
    >>> prob = probability_map(ngrams)
    >>> prob[('b', 'c')]
    0.5
    >>> prob[('a', 'b')]
    0.25
    >>> prob[('c', 'd')]
    0.25
    """
    counts = defaultdict(int)
    #Or: {ngram:ngrams.count(ngram) for ngram in set(ngrams)} #dict([(ngram, ngrams.count(ngram)) for ngram in set(ngrams)])
    for ngram in ngrams:
        counts[ngram] += 1
    # ngrams_list = list(ngrams)
    # counts = dict([(ngram, ngrams_list.count(ngram)) for ngram in set(ngrams_list)])

    total = float(sum(counts.values()))

    probabilities = dict([(k, (v/total)) for k,v in counts.iteritems()])

    return probabilities


def train(n, sentences):
    """Perform the whole training process
    >>> sentences = [['a', 'b', 'c'], ['b', 'c', 'd', 'e'], ['d', 'e']]
    >>> train(2, sentences)
    {('a', 'b'): 0.16666666666666666, ('b', 'c'): 0.33333333333333331, ('c', 'd'): 0.16666666666666666, ('d', 'e'): 0.33333333333333331}"""
    ngrams_for_sentences = [ngrams(sent, n) for sent in sentences]
    chained = itertools.chain(*ngrams_for_sentences)

    probs = probability_map(chained)

    return probs

def sentence_score(sentence, training):
    """Determine the score of a sentence against the training. 
    This score is the probability of the ngrams multiplied, for now."""
    sent_ngrams = ngrams(sentence)
    ngram_probabilities = [training[ngram] for ngram in sent_ngrams]

    total = reduce(lambda a,b: a*b, ngram_probabilities, 1)
    return total


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    #TRAINING:
    #   Import a corpus
    #   Build n-grams (start with n=2)
    #   Define probability for each n-gram
    #FIXING
    #   Take a sentence
    #   Shuffle the spaces around
    #       First each space separately back and forth one position, then a couple etc. 
    #   For each permutation:
    #       Get the n-grams
    #       Determine probability for n-grams. 
    #   Permutation with highest probability is the fixed sentence.

    
    #import ipdb; ipdb.set_trace()
    sentences = corpus.sents()
    #sentences = [['a', 'b', 'c'], ['b', 'c', 'd', 'e'], ['d', 'e']]
    p = train(2, sentences)

    import pprint
    pprint.pprint(p)