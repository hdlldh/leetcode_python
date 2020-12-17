#Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1. 
#
# Example 1: 
#
# 
#Input: 123
#Output: "One Hundred Twenty Three"
# 
#
# Example 2: 
#
# 
#Input: 12345
#Output: "Twelve Thousand Three Hundred Forty Five" 
#
# Example 3: 
#
# 
#Input: 1234567
#Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# 
#
# Example 4: 
#
# 
#Input: 1234567891
#Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
# 
# Related Topics Math String



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        oneDigit = {1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
        twoDigit ={10:'Ten',11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eighteen',19:'Nineteen'}
        tenDigit ={2:'Twenty',3:'Thirty',4:'Forty',5:'Fifty',6:'Sixty',7:'Seventy',8:'Eighty',9:'Ninety'}

        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000

        if not num: return 'Zero'

        def two(num):
            if not num: return ''
            elif num <10: return oneDigit[num]
            elif num <20: return twoDigit[num]
            else:
                tens =num //10
                rest = num - tens*10
                return tenDigit[tens] + ' ' + oneDigit[rest] if rest else tenDigit[tens]

        def three(num):
            hundred = num//100
            rest = num - hundred*100
            if hundred and rest: return '%s Hundred %s'%(oneDigit[hundred], two(rest))
            elif not hundred and rest: return two(rest)
            elif hundred and not rest: return '%s Hundred'%oneDigit[hundred]

        ans = ''
        if billion: ans += three(billion) + ' Billion'
        if million:
            if ans: ans += ' '
            ans += three(million) + ' Million'
        if thousand:
            if ans: ans += ' '
            ans += three(thousand) + ' Thousand'
        if rest:
            if ans: ans += ' '
            ans += three(rest)
        return ans
#leetcode submit region end(Prohibit modification and deletion)
