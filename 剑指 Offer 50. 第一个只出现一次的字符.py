#在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
#示例:
#s = "abaccdeff"
#返回 "b"
#s = "" 
#返回 " "
class Solution:
    def firstUniqChar(self, s: str) -> str:
        if not s:
            return ' '
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for i in dic:
            if dic[i] == 1:
                return i
        return ' '
        
            
