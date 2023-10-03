#import the necessary libraries
import json
#needed to list the files in the directories
import os

#tests contains the JSON files and subdirectories
directory = 'test'

#os.walk is used to traverse through the directory
#recursively loop through the files in the directory and its subdirectories
for root, dirs, files in os.walk(directory):
     for filename in files:
          #check to see if it's a JSON file
          if filename.endswith('.json'):
            #construct the path to reach the JSON
            file_path = os.path.join(root, filename)
            print(f'Parsing {file_path} ')

            #opening the JSON files
            try:
                #Open the JSON file
                with open(file_path) as file:
                    #Parse the file
                    data = json.load(file)
                    print(f'Parsed JSON from {filename}: {data} \n')
            except json.JSONDecodeError as e:
                #Handle decoding errors in invalid JSON files
                print(f'Error Parsing {filename}: {str(e)} \n')
