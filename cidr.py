import sys 

if __name__ == "__main__":
    try:
        cidr = int(sys.argv[1].replace("/", ""))
        toalHost = 1
        if cidr > 0 and cidr < 33:
            subnetmask= ["0","0","0","0"]
            temp = cidr // 8
            if cidr % 8 == 0:
                for i in range(temp):
                    subnetmask[i]= "255"
                for j in subnetmask:
                    if j == "0":
                        toalHost*= (2**8)
            else:
                arr = [128 ,64 ,32 ,16 ,8 ,4 ,2 ,1]
                borrow = 0
                for i in range(temp):
                    subnetmask[i] = "255"
                module = cidr % 8
                for j in range(module):
                    borrow+= arr[j]
                subnetmask[temp] = str(borrow)
                
                for host in subnetmask:
                    if host != "255" and host != "0":
                       toalHost*= 2**(8-module)
                    elif host == "0":
                        toalHost*= 2**8
            print(f'[+] Subnetmask => {".".join(subnetmask)}')
            print(f'[+] Total Host => {toalHost}')
        else:
            print("[-]Prefix greater than 0 and less than 33")
            sys.exit()

    except IndexError:
        print("[-]python3 cidr.py <cidr>")
        print("[-]Exmaple: python cidr.py /24")
        sys.exit()