#!/usr/bin/env python3

################################################################################
#                                                                              #
#  Random process generator                                                    #
#                                                                              #
#  Author: Thales Otávio                                                       #
#  Contact: @ThalesORP | ThalesORP@gmail.com                                   #
#                                                                              #
################################################################################

'''Root file of this project.'''

import sys
from numpy import random
from math import ceil

processes_quantity = sys.argv[1]

random.seed()

zero_arrival_file_name = "Case-" + processes_quantity + "-processes_zero-arrival-time.txt"
non_zero_arrival_file_name = "Case-" + processes_quantity + "-processes_non-zero-arrival-time.txt"

print("Generating scenario with " + processes_quantity + " processes...")

header = "################################################################################\n"
header += "#                                                                              #\n"
header += "#  Dataset randomly generated                                                  #\n"
header += "#                                                                              #\n"
header += "################################################################################\n\n"
header += "# Process quantity: " + str(processes_quantity) + " \n\n"
header += "# P [identifier] [arrival] [burst]\n\n"

processes_quantity = int(processes_quantity)
bursts = 1 + random.exponential(scale=20.0, size=processes_quantity)

arrivals = 1 + random.exponential(scale=20.0, size=processes_quantity)

zero_arrival_output = ""
non_zero_arrival_output = ""

for i in range(processes_quantity):

    burst = ceil(bursts[i])
    arrival = ceil(arrivals[i])

    zero_arrival_output += "P " + str(i+1) + " 0 " + str(burst) + "\n"
    non_zero_arrival_output += "P " + str(i+1) + " " + str(arrival) + " " + str(burst) + "\n"

with open(zero_arrival_file_name, "w") as file_:
    file_.write(header)
    file_.write(zero_arrival_output)

with open(non_zero_arrival_file_name, "w") as file_:
    file_.write(header)
    file_.write(non_zero_arrival_output)
