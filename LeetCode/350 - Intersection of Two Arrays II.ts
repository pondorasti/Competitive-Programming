// Lookup/Search -> x in nums1 exist O(n)

function intersect(nums1: number[], nums2: number[]): number[] {
  const freq1 = new Object()
  nums1.forEach((val) => {
    if (freq1[val] === undefined) {
      freq1[val] = 1
    } else {
      freq1[val] += 1
    }
  })

  const ans: number[] = []
  nums2.forEach((val) => {
    if (freq1[val] > 0) {
      freq1[val] -= 1
      ans.push(val)
    }
  })

  return ans
}
