#!/usr/bin/env python3

import os,sys
import json
import pandas as pd

def concatenate_csvs(csvs,subjects,sessions,tags,datatype_tags):
    
    data = pd.DataFrame()

    for i in range(len(csvs)):
        # load data
        tmp = pd.read_csv(csvs[i])

        # add subject and session ids if not there
        if 'subjectID' not in tmp.keys().tolist():
            tmp['subjectID'] = [ subjects[i] for f in range(len(tmp)) ]
        if 'sessionID' not in tmp.keys().tolist():
            tmp['sessionID'] = [ sessions[i] for f in range(len(tmp)) ]

        # add tags and datatype tags
        tmp['tags'] = [ tags for f in range(len(tmp)) ]
        tmp['datatype_tags'] = [ datatype_tags for f in range(len(tmp)) ]

        # concatenate dataframes
        data = pd.concat([data,tmp])
    
    # reset index
    data = data.reset_index(drop=True)

    return data

def main():
    
    # load config
    with open('config.json','r') as config_f:
        config = json.load(config_f)

    # make output directories
    if not os.path.exists('./tractmeasures'):
        os.mkdir('./tractmeasures')

    # set input values
    csvs = config['csv']
    subjects = [ f['meta']['subject'] for f in config['_inputs'] ]
    sessions = [ f['meta']['session'] for f in config['_inputs'] ]
    tags = config['tags']
    datatype_tags = config['datatype_tags']
    outPath = './tractmeasures/tractmeasures.csv'

    # concatenate data
    data = concatenate_csvs(csvs,subjects,sessions,tags,datatype_tags)

    # output csv
    data.to_csv(outPath,index=False)

if __name__ == '__main__':
    main()