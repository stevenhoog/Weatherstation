import random

threshold = 3


def CreateData(data):

    # Show data passed to function
    print(f"Data: {data}")

    # Convert ints to 8 bit binary
    binary = []
    for i in data:
        # First convert the data
        binary.append('{0:08b}'.format(i))
        print(f"Data byte: {binary[-1]}")

    # Create parity byte
    if(random.randint(0, 1) is 0):
        # Create valid parity byte
        new_var = sum(data)
        binary.append('{0:08b}'.format(new_var))
    else:
        # Create invalid parity byte
        binary.append("00000000")

    # Log the parity byte
    print(f"Parity byte: {binary[-1]}")

    # Combine all bytes so it's easier to loop over
    bytesCombined = "".join(binary)
    print(f"Bytes combined: {bytesCombined}")

    # Start the output with random amount of 0's
    output = [0] * random.randint(5, 9)

    # Loop over all the bits
    for c in bytesCombined:
        if(c == '1'):
            # If bit is 1 create a between 5 and 9 1's
            length = random.randint(threshold + 1, 9)
        else:
            # If bit is 0 create a between 3 and 5 1's
            length = random.randint(1, threshold)

        # Add the data to the output
        output.extend([1] * length)
        # Space out the actual data with a divider of 5 0's
        output.extend([0] * 5)

    # Fill the output at the end with 0's
    output.extend([0] * (500 - len(output)))

    # Make a string out of the list for easy printing
    printOutput = "".join("{0}".format(n) for n in output)
    print(f"Output data: {printOutput}")
    print(f"Output data length: {len(printOutput)}")

    return output
