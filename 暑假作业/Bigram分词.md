# Bigram分词

这题的核心就是判断first second third三个词出现的情况，要么连续出现，要么first second third 三个单词中的third是下一次循环中的first

首先还是按照空格分割句子

然后边遍历边判断，最后输出结果

```python
class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        res = []
        text = text.split()
        for i in range(len(text) - 2):
            if text[i] == first and text[i + 1] == second:
                res.append(text[i + 2])
        return res
        
```

