import os, errno

def gen_contacts(a, b):
    
    address = '@none.com'
    name = 'name'
    L = []
    
    for i in range(a, b):
         result_contact = name + '{0:03}'.format(i) + address
         L.append(str(result_contact))

    return L

def write_txt(L, type):

    try:
        count = 0
        list_len = len(L)

        with open('contacts.txt','wb') as f:
            for i in L:
                if int(type) == 0:
                    count += 1
                    if count == list_len:
                        f.write(i)
                    else:
                        f.write(i + ',')
                else:
                    f.write(i + '\r\n')

    except Exception, err:
        sys.stderr.write('ERROR: %s\n' % str(err))
        raise

if __name__ == '__main__':

    list_contacts = gen_contacts(1, 201)
    write_txt(list_contacts , 0)
    
