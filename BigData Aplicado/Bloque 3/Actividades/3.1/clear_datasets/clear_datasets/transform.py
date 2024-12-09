import pandas as pd
import argparse

def main():
	# Create an argument parser and read the arguments
	parser = argparse.ArgumentParser(description="Process a URL.")
	parser.add_argument("url", type=str, help="The URL to process")
	parser.add_argument(
      "-o", "--output", 
      type=str, 
      help="Output file name for the cleaned data (default: cleaned_data.csv)"
    )
	args = parser.parse_args()
	url = args.url
	output_file = args.output

	# Just in case, check if the url is one to a CSV file
	if not url.lower().endswith('.csv'):
		raise ValueError("Error: The URL provided is not valid. This program requires a CSV file URL as argument.")
	
	# Set a default value to the output file in case is not defined
	if not output_file: output_file = url.split('/')[-1]
	if not output_file.endswith('.csv'): output_file += '.csv' # Just in case

	# Load the datasets from URL
	data = pd.read_csv(url, sep='\t')
	cleaned_data = data.dropna()
	# Save the data into datasets/ directory
	cleaned_data.to_csv(f'datasets/{output_file}', index=False, sep='\t')
	print(f"Cleaned data has been saved to 'datasets/{output_file}'")

if __name__ == "__main__":
	main()