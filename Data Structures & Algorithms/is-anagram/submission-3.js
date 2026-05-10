class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */

    /**
     s = "racecar", t = "carrace"
                i  
        {
            c: 0,
            a: 0,
            r: 0
            e: 0
        }

     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false;

        let hash = new Map();

        for (const char of t) {
            hash.set(char, (hash.get(char) || 0) + 1);
        }

        for (const char of s) {
            if (hash.has(char)) {
                hash.set(char, hash.get(char) - 1);

                if (hash.get(char) === 0) {
                    hash.delete(char);
                }
            } else {
                return false;
            }
        }
        return hash.size === 0;
    }
}
