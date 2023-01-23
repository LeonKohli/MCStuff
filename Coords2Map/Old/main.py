# Initialize an empty list to store the records
records = []

# Read the input data line by line
with open('Coords.txt', 'r') as input_file:
    # Read the first line and extract the name
    name = input_file.readline().strip().split('\n')[0]
    
    # Skip the second line
    next(input_file)
    
    for line in input_file:
        x, z = line.strip().split(',')
        records.append([x, z])

# Write the data to a new output file
with open('output.txt', 'w') as output_file:
    # Write the fixed rows at the beginning of the file
    output_file.write('#\n')
    output_file.write('#waypoint:name:initials:x:y:z:color:disabled:type:set:rotate_on_tp:tp_yaw:visibility_type\n')
    output_file.write('#\n')
    
    # Write the data in `records` to the output file
    for i, (x, z) in enumerate(records):
        # Generate the initials for the waypoint
        initials = str(i+1)
        
        # Write the waypoint data to the output file
        output_file.write(f'waypoint:{i+1}{name}:{initials}:{x}:60:{z}:14:false:0:gui.xaero_default:false:0:0\n')

print("Done")
