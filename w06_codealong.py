#open the file
with open("hr_system.txt") as hr_file:
    next(hr_file)

    #read through the file line by line
    for line in hr_file:

        #get the various part of the record
        parts = line.split(" ")

        name = parts[0]
        id = int(parts[1])
        job_title = parts[2]
        salary = int(parts[3])

        paycheck_amount = salary / 24

        if "engineer" in job_title.lower():
            paycheck_amount = paycheck_amount + 1000


        #Alexia (ID: 1913), Engineer - $84000.00
        #print out the values
        print(f"{name} (ID: {id}), {job_title} - ${paycheck_amount:.2f}")