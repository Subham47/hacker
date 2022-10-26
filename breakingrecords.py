

def breakingRecords():
    scores = list(map(int,input().split())) 

    lowest=scores[0]
    highest=scores[0]
    lowest_count=0
    highest_count=0
    for score in scores:
        if score<lowest:
            lowest=score
            lowest_count+=1
        if score>highest:
            highest=score
            highest_count+=1
            
    return(str(highest_count)+" "+str(lowest_count))


