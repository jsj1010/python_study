
def ProCess():

    with open(r'sales.txt', mode='r', encoding='utf-8') as f:
        line = f.readline()
        print(f.read())

        while line:
                    lines = line.replace("," ,"   ")
                    if lines.startswith(line):
                        line = f.read()
                        print("사번  이름    기본급    근무년수  근속수당  공제액    수령액")
                        print(lines)
                        
                        for data in line:
                            print(
                                f"{data[0]:<4} " 
                                f"{data[1]:<6} "
                                f"{data[2]:<8} "
                                f"{data[4]:<8} "
                                f"{data[5]:<8} "
                                f"{data[6]:<8} "
                                f"{data[7]}"
                            )

if __name__ == '__main__':
    ProCess()
