# 1348. 推文计数
'''
一家社交媒体公司正试图通过分析特定时间段内出现的推文数量来监控其网站上的活动。这些时间段可以根据特定的频率（ 每分钟 、每小时 或 每一天 ）划分为更小的 时间段 。

 

例如，周期 [10,10000] （以 秒 为单位）将被划分为以下频率的 时间块 :

 每 分钟 (60秒 块)： [10,69], [70,129], [130,189], ..., [9970,10000]

 每 小时 (3600秒 块)：[10,3609], [3610,7209], [7210,10000]

 每 天 (86400秒 块)： [10,10000]

注意，最后一个块可能比指定频率的块大小更短，并且总是以时间段的结束时间结束(在上面的示例中为 10000 )。

设计和实现一个API来帮助公司进行分析。

实现 TweetCounts 类:

 TweetCounts() 初始化 TweetCounts 对象。

 存储记录时间的 tweetName (以秒为单位)。

 List<integer> getTweetCountsPerFrequency(String freq, String tweetName, int startTime, int endTime) 返回一个整数列表，表示给定时间 [startTime, endTime] （单位秒）和频率频率中，每个 时间块 中带有 tweetName 的 tweet 的数量。
 
 freq 是 “minute” 、 “hour” 或 “day” 中的一个，分别表示 每分钟 、 每小时 或 每一天 的频率。
'''

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
import bisect
import heapq

class TweetCounts(object):

    def __init__(self):
        

    def recordTweet(self, tweetName, time):
        """
        :type tweetName: str
        :type time: int
        :rtype: None
        """
        

    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        """
        :type freq: str
        :type tweetName: str
        :type startTime: int
        :type endTime: int
        :rtype: List[int]
        """
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)

# 快速测试验证
if __name__ == "__main__":
    solution = Solution()
