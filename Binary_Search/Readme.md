# Binaary Search 
Binary Search is quite easy to understand conceptually. Basically, it splits the search space into two halves and only keep the half that probably has the search target and throw away the other half that would not possibly have the answer. 

In this manner, we reduce the search space to half the size at every step, until we find the target. Binary Search helps us reduce the search time from linear O(n) to logarithmic O(log n). 
But when it comes to implementation, it's rather difficult to write a bug-free code in just a few minutes. 
Some of the most common problems include:
When to exit the loop? Should we use left < right or left <= right as the while loop condition ?
How to initialize the boundary variable left and right?
How to update the boundary? How to choose the appropriate combination from left = mid , left = mid + 1 and right = mid, right = mid - 1?
A rather common misunderstanding of binary search is that people often think this technique could only be used in simple scenario like "Given a sorted array, 
find a specific value in it". As a matter of fact, it can be applied to much more complicated situations.

After a lot of practice in LeetCode, I've made a powerful binary search template and solved many Hard problems by just slightly twisting this template. I'll share the template with you guys in this post. 
I don't want to just show off the code and leave. Most importantly, I want to share the logical thinking: how to apply this general template to all sorts of problems. Hopefully, after reading this post, people wouldn't be pissed off any more when LeetCoding, "Holy sh*t! This problem could be solved with binary search! Why didn't I think of that before!"


Source : 
https://leetcode.com/problems/koko-eating-bananas/solutions/769702/python-clear-explanation-powerful-ultima-sx6q/?__cf_chl_f_tk=8xWazoQoUh8_Bu36wVAQy0Ec1kSLAHtKlD1na1BAG7g-1783348891-1.0.1.1-8n02clxoEk2HY3u61Fjt4CJtVAjWQWc9n7.q5qUcHvU
