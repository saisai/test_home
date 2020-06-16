'''
จงเขียนโปรแกรม เพื่ออ่ำนข้อควำมจำก txt file (“c:/test_read.txt” ) แล้ว print แสดงผลลัพธ์
โดยใหแสดงวำขอควำมนนมตวอักษรอะไรบ้ำง และมีจ ำนวนเท่ำไหร่
Ex. ข้อควำมใน txt file คือ Strategic Software Solution
Output : r = 2
o = 3
n = 1
l = 1
S = 3
i = 2
g = 1
f = 1
e = 2
c = 1
a = 2
w = 1
u = 1
t = 4
s = 1
โปรดดูหน้าถัดไป

Write a program To read the message from the txt file ("c: /test_read.txt") and print to show the results.
By showing the request for information, and what amount is the number?
Ex. Message in txt file is Strategic Software Solution.
Output: r = 2
o = 3
n = 1
l = 1
S = 3
i = 2
g = 1
f = 1
e = 2
c = 1
a = 2
w = 1
u = 1
t = 4
s = 1
Please see the next page.

'''
def read_file(filename):

    results = open(filename, 'r').read()

    wordlist = results.split()

    

    wordfreq = {}

    for word in wordlist:
        for w in word:
            wordfreq[w] = 1 + wordfreq.get(w,0)

            

    for key, val in wordfreq.items():
        print('%s = %s' % (key, val))



if __name__ == "__main__":

    read_file("test_read.txt")
