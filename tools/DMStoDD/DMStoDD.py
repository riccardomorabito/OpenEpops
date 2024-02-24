def dms_to_dd(coordinate):
    direction = 1
    if coordinate[-1] in ['S', 'W']:
        direction = -1

    parts = coordinate[:-1].split('°')
    degrees = float(parts[0])
    minutes = float(parts[1].split('\'')[0])
    seconds = float(parts[1].split('\'')[1].split('\'\'')[0])

    dd = direction * (degrees + minutes / 60 + seconds / 3600)
    return round(dd, 6)

def convert_coordinates(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    converted_coordinates = []

    for line in lines:
        parts = line.split()
        latitude = parts[0]
        longitude = parts[1]

        converted_lat = dms_to_dd(latitude)
        converted_long = dms_to_dd(longitude)

        # Formatting longitude with 000.000000 format
        converted_long = '{:010.6f}'.format(converted_long)


        # Creating FlightGear format for output
        output_line = f"{converted_lat:09.6f} {converted_long} {parts[2][:5].upper()}"

        converted_coordinates.append(output_line)

    with open(output_file, 'w', encoding='utf-8') as output_file:
        for line in converted_coordinates:
            output_file.write(line + '\n')

if __name__ == "__main__":
    convert_coordinates("input.txt", "output.txt")
