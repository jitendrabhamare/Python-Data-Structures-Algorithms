## Greedy Algorithm that minimizes the weighted sum of completion times. 
## Author: Jitendra Bhamare

"""
The input file describes a set of jobs with positive and integral weights and lengths. It has the format

[number_of_jobs]
[job_1_weight] [job_1_length]
[job_2_weight] [job_2_length]
...

Aim is to run the greedy algorithm that schedules jobs in decreasing order of the difference (weight - length).
If two jobs have equal difference (weight - length), you should schedule the job with higher weight first. 
"""

## Load input file in the form of tuples (w,l,(w-l)) of array
input_file = 'jobs.txt'
with open (input_file) as f:
    num_job = f.readline()
    num_job = int(num_job.rstrip('\n'))
    print(num_job)
    wl_list = []
    for item in f:
        item = item.split()
        w = int(item[0])
        l = int(item[1])
        diff = w - l
        tup = (diff, w,l)
        wl_list.append(tup)
    wl_list.sort(reverse=True)

#print(wl_list)

comp_time = 0
weighted_sum = 0
#count = 0
for tup in wl_list:
    (diff, w, l) = tup
    comp_time += l
    weighted_sum += w*comp_time 

print(weighted_sum)


        
