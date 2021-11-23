# Ideen er å holde styr på hvilke bokstaver som er mappet til hvilket ord, og hvilke ord
# som er mappet til hvilken bokstav. For hver bokstav/ord, sjekk at dette stemmer
def wordPattern(pattern: str, s: str) -> bool:
        pattern_map = {}
        word_map = {}
        
        words = s.split()
        
        # Sjekk at lengdene stemmer
        if len(words) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]
            
            if char not in pattern_map and word not in word_map:
                pattern_map[char] = word
                word_map[word] = char
                
            elif char in pattern_map and pattern_map[char] != word:
                return False
            
            elif word in word_map and word_map[word] != char:
                return False
            
        return True
