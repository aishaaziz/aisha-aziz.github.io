import csv
import json

def csv_to_nested_json(csv_file_path, json_file_path):
    data = {}

    with open(csv_file_path, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            origin_name = row['Origin']
            origin_country = row['origin_country']
            origin_lat = float(row['origin_lat'])
            origin_lon = float(row['origin_lon'])
            destination = {
                "name": row['Destination'],
                "lat": float(row['dist_lat']),
                "lon": float(row['dist_lon'])
            }
            transit = {
                "name": row['Transit'],
                "lat": float(row['tran_lat']),
                "lon": float(row['tran_lon'])
            }
            
            if origin_name not in data:
                data[origin_name] = {
                    "origin": {"name": origin_name, "country": origin_country,"lat": origin_lat, "lon": origin_lon},
                    "destinations": [],
                    "transit": transit
                }
            
            data[origin_name]["destinations"].append(destination)
    
    # Convert the dictionary to a list of dictionaries for JSON output
    output = list(data.values())

    with open(json_file_path, mode='w') as jsonfile:
        json.dump(output, jsonfile, indent=4)

# Example usage
csv_file_path = 'SalamAir_Destinations.csv'
json_file_path = 'output.json'
csv_to_nested_json(csv_file_path, json_file_path)
