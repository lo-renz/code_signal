public class sortByHeight {
    /*
        Possible solution:
            Sort the list using linar search. If the number -1 is encountered then skip it.
    */

    int[] solution(int[] a) {
        int n = a.length;
        for(int i = 1; i < n; i++) {
            int key = a[i];
            int j = i - 1;
        
            while(j >= 0 && a[j] > key) {
                a[j + 1] = a[j];
                j = j - 1;
            }
            a[j + 1] = key;
        }
        return a;
    }
    
    public static void main(String[] args) {
        int[] a = new int[]{ 150, 190, 170, 160, 180};
        sortByHeight test = new sortByHeight();
        int[] sorted_list = test.solution(a);
        for(int i = 0; i < a.length; i++) {
            System.out.println(sorted_list[i]);
        }
    }
}