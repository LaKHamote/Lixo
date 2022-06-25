class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        tmp = self.head
        lstr = ''
        while tmp != None:
            lstr += str(tmp.data) + ' '
            tmp = tmp.getNext()
            
        return lstr

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext()) 

def removerSegundaOcorrencia(L,n):
    temp = UnorderedList()
    resp = UnorderedList()
    flag = False
    flag2 = True
    for i in str(L).split():
        if flag and i == str(n):
            flag2 = False
            flag = False
        elif flag2 and i == str(n):
            temp.add(i)
            flag = True
        else:
            temp.add(i)
    [resp.add(k) for k in str(temp).split()]
    return resp
    
    

	
L = UnorderedList()
L.add(42)
L.add(42)
L.add(42)
L = removerSegundaOcorrencia(L, 42)
L = removerSegundaOcorrencia(L, 42)
print(f'Lista: {L}')