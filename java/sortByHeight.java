public class sortByHeight {
    /*
        Possible solution:
            Sort the list using linar search. If the numer-1 is encountered then skip it.
    */

    int[] sorting_list(int[] a) {
        int[] to_sort_list = new int[a.length];

        for(int i = 0; i < a.length; i++) {
            if(a[i] != -1) {
                to_sort_list[i] = a[i];
            }
        }

        return to_sort_list;
    }

    int[] solution(int[] a) {
        int[] list_to_sort = new int[a.length];

        int i = 0;
        for(int j = 1; i < a.length; i++) {
        }
    }
    
    public static void main(String[] args) {
        int[] a = new int[]{-1, 150, 190, 170, -1, -1, 160, 180};
        sortByHeight test = new sortByHeight();
        
        // testing for index list
        /*int[] index_list = test.index_search(a);
        for(int i = 0; i < index_list.length; i++) {
            System.out.println(index_list[i]);
        }*/

        // testing for sorting list
        int[] list_to_sort = test.sorting_list(a);
        for(int i = 0; i < list_to_sort.length; i++) {
            System.out.println(list_to_sort[i]);
        }
    }
}