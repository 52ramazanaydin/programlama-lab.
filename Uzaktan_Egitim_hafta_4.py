#Heap durumuna sokmak için kullanılır heapteki elemanlar parentları ile karşılaştırılır.
#parametre olarak bir dizi ve bir index alır 
def min_heapify(array, i):
    left = 2 * i + 1
    right = 2 * i + 2
    length = len(array) - 1
    smallest = i
    if left <= length and array[i] > array[left]:
        smallest = left
    if right <= length and array[smallest] > array[right]:
        smallest = right
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        min_heapify(array, smallest)
        

#sırayla, parametre olarak gönderilen dizideki tüm elemanlara heapify uygular ve o diziyi heap haline getirir.
#parametre olarak dizi  alır
def build_min_heap(array):
    for i in reversed(range(len(array)//2)):
        min_heapify(array, i)

my_array = [8,10,3,4,7,15,1,2,16]


build_min_heap(my_array)
print("min heap yapılmış dizi = ", my_array)
print("\n")


#heapsort fonksiyonu, heapify ve build_heap ile diziyi sıralamak için kullanılır
#Liste küçükten büyüğe sıralanıp fonksiyondan döndürülür
#parametre olarak dizi alır
def heapsort(array):
    array = array.copy()
    build_min_heap(array)
    sorted_array = []
    for i in range (len(array)):
        array[0], array[-1] = array[-1], array[0]
        sorted_array.append(array.pop())
        min_heapify(array, 0)
    return sorted_array


# diziye, parametre olarak gönderilen değeri ekleyen fonksiyondur
#eğer ekleme yapıldıysa dizi yeniden heap haline getirilip geri döndürülecek
#parametre olarak hem dizi hem de sayı alır
def insertitemToHeap(my_heap, item):
    for i in range(len(my_heap)): #eğer gönderilen değer listede varsa ekleme yapmadan uyarı mesajı döndürür ve listeyi aynı şekilde return eder
        if my_heap[i] == item:
            print("Bu sayı heapde mevcut, listeye eklenemedi")
            return my_heap
    my_heap.append(item)
    build_min_heap(my_heap)
    return my_heap
    #return heapsort(my_heap) listeyi sıralı döndürmek için kullanırız


print(" heape eklenmiş hali = ", insertitemToHeap(my_array, 15))#sayı dizide olduğu için eklenmeyecek
print("\n")
print(" heape eklenmiş hali = ", insertitemToHeap(my_array, 40))
print("\n")
print("-----------------")
print("\n")


# en son elemanı silerek heap dizisini yeniden oluşturur.
#parametre olarak hem dizi hem de sayı alır
def removeitemFrom(my_heap):
    yeni_dizi = heapsort(my_heap)
    #print(yeni_dizi)
    yeni_dizi[0], yeni_dizi[-1] = yeni_dizi[-1], yeni_dizi[0]
    yeni_dizi.pop()
    build_min_heap(yeni_dizi)
    return yeni_dizi
    #return heapsort(yeni_dizi) eğer listeyi sıralı halde döndürür


print("ilk elemanı silinmiş dizi = ", removeitemFrom(my_array))
