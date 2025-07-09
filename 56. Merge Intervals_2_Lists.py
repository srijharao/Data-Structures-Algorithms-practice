def merge_result(result, arr, i):
    if result[-1][1] >= arr[i][0]:
        result[-1][1] = max(result[-1][1], arr[i][1])
    else:
        result.append(arr[i])


def merge_intervals(A,B):

  lenA = len(A)
  lenB = len(B)
  result = []


  i,j = 0,0
  if lenA > 0 and lenB > 0:
    if A[0][0] < B[0][0]:
      result = [A[0]]
      i += 1
    else:
      result = [B[0]]
      j += 1
  else:
    result = [A[0]] if lenA>0 else [B[0]]

  while i < lenA and j < lenB:
    if A[i][0] < B[j][0]:
      merge_result(result, A, i)
      i += 1
    else:
      merge_result(result, B, j)
      j += 1

    
  while i < lenA:
    merge_result(result,A,i)
    i += 1

  while j < lenB:
    merge_result(result,B,j)
    j += 1

  return result
