from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        met = 1
        new_string = ''
        i = 0
        while i < n:
            if i < n - 1:
                if chars[i] == chars[i+1]:
                    met += 1
                else:
                    smet = str(met) if met > 1 else ''
                    new_string += chars[i] + smet
                    met = 1
            else:
                smet = str(met) if met > 1 else ''
                new_string += chars[i] + smet
            i += 1

        chars[:] = new_string[:]

        print(new_string.split())

        return len(new_string)
