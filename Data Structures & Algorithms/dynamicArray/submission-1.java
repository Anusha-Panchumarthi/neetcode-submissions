class DynamicArray {
    private int[] arr;
    private int capacity;
    private int length;
    public DynamicArray(int capacity) {
        this.arr = new int[capacity];
        this.capacity = capacity;
        this.length = 0;
    }

    public int get(int i) {
        return arr[i];
    }

    public void set(int i, int n) {
        arr[i] = n;
    }

    public void pushback(int n) {
        if(length >= capacity)
            resize();
        
        arr[length++] = n;
    }

    public int popback() {
        return arr[--length];
    }

    private void resize() {
        capacity *= 2;
        int[] arr1 = new int[capacity];

        for(int i = 0; i < length; i++)
        {
            arr1[i] = arr[i];
        }

        arr = arr1;
    }

    public int getSize() {
        return length;
    }

    public int getCapacity() {
        return capacity;
    }
}
