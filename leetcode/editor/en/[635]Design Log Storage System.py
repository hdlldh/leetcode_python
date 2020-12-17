# You are given several logs that each log contains a unique id and timestamp. T
# imestamp is a string that has the following format: Year:Month:Day:Hour:Minute:S
# econd, for example, 2017:01:01:23:59:59. All domains are zero-padded decimal num
# bers. 
# 
#  Design a log storage system to implement the following functions: 
# 
#  void Put(int id, string timestamp): Given a log's unique id and timestamp, st
# ore the log in your storage system. 
#  
#  int[] Retrieve(String start, String end, String granularity): Return the id o
# f logs whose timestamps are within the range from start to end. Start and end al
# l have the same format as timestamp. However, granularity means the time level f
# or consideration. For example, start = "2017:01:01:23:59:59", end = "2017:01:02:
# 23:59:59", granularity = "Day", it means that we need to find the logs within th
# e range from Jan. 1st 2017 to Jan. 2nd 2017. 
# 
#  Example 1: 
#  
# put(1, "2017:01:01:23:59:59");
# put(2, "2017:01:01:22:59:59");
# put(3, "2016:01:01:00:00:00");
# retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year"); // return [1,2,3
# ], because you need to return all logs within 2016 and 2017.
# retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Hour"); // return [1,2],
#  because you need to return all logs start from 2016:01:01:01 to 2017:01:01:23, 
# where log 3 is left outside the range.
#  
#  
# 
#  Note: 
#  
#  There will be at most 300 operations of Put or Retrieve. 
#  Year ranges from [2000,2017]. Hour ranges from [00,23]. 
#  Output for Retrieve has no order required. 
#  
#  Related Topics String Design


# leetcode submit region begin(Prohibit modification and deletion)
class LogSystem(object):

    def __init__(self):
        self.mem = collections.defaultdict(list)
        self.data = []

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: None
        """
        if timestamp not in self.mem:
            if not self.data: self.data.append(timestamp)
            else:
                low = 0
                high = len(self.data)-1
                while low<=high:
                    mid = low + (high-low)//2
                    if self.data[mid] >= timestamp: high = mid -1
                    else: low = mid +1
                self.data.insert(low, timestamp)
        self.mem[timestamp].append(id)

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        ans = []
        if gra =='Year':
            s1 = s[:4] + ':00:00:00:00:00'
            e1 = e[:4] + ':12:31:23:59:59'
        elif gra =='Month':
            s1 = s[:7] + ':00:00:00:00'
            e1 = e[:7] + ':31:23:59:59'
        elif gra =='Day':
            s1 = s[:10] + ':00:00:00'
            e1 = e[:10] + ':23:59:59'
        elif gra == 'Hour':
            s1 = s[:13] + ':00:00'
            e1 = e[:13] + ':59:59'
        elif gra == 'Minute':
            s1 = s[:16] + ':00'
            e1 = e[:16] + ':59'
        elif gra == 'Second':
            s1 = s
            e1 = e

        low = 0
        high = len(self.data)-1
        while low<=high:
            mid = low + (high-low)//2
            if self.data[mid] >= s1: high = mid -1
            else: low = mid +1
        while low < len(self.data) and self.data[low] <= e1:
            ans.extend(self.mem[self.data[low]])
            low += 1
        return ans



# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)
# leetcode submit region end(Prohibit modification and deletion)
