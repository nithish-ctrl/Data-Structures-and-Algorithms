
def job_sequencing(N, jobs):
    jobs = list(jobs)
    jobs.sort(key=lambda x: (x[2]), reverse=True)
    #print(jobs)
    job_seq = []
    prof_val = 0
    count=0
    for idx,job in enumerate(jobs):
        if job[1] > idx :
            count+=1
            prof_val+=job[2]
        else : continue
        job_seq.append((count,prof_val))
    return f'The number of possible jobs and total profit is : {max(job_seq)}'


'''
N = 4
Jobs = {(1, 4, 20), (2, 1, 10), (3, 1, 40), (4, 1, 30)}  
print(job_sequencing(N,Jobs))    

N = 5
Jobs = {(1, 2, 100), (2, 1, 19), (3, 2, 27), (4, 1, 25), (5, 1, 15)}  
print(job_sequencing(N,Jobs))   

N = 4
Jobs = {(1, 3, 25), (2, 3, 35), (3, 2, 45), (4, 1, 30)}  
print(job_sequencing(N,Jobs)) 
'''

