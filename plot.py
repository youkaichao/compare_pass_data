import time
import matplotlib.pyplot as plt
import example

def measure_time(data_size):
    # Generate a dictionary of the given size
    # data = {i: i for i in range(data_size)}

    from example import IntMap
    data = IntMap()
    for i in range(data_size):
        data.insert(i, i)
    
    # Measure start time
    start_time = time.time()
    
    # Call the function
    example.pass_data(data)
    
    # Measure end time
    end_time = time.time()
    
    # Return the time taken
    return end_time - start_time

# Data sizes to test
data_sizes = [int(1e2), int(1e3), int(1e4), int(1e5), int(1e6), int(1e7)]
# Store times for each data size
times = []

# Measure time for each data size
for size in data_sizes:
    elapsed_time = measure_time(size)
    times.append(elapsed_time)
    print(f"Data size: {size}, Time taken: {elapsed_time:.4f} seconds")

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(data_sizes, times, marker='o', linestyle='-', color='b')
plt.xlabel('Number of Entries in Dictionary')
plt.ylabel('Time Taken (seconds)')
plt.title('Execution Time of example.pass_data(data) by Dictionary Size')
plt.xscale('log')
plt.yscale('log')
plt.grid(True, which="both", ls="--")
plt.show()
