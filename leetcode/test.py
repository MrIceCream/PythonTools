
def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    _dict = {}
    for first_index in range(0, len(nums)-1):
        first = nums[first_index]
        for second_index in range(first_index+1, len(nums)):
            second = nums[second_index]
            if first + second == target:
                _dict[first_index] = True
                _dict[second_index] = True

    _result = []
    for key in _dict:
        _result.append(key)
    return _result

def twoSum_test():
    result = twoSum(None,[2, 1, 2, 3],3)
    print result

def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    if x == 0 : 
        return 0

    negative = x / abs(x)
    _list = map(int, str(abs(x)))
    _reverse = int(''.join(map(str, _list[::-1]))) * negative

    if -pow(2,31) < _reverse < pow(2,31)-1:
        return _reverse
    return 0

def reverse_test():
    # result = reverse(None, pow(2,32))
    result = reverse(None, 0)
    print(result)

def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0 :
        return False
    
    _list = map(int, str(x))
    _list_len = len(_list)
    for x in range(_list_len/2):
        if _list[x] != _list[_list_len-1-x] :
            return False
    
    return True

def isPalindrome_test():
    result = isPalindrome(None, 1223221)
    print(result)

def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    _dict = {'I':1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

    result = 0
    isCombine = False
    _len = len(s)

    if _len == 1:
        result += _dict[s[0]]

    for i in range(_len-1):
        char = s[i]
        next_char = s[i+1]
        
        if isCombine:
            isCombine = False
            continue

        if _dict[next_char] > _dict[char] :
            isCombine = True
            result += _dict[next_char] - _dict[char]
            continue
        result += _dict[char]
    
    if not isCombine and _len > 1:    
        result += _dict[next_char]
    return result

def romanToInt_test():
    result = romanToInt(None, 'MI')
    print(result)

def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) == 0:
        return ''

    strs.sort(key = lambda i:len(i))
    _resultList = None
    for index in xrange(len(strs)):
        _charList = map(str, strs[index])
        if _resultList == None:
            _resultList = _charList
            continue
        
        for x in xrange(len(_resultList)):
            if _charList[x] != _resultList[x]:
                _resultList = _resultList[:x:]
                break
    
    return ''.join(_resultList)

def longestCommonPrefix_test():
    # result = longestCommonPrefix(None, ["dog","racecar","car"])
    # result = longestCommonPrefix(None, ["flower","flow","flight"])
    result = longestCommonPrefix(None, [])
    print(result)

def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    

def isValid_test():
    result = isValid(None, r"()[]{}")
    # result = isValid(None, r"([)]")
    print(result)

if __name__ == "__main__":
    longestCommonPrefix_test()