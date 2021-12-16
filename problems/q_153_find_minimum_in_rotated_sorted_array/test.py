def solution(A):
  """Your solution goes here."""
  sys.stderr.write('Tip: Use sys.stderr.write() to write debug messages on the output tab.\n')
  def b_search(sublist1, sublist2, B):
    if not B: return sum(sublist1) - sum(sublist2)
    return min(b_search(sublist1 + B[0], sublist2, B[1:]), b_search(sublist1, sublist2 + B[0], B[1:]))
  return b_search([], [], A) 
