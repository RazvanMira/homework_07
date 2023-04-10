print("The programme ends when you press Enter.")
total_time = 0
average_time = 0 
number_of_runs = 0

more_runs = True
while more_runs:
    run_time = input("Enter 10 km run time: ")
    if run_time == "":
        more_runs = False
    else:
        run_time = int(run_time)
        total_time = total_time + run_time
        number_of_runs = number_of_runs + 1
        average_time = total_time / number_of_runs

print("Average of " + "{:.2f}".format(average_time) + " over " + str(number_of_runs) + " runs.")