#!/usr/bin/env python3
# Code copied, adapted and modified from https://github.com/faskowit/app-fmri-2-mat/blob/0.1.1/generate_cm_datatype.py, owner Josh Faskowitz

import json
import os
import shutil

## make output directory
if not os.path.exists("cm/csv"):
    os.makedirs("cm/csv")

## load config file for brainlife
with open('config.json') as config_file:
    config = json.load(config_file)

## input csv file of connectivity matrix data
input_csv = input_csv = "%s/output/%s.csv" %(config["matrices"],config["measure"])

## generate labels data
labels = [ {"name": "self-loop", "desc": "index(x,x) is the diagonal"} ]

# loop through key.txt file to pull parcellation label information data
catalog = dict()
with open(config["key"]) as key_file:
    key_lines = key_file.readlines();
    for line in key_lines:
        tokens = line.split("\t")
        label = tokens[0]
        parcellation = tokens[2]
        name_comp = tokens[3].split(" ") #== rh.R_V4t_ROI.label \n
        name = name_comp[1]
        catalog[parcellation] = {"name": name, "label": label, "voxel_value": int(parcellation)}
        labels.append(catalog[parcellation])

# freesurfer subcortical labels
f14 = [
        {"name": "Freesurfer Aseg / Left thalamus", "label": "10"},
        {"name": "Freesurfer Aseg / Left caudate", "label": "11"},
        {"name": "Freesurfer Aseg / Left putamen", "label": "12"},
        {"name": "Freesurfer Aseg / Left pallidum", "label": "13"},
        {"name": "Freesurfer Aseg / Left hippocampus", "label": "17"},
        {"name": "Freesurfer Aseg / Left amygdala", "label": "18"},
        {"name": "Freesurfer Aseg / Left accumbens", "label": "26"},

        {"name": "Freesurfer Aseg / Right thalamus", "label": "49"},
        {"name": "Freesurfer Aseg / Right caudate", "label": "50"},
        {"name": "Freesurfer Aseg / Right putamen", "label": "51"},
        {"name": "Freesurfer Aseg / Right pallidum", "label": "52"},
        {"name": "Freesurfer Aseg / Right hippocampus", "label": "53"},
        {"name": "Freesurfer Aseg / Right amygdala", "label": "54"},
        {"name": "Freesurfer Aseg / Right accumbens", "label": "58"},
    ]

# append subcortical labels to labels array
idx=0
for parc in range(1,len(f14)+1):
    labels.append({"name": f14[idx]["name"], "label": f14[idx]["label"], "voxel_value": int(len(key_lines)+parc)}) 
    idx+=1

## generate index data
index_output = [
        {
            "filename": "cm/csv/correlation.csv",
            "unit": "r",
            "name": "connectivity matrix of %s" %config["measure"],
            "desc": "The connectivity matrix of %s" %config["measure"]
            }
        ]

## output connectivity matrix to correlation.csv
# input connectivity matrix data
with open(input_csv) as cm_csv:
    cm_lines = cm_csv.readlines()

# output data to correlation.csv
with open("cm/csv/correlation.csv", "w") as cm_csv:
    csv = []
    for line in cm_lines:
        line = line.strip().split(",")
        csv.append(",".join(line))
    cm_csv.write("\n".join(csv))

## output labels information to label.json
with open("cm/label.json", "w") as label_file:
    json.dump(labels, label_file, indent=4)

## output index information to index.json
with open("cm/index.json", "w") as index_file:
    json.dump(index_output,index_file,indent=4)
