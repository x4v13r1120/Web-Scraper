import json
# Code from Josiah Greenwell of FGCU

def transform():
# starting cleaning process
    comment = False
    with open("data/jsondata.json", 'r') as infile, open("data/cleaned_data.json", 'w') as \
            outfile:
        for line in infile:
            if line.startswith("/*"):
                comment = True
                continue
            elif line.startswith("*/"):
                comment = False
                continue
            elif comment:
                continue
            if len(line.strip()) > 0:
                if not line.strip().startswith("//"):
                    if not comment:
                        outfile.write(f"{line}\n")
                        print("Transformation Complete.")


