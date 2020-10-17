[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-brainlife.app.335-blue.svg)](https://doi.org/10.25663/brainlife.app.335)

# Convert network neuro matrix to conmat 

This app will converts a network matrix of a measure of interest (i.e. density, count) found in the raw:networkmatrices datatype output of Network Neuro app and a parcellation used to generate the matrix to a conmat datatype. This is a temporary app until the Network Neuro app outputs a conmat datatype. This conmat datatype is main datatype for a majority of the network processing apps currently on the website. May be deprecated in the future. 

### Authors 

- Brad Caron (bacaron@iu.edu) 

### Contributors 

- Soichi Hayashi (hayashis@iu.edu) 

### Funding 

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)

### Citations 

Please cite the following articles when publishing papers that used data, code or other resources created by the brainlife.io community. 

 

## Running the App 

### On Brainlife.io 

You can submit this App online at [https://doi.org/10.25663/brainlife.app.335](https://doi.org/10.25663/brainlife.app.335) via the 'Execute' tab. 

### Running Locally (on your machine) 

1. git clone this repo 

2. Inside the cloned directory, create `config.json` with something like the following content with paths to your input files. 

```json 
{
   "raw":    "testdata/raw/",
   "parc":    "testdata/parc/parc.nii.gz",
   "key":    "testdata/parc/key.txt",
   "label":    "testdata/parc/label.json"
} 
``` 

### Sample Datasets 

You can download sample datasets from Brainlife using [Brainlife CLI](https://github.com/brain-life/cli). 

```
npm install -g brainlife 
bl login 
mkdir input 
bl dataset download 
``` 

3. Launch the App by executing 'main' 

```bash 
./main 
``` 

## Output 

The main output of this App is a conmat datatype, including a index.json, label.json, and a directory titled 'csv' containing the network data. 

#### Product.json 

The secondary output of this app is `product.json`. This file allows web interfaces, DB and API calls on the results of the processing. 

### Dependencies 

This App requires the following libraries when run locally. 

- Python3: https://www.python.org/download/releases/3.0/
- matplotlib: https://matplotlib.org/users/installing.html
- shutil: https://pypi.org/project/pytest-shutil/
- json: https://pypi.org/project/jsonlib-python3/
