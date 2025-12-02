def InvertStr(S, K, N):
  K-=1
  if K>= len(S):
      return ''
  return S[K:K+N][::-1]
InvertStr("abcdef", 2, 3)
InvertStr("abcdef", 6, 10)
InvertStr("abcdef", 10, 3)  
