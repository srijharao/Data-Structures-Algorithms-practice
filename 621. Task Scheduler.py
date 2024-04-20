class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # n + 1: columns: max frequency elements + n intervals after
        # (max_freq -1): rows excluding last row, because last row can have multiple max_freq elements
        # ans is the min elements we need. anything remaining can be added at the end

        mp = Counter(tasks)
        frequencies = mp.values()
        max_frequency = max(frequencies)
        all_high_freq_elements = 0
        for i in mp.keys():
            if mp[i] == max_frequency:
                all_high_freq_elements += 1
        

        ans = (n+1) * (max_frequency-1) + all_high_freq_elements

        return max(ans, len(tasks))
