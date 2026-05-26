class Solution:
    def __init__(self):
        self.delimiter = "#"
    
    def get_length(self, str1):
        return len(list(str1))

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for str1 in strs:
            encode_str1 = str(self.get_length(str1)) + str(self.delimiter) + str1
            encoded_string += encode_str1
        return encoded_string

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != self.delimiter:
                j += 1

            length = int(s[i:j])

            start = j + 1
            end = start + length

            word = s[start:end]
            ans.append(word)

            i = end

        return ans