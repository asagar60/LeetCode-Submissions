def longestCommonPrefix(strs):
        output = strs[0]
        for i in range(1, len(strs)):
            output = output[:min(len(strs[i]), len(output))]
            for k in range(len(output)):
                if strs[i][k] != output[k]:
                    output = output[:k]
                    break
        return output




print(longestCommonPrefix(["ab","a", "ab","aa"]))