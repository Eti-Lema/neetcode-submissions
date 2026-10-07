class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> groups = new HashMap<>();

        for (int i = 0; i < strs.length; i++){
            String currWord = strs[i];

            char[] chars = currWord.toCharArray();
            Arrays.sort(chars);
            String sorted = String.valueOf(chars);

            groups.computeIfAbsent(sorted, k -> new ArrayList<>()).add(currWord);
        }

        return new ArrayList<>(groups.values());
    }
}
