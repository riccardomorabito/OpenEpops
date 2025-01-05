
<div align="center">
  <img src="https://raw.githubusercontent.com/riccardomorabito/OpenEpops/main/logo.png" alt="Logo" width="400">
</div>
</br>

# DMS to DD Documentation

## Introduction

The `DMStoDD` script is designed to convert geographical coordinates from Degrees, Minutes, and Seconds (DMS) format to Decimal Degrees (DD) format. The input coordinates are read from an input file, and the converted coordinates are written to an output file in the format required by FlightGear flight simulator.

## Functions

### `dms_to_dd(coordinate)`

This function takes a coordinate in Degrees, Minutes, and Seconds (DMS) format as input and returns the corresponding Decimal Degrees (DD) value.

#### Parameters:
- `coordinate`: A string representing the geographical coordinate in DMS format.

#### Returns:
- A floating-point number representing the coordinate in Decimal Degrees.

### `convert_coordinates(input_file, output_file)`

This function reads coordinates from an input file in DMS format, converts them to Decimal Degrees using `dms_to_dd` function, formats them according to FlightGear requirements, and writes the result to an output file.

#### Parameters:
- `input_file`: The path to the input file containing coordinates in DMS format.
- `output_file`: The path to the output file where the converted coordinates will be written.

## Output Format:
The output file will contain lines with space-separated values in the following format:
```
DD_LATITUDE DD_LONGITUDE XXXXX
```
- `DD_LATITUDE`: Decimal Degrees representation of latitude.
- `DD_LONGITUDE`: Decimal Degrees representation of longitude.
- `XXXXX`: Name of fix. Usually five characters. Unique within an ICAO region.

## Input Format:

The input file is expected to contain coordinates in the Degrees, Minutes, and Seconds (DMS) format. Typically, this information can be sourced from the ENAV website (for Personal and Non-Commercial Use Only), specifically in section ENR 4.4 within the Aeronautical Information Publication (AIP).

```plaintext
40°26'46.158"N 3°42'27.618"W AIRPT
38°47'8.956"S 62°12'54.552"E CITY1
```

### AIP ENR 4.4 Format

The input file is structured in a tabular or text format, where each line represents a set of geographical coordinates. The expected format for each line is as follows:

```
LATITUDE LONGITUDE XXXXX
```

- `LATITUDE`: Represents the latitude of a location in the Degrees, Minutes, and Seconds (DMS) format. It should be expressed as a string with the direction indicator ('N' for North or 'S' for South) at the end.
  
- `LONGITUDE`: Represents the longitude of a location in the Degrees, Minutes, and Seconds (DMS) format. It should be expressed as a string with the direction indicator ('E' for East or 'W' for West) at the end.

- `XXXXX`: This is an additional value associated with the geographical location. The script will take the first five characters of this value, convert it to uppercase, and include it in the output file.

## Usage

To use the script, run it with the appropriate input and output file paths. By default, the script is configured to read from "input.txt" and write to "output.txt". You can modify the file paths to suit your specific needs.

```python
if __name__ == "__main__":
    convert_coordinates("input.txt", "output.txt")
```

Make sure the input file contains coordinates in the required format, and the output file will be generated with the FlightGear-compatible coordinates.

## Useful Links

- **ENAV Online Services:**
  - [ENAV Online Services](https://www.enav.it/servizi-online) - Access the Online Services section of the Italian National Civil Aviation Authority (ENAV), where you can find the Aeronautical Information Publication (AIP) and other related resources.

- **X-Plane Intersection Fix DAT File Format:**
  - [X-Plane Docs](https://developer.x-plane.com/article/fix-intersection-fix-dat-file-format-specification/) - The file output format adheres to the specifications outlined in the DAT file format specification document for intersection fixes in the context of X-Plane development. Detailed information about the format can be found here.



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/riccardomorabito/OpenEpops](https://github.com/riccardomorabito/OpenEpops)