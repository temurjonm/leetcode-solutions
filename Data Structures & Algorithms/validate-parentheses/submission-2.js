class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     * 
     * "([{}])"
     *  i
     * [(,[,{ ]
     */
    isValid(s) {
        let hash = { ")": '(', ']': '[', '}': '{'}
        let stack = []

        for (let i=0; i<s.length;i++) {
            let char = s[i]

            if (hash.hasOwnProperty(char)) {
                if (stack && stack[stack.length-1] === hash[char]) {
                    stack.pop()
                } else {
                    return false
                }
            } else {
                stack.push(char)
            }    
        }
        return stack.length === 0
    }
}
