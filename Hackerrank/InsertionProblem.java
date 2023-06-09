package Hackerrank;
import java.util.*;

class InsertionProblem{
    public static void main(String[] args){
        List<Integer> list = new ArrayList();
        list.add(2);
        list.add(3);
        list.add(4);
        list.add(5);
        list.add(6);
        list.add(7);
        list.add(8);
        list.add(9);
        list.add(10);
        list.add(1);
        insertionSort(list);
    }
    public static void insertionSort1(int n, List<Integer> arr) {
        // n is the index where the unsorted element is present in the array
        // array arr is sorted other than one element at index n
        // problem => make the whole array sorted
        // solution => from n -> 0 scan each element if it is bigger than arr[n] or not if yes continue, if no stop and swap elements
        int scannable = arr.get(n-1); // 1
        int broken = -1;
        int i = 0;
        for(i = arr.size() - 2; i >= 0; i--){
            if(arr.get(i) > scannable) {
                arr.set(i + 1, arr.get(i));
            }
            else {
                broken = i;
                break;
            }
            System.out.println(arr.toString().replace(",", "").replace("[", "").replace("]", ""));
        }
        if(broken > -1){
            arr.set(broken + 1 , scannable);
        }
        else{
            arr.set(i + 1, scannable);
        }
        System.out.println(arr.toString().replace(",", "").replace("[", "").replace("]", ""));
    }
    public static void insertionSort(List<Integer> arr) {
        // n is the index where the unsorted element is present in the array
        // array arr is sorted other than one element at index n
        // problem => make the whole array sorted
        // solution => from n -> 0 scan each element if it is bigger than arr[n] or not if yes continue, if no stop and swap elements
        for(int i = 1; i < arr.size(); i++) {
            int key = arr.get(i);
            int j = i - 1;
            while(j >= 0 && arr.get(j) > key){
                arr.set(j + 1, arr.get(j));
                j = j - 1;
            }
            arr.set(j + 1, key);
            System.out.println(arr.toString().replace(",", "").replace("[", "").replace("]", ""));
        }

    }
}
