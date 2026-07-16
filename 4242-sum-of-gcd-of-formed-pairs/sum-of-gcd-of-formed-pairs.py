import numpy

def gcdSum(
    nums: list[int],
    dtypes=(numpy.uint8,)*9 + (numpy.uint16,)*8 + (numpy.uint32,)*14
) -> int:        
    nums = numpy.asarray(nums, dtype=dtypes[max(nums).bit_length()])    
    numpy.gcd(numpy.maximum.accumulate(nums), nums, out=nums)
    nums.sort()
    half = len(nums) >> 1
    return numpy.gcd(nums[:half], nums[::-1][:half]).sum().item()    

Solution = repeat(namedtuple('Solution', ('gcdSum',))(gcdSum)).__next__
        
