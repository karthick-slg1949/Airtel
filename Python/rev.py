def list_reverse(arr,size):
    if (size==1):
        return arr
    elif(size==2):
        arr[0],arr[1]=arr[1],arr[0]
        return arr
    else:
        i=0
        while(i<size//2):
                arr[i],arr[size-i-1]=arr[size-i-1],arr[i]
                if ((i!=i+1 and size-i-1)!=size-i-2) and (i!=size-i-2 and size-i-1!=i+1):
                     arr [i+1],arr[size-i-2]=arr[size-i-2],arr[i+1]
                     i+2
                     return arr
                arr=[1,2,3,4,5]
                size=5
                print('original list:',arr)
                print("Reversed list:",list_reverse(arr,size))
                


            
