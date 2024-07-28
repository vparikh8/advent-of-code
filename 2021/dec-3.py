import logging
import os
import time
from collections import Counter


logging.basicConfig(format="%(asctime)s.%(msecs)03d:%(levelname)s:%(name)s:\t%(message)s", 
                    datefmt='%H:%M:%S')
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)

def main():
    input_file = "input.txt"
    with open(input_file, mode="rt") as f:
        data = f.read().splitlines()
    
    # Part 1
    transposed = list(zip(*data))   # transpose to get list of columns
    
    most_common_bits = "".join([Counter(current_col).most_common()[0][0] for current_col in transposed])
    logger.debug("Gamma rate: %s", most_common_bits)
    least_common_bits = "".join([Counter(current_col).most_common()[-1][0] for current_col in transposed])
    logger.debug("Epsilon rate: %s", least_common_bits)
    
    logger.info("Part 1: Product = %d\n", int(most_common_bits, 2) * int(least_common_bits, 2))
    
    # Part 2
    filter_with_most_common = int(filter_diag_vals(data), 2)
    logger.debug("Oxygen sensor rating = %s", filter_with_most_common)

    filter_with_least_common = int(filter_diag_vals(data, least_common=True), 2)
    logger.debug("CO2 scrubber rating = %s", filter_with_least_common)
    
    logger.info("Part 2: Product of O2 and CO2 ratings = %d\n", 
                filter_with_most_common * filter_with_least_common)

def filter_diag_vals(diag_values: list[str], least_common=False):
    diag_value_len = len(diag_values[0])
    
    # Process each digit
    for diag_posn in range(diag_value_len):
        count_of_1 = count_of_0 = 0
        
        # loop through each value to find most common / least common digit
        for diag_val in diag_values:
            if diag_val[diag_posn] == "1":
                count_of_1 += 1
            else:
                count_of_0 += 1
        
        keep = "1"  # default for most common, i.e. if equal count of 1s and 0s
        if count_of_0 > count_of_1:
            keep = "0"
            
        if least_common:    # invert if we want least common
            keep = "1" if keep == "0" else "0"
        
        # eliminate the diag values that don't match the criteria
        diag_values = [diag_val for diag_val in diag_values if diag_val[diag_posn] == keep]
        if len(diag_values) == 1:
            break
            
    return diag_values[0] 

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    logger.info("Execution time: %0.4f seconds", t2 - t1)