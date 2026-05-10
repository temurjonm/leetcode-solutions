/*
    s =  "Was it a car or a cat I saw?"
          l
                                    r   
    while left < right
        check if s[l] is not alpha num skip, the same as right

        if not match return false

    else return true

 */
class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let left = 0, right = s.length - 1

        const isAlpha = (char) => {
            return /^[a-zA-Z0-9]$/.test(char);
        };

        while (left < right) {
            while (left < right && !isAlpha(s[left])) left++
            while (left < right && !isAlpha(s[right])) right--

            if (s[left].toLowerCase() !== s[right].toLowerCase()) {
                return false
            }
            left++
            right--
        }
        return true
    }
}
