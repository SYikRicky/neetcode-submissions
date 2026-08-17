class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const map1 = new Map();
        let count = 0;
        for (let i in s) {
            if (!map1.has(s[i])) map1.set(s[i], 0);
            map1.set(s[i], map1.get(s[i]) + 1);
        }
        
        const map2 = new Map();
        map1.entries().forEach(i => (map2.set(i[0],i[1])))

        for (let i in t) {
            if(map1.has(t[i])) {
                map1.set(s[i], map1.get(s[i]) + 1);
            } else {
                return false;
            }
        }
        let arr1 = [];
        let arr2 = [];

        map1.values().forEach(n => arr1 += n/2);
        map2.values().forEach(n => arr2 += n);

        console.log(arr1)
        console.log(arr2)
        
        if (arr1 === arr2) {
            return true;
        }

        return false;
    }
}
