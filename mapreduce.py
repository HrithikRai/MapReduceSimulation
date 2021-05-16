def mapper():
    map_data = open(r"purchases.txt")
    map_data.seek(0)
    with open("inter_rec.txt","w") as file:
        for line in map_data:
            map_ln = line.strip().split("\t")
            if len(map_ln) == 6:
                date,time,store,item,cost,payment = map_ln
                file.write("{}\t{}\n".format(store,cost))
                
def sort():
    inter_rec = open(r"inter_rec.txt")
    inter_rec.seek(0)
    sorted = []
    for line in inter_rec:
        sorted.append(line)
        
    sorted.sort()
    with open("inter_rec.txt","w") as file:
        file.truncate(0)
        file.seek(0)
        for i in sorted:
            file.write("{}\n".format(i))
            
def reducer():
    salestotal = 0.0
    oldkey = None
    reduce_data = open(r"inter_rec.txt")
    reduce_data.seek(0)
    with open("MapReduced.txt","w") as file:
        for line in reduce_data:
            red_ln = line.strip().split("\t")
            if len(red_ln) != 2:
                continue
            thiskey,thisvalue = red_ln
            if oldkey and oldkey!=thiskey:
                file.write("{}\t{}\n".format(oldkey,salestotal))
                salestotal = 0
            oldkey = thiskey
            salestotal = salestotal + float(thisvalue)
        file.write("{}\t{}".format(oldkey,salestotal))
            
        
            
