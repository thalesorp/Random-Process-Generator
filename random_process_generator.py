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

import random
from pathlib import Path

class RandomProcessGenerator():
    '''Main class of this project.'''

    PREFIX = "My-test-dataset"
    DIVIDER = "_"
    SUFFIX = ".text"

    def __init__(self):
        random.seed(1)

    def run(self):

        process_quantity = [5, 25, 50, 100]

        FOLDERS = ["Scenarios\\My test dataset 1 - 50-50 low and high bursts\\",
                   "Scenarios\\My test dataset 2 - 20-80 low and high bursts\\",
                   "Scenarios\\My test dataset 3 - 80-20 low and high bursts\\"]

        bursts_percentage = [[50, 50], [20, 80], [80, 20]]

        for i in range(len(FOLDERS)):
            for j in range(len(process_quantity)):

                low_burst_percentage = bursts_percentage[i][0]
                high_burst_percentage = bursts_percentage[i][1]

                final_file_name = FOLDERS[i] + self.PREFIX + self.DIVIDER + "Case-" + str(j+1) + self.DIVIDER + str(process_quantity[j]) + "-processes" + self.SUFFIX
                self.generate_scenario(FOLDERS[i], final_file_name, process_quantity[j], low_burst_percentage, high_burst_percentage)

    def generate_scenario(self, folder, final_file_name, process_quantity, low_burst_percentage, high_burst_percentage):

        print("\nGenerating scenario...")
        print("  final file name:", final_file_name)
        print("  process_quantity:", process_quantity)
        print("  low_burst_percentage:", low_burst_percentage)
        print("  high_burst_percentage:", high_burst_percentage)

        Path(folder).mkdir(parents=True, exist_ok=True)

        f = open(final_file_name, "w+")

        try:
            f.write("################################################################################\n")
            f.write("#                                                                              #\n")
            f.write("#  Dataset randomly generated                                                  #\n")
            f.write("#                                                                              #\n")
            f.write("################################################################################\n\n")
            f.write("# Process quantity: " + str(process_quantity) + " \n")
            f.write("# Low burst percentage: " + str(low_burst_percentage) + " \n")
            f.write("# High burst percentage: " + str(high_burst_percentage) + " \n\n")
            f.write("# P [identifier] [arrival] [burst]\n\n")

            bursts = self.generate_bursts(process_quantity, low_burst_percentage, high_burst_percentage)

            for i in range(process_quantity):
                #if random.randint(0, 10)
                arrival = 0
                burst = bursts[i]
                f.write("P " + str(i+1) + " " + str(arrival) + " " + str(burst) + "\n")

        finally:
            f.close()

    def generate_bursts(self, process_quantity, low_burst_percentage, high_burst_percentage):
        '''Generates the burst time of processes.'''

        low_bursts_quantity = (process_quantity * low_burst_percentage) // 100
        high_bursts_quantity = (process_quantity * high_burst_percentage) // 100

        bursts = list()

        # Generate low bursts
        for _ in range(low_bursts_quantity):
            bursts.append(random.randint(0, 10))

        # Generate high bursts
        for _ in range(high_bursts_quantity):
            bursts.append(random.randint(10, 200))

        # When process quantity it's odd, generate a new one
        if process_quantity % 2 == 1:
            # There are 50-50% chance of generating a low or high burst
            if random.randint(0, 1) % 2 == 0:
                bursts.append(random.randint(0, 10))
            else:
                bursts.append(random.randint(10, 200))


        random.shuffle(bursts)
        return bursts

################################################################################

RandomProcessGenerator().run()
