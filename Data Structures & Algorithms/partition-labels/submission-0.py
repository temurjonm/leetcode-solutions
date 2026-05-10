'''  
     
     |
"xyxxyzbzbbisl"
  ^
 {'x': 3, 'y': 4, 'z': 7, 'b': 9, 'i': 10, 's': 11, 'l': 12}
'''
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        endChars = {}

        # find the last elemet of each chars
        for idx, char in enumerate(s):
            endChars[char] = idx

        size, result = 0, []
        last_end = endChars[s[0]]
        for idx, char in enumerate(s): # x
            # if idx == endChars[char]: insert into output
            size += 1
            last_end = max(last_end, endChars[char])
    
            if idx == last_end:
                result.append(size)
                size = 0
                

        return result

            

                
            
            