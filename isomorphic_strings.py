{\rtf1\ansi\ansicpg1252\cocoartf1504\cocoasubrtf760
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 class Solution(object):\
    def isIsomorphic(self, s, t):\
        """\
        :type s: str\
        :type t: str\
        :rtype: bool\
        """\
        idx = 0\
        h=\{\}\
        while idx<len(s):\
            source = s[idx]\
            target = t[idx]\
            if source not in h.keys():\
                h[source] = target\
            else:\
                #source in h, need to check if matches the target according to previous assignment\
                if h[source] != target:\
                    return False\
            idx+=1\
        print(h, h.keys(), h.values())\
        return len(set(h.keys())) == len(set(h.values()))}