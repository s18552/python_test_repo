
    def distance(s1, s2):
        if len(s1) != len(s2):
            raise ValueError("strings have different length")
        i = 0
        result = 0
        while len(s1) > i:
            if s1[i] != s2[i]:
                result += 1
            i += 1
        return result


