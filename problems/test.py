def solution(A):
  """Your solution goes here."""
  sys.stderr.write('Tip: Use sys.stderr.write() to write debug messages on the output tab.\n')
  def tree_search(nums1, nums2, B):
    if not B:
      return abs(sum(nums1) - sum(nums2))
    return min(tree_search(nums1 + [B[0]], nums2, B[1:]), tree_search(nums1, nums2 + [B[0]],B[1:]))
  return tree_search([],[]. A)