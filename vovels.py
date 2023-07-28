def reverse_vowels(s):
    #leetcode
    vowels = set('aeiouAEIOU')
    
    s = list(s)
    #['l', 'e', 'e', 't', 'c', 'o', 'd', 'e']
    left, right = 0, len(s) - 1
    #0 <7

    while left < right:
        # 0 <7 and  s[0] = l not in vowels
        # 1 <7 and  s[1] = e in vowels
        while left < right and s[left] not in vowels:
            left += 1
            #1
            #0<7 and s[1] = e in vowels
            
        #1<7 and s[7] = e in vowels            
        while left < right and s[right] not in vowels:
            right -= 1 

        #1<7 and s[1] = e in vowels    
        if left < right:
            #s[1] ,s[7] = s[7],s[1]
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    return ''.join(s)

# Example usage:
input_str1 = "leetcode"
output_str1 = reverse_vowels(input_str1)
print(output_str1)  # Output: "leotcede"

input_str2 = "leotcede"
output_str2 = reverse_vowels(input_str2)
print(output_str2)  # Output: "leetcode"
