class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> freq = new HashMap<>();

        for (int num : nums){
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }

        List<Integer> numsList = new ArrayList<>(freq.keySet());
        numsList.sort((a, b) -> freq.get(b) - freq.get(a));

        int[] result = new int[k];

        for (int i = 0; i < k; i++){
            result[i] = numsList.get(i);
        }

        return result;
    }
}
