#!/usr/bin/env python

# File       : normalize.py
# Author     : Douglas Anderson
# Description: Normalizes words to ease comparison

import re

def __call__(tokens):
    normalize_words(tokens)
    normalize_punct(tokens)
    normalize_emoticons(tokens)
    normalize_users(tokens)
    normalize_hashtags(tokens)
    normalize_nums(tokens)
    normalize_urls(tokens)
    return tokens

def normalize_users(tokens):
    for t in tokens:
        if t.tokentype == "user":
                t.text = "@USER"

def normalize_urls(tokens):
    for t in tokens:
        if t.tokentype == "url ":
            t.text = "@URL"

def normalize_nums(tokens):
    for t in tokens:
        if t.tokentype == "num ":
            t.text = "#NUM"

def normalize_hashtags(tokens):
    for t in tokens:
        if t.tokentype == "hash":
            t.text = "#OCTOTHORPE"

def normalize_punct(tokens):
    for t in tokens:
        if t.tokentype == "punc":
            if t.text == ".." or t.text == "...":
                t.text = "ELLIPSIS"
            if t.text == "!":
                t.text = "BANG"
            if t.text == "?":
                t.text = "QUESTION"
            for punct in """.,:;+-_=*&^%$"'~`<>[]{}()""":
                if t.text == punct:
                    t.text = "PUNCT"

def normalize_emoticons(tokens):
    happy= re.compile(":-?\)+|:-?D+|B-?\)+|8-?\)+|:-?p+")
    sad  = re.compile(":-?\(+|8-?\(+|:'\(+")
    wink = re.compile(";-?\)|;-?D|;-?p")
    love = re.compile("<+3+")
    for t in tokens:
        if t.tokentype == "emot":
            if happy.match(t.text):
                t.text = "EM_HAPPY"
            elif sad.match(t.text):
                t.text = "EM_SAD"
            elif wink.match(t.text):
                t.text = "EM_WINK"
            #elif surprise.match(t.text):
                #t.text = "EM_SURPRISE"
            elif love.match(t.text):
                t.text = "EM_LOVE"
            else:
                print "ERROR. Unrecognized emticon"

def normalize_words(tokens):
    for t in tokens:
        if t.tokentype == "word":
            t.text = t.text.lower()

