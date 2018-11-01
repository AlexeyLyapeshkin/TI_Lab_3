from math import sqrt
from itertools import count, islice



def testing(b,n,p=2,q=2):

    def isPrime(n):
        if n < 2: return False
        for number in islice(count(2), int(sqrt(n)-1)):
            if not n%number:
                return False
        return True


    if isPrime(p) and isPrime(q) and b < n and b > 0 and n > 256 : return True
    else: return False


def Cipher(filename,n,b):

    b_arr = []
    out_arr = []
    file_out = open(filename + '.cph', 'w')


    for byte in bytes_from_file(filename):
        out_arr.append(byte)
        b_arr.append((byte*(byte+b)) % n)
    for i in range(len(b_arr)):
        file_out.write(str(b_arr[i])+' ')
    file_out.close()
    return out_arr


def euclid(p,q):

    d0 = p
    d1 = q
    x0 = 1
    x1 = 0
    y0 = 0
    y1 = 1
    while d1 > 1:

        t = d0 // d1
        d2 = d0 % d1
        x2 = x0-t*x1
        y2 =y0-t*y1
        d0 =d1; d1=d2
        x0=x1; x1 =x2
        y0 = y1; y1 = y2

    return (x1,y1)

def FastEXP(number, stepen, modN):

    x = 1
    while stepen != 0:
        while (stepen % 2) == 0:
            stepen = stepen // 2
            number = (number * number) % modN
        stepen = stepen - 1
        x = (x * number) % modN

    return x



def bytes_from_file(filename, chunksize=8192):

    with open(filename, "rb") as f:
        while True:
            chunk = f.read(chunksize)
            if chunk:
                for b in chunk:
                    yield b
            else:
                break

def addMod(N,modn):

    result = N % modn
    if N < 0:
        result = modn + result

    return result

def read_from_f(file):

    f = open(file,'r')
    text = f.read()
    text = text.split()
    return text


def Decipher(filename,p,q,b):
    n = p*q

    index = filename.rfind('/')
    tep_filename = filename
    
    tep_filename = tep_filename[:index+1] + '[deciphered]' + tep_filename[index+1:]

    file_out = open(tep_filename[:len(tep_filename) - 4], 'wb')
    #print(tep_filename[:len(tep_filename) - 4])

    m_arr = []
    out_arr = bytearray()

    kek = read_from_f(filename)
    for byte in kek:

        byte = int(byte)
        D = (b**2 + 4*byte) % n

        mp = FastEXP(D,(p+1)//4,p)
        mq = FastEXP(D,(q+1)//4,q)

        yp, yq = euclid(p,q)

        ap = yp*p
        aq = yq*q

        d1 = (ap * mq + aq * mp) % n
        d2 = (n - d1) % n
        d3 = (ap * mq - aq * mp) % n
        d4 = (n - d3) % n
        list_d = [d1, d2, d3, d4]

        for d in list_d:

            if (d - b) % 2 == 0:
                m_arr.append(int(((-b + d) / 2) % n))
            else:
                m_arr.append(int(((-b + n + d) / 2) % n))

    for i in range(len(m_arr)):
        if m_arr[i] < 256:
            out_arr.append(m_arr[i])

    file_out.write(out_arr)
    file_out.close()

    return m_arr

