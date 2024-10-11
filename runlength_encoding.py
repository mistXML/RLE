def decode(encoded):
    decoded = []
    for i in range(len(encoded)):
        try:
            decoded.append(int(encoded[i])*encoded[i+1])
        except:
            continue
    return "".join(decoded)


def encode(unencoded):
    encoded = []
    skip_iterations = 0

    for i in initial:
        if skip_iterations > 0:
            skip_iterations -= 1
            continue
        else:
            encoded.append(str(unencoded.count(i)) + i)
            skip_iterations = unencoded.count(i)-1

    return "".join(encoded)

initial = input("Enter your encoded or unencoded string here: ")
algorithm_choice = input("Encode or decode? ")

while algorithm_choice.lower() != "encode" and algorithm_choice.lower() != "decode":
    algorithm_choice = input("Invalid choice, encode or decode?")

if algorithm_choice.lower() == "encode":
    print(encode(initial))
elif algorithm_choice.lower() == "decode":
    print(decode(initial))
