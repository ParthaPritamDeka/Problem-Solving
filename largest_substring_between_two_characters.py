def solve(s):
   memo = {}
   for i in range(len(s)):
      if s[i] in memo:
         memo[s[i]].append(i)
      else:
         memo[s[i]] = [i]

   best = 0
   for key in memo:
      best = max(best, memo[key][-1] - memo[key][0])
   return best - 1

s = "level"
print(solve(s))
