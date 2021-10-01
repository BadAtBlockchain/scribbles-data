# for each chunk in the JSON file
# get the image data from the directory and base64 the contents
# store base64 into the JSON block and rewrite

import json
import base64

json_data = []

# load the image data and spit out as base64 string
def get_image_data(id):
    file_name = str(id) + ".svg"
    image_data = ""

    with open("scribble_images/" + file_name, 'rb') as image_file:
        image_data = image_file.read()

    return base64.b64encode(image_data)

def patch_json_data():
    final_json = []

    for scribble in json_data:
        print("[*] Processing Scribble #%s" % scribble["id"])

        enc_image_data = get_image_data(scribble["id"])
        scribble["image_data"] = enc_image_data.decode("utf-8") 

        final_json.append(scribble)

    return final_json
    

# main entrypoint
if __name__ == "__main__":
    with open('pre_allData.json') as json_file:
        json_data = json.load(json_file)

    patched_data = patch_json_data()

    with open('patched_data.json', 'w') as outfile:
        json.dump(patched_data, outfile, indent=4)

    with open('patched_data.min.json', 'w') as outfile:
        json.dump(patched_data, outfile)