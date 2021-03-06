class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = collections.Counter()
        for e in answers:
            counter[e] += 1
        return sum([math.ceil(v / (k + 1)) * (k + 1) for k, v in counter.items()])
