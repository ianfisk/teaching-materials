import random

# PROMPT: Read the following blocks of code and write down their output by hand.

####################################

# Block 1
i = 0
while i < 10:
    print(i)
    i += 1

####################################

# Block 2
j = 0
while j < 15:
    if (j % 2 == 0):
        print(j)
    j += 1

####################################

# Block 3
# Give TWO POSSIBLE outputs of this program.
def is_job_done():
    random_number = random.random()
    return random_number >= 0.5

while not is_job_done():
    print("Job not done. Continuing")

print("All work done")
