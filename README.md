## Investigating Hotfixes in reposotories of different topics.

**RawBoaData** folder contains raw output from boa files (which are very hard to manipulate due to unpleasant data structures)

**ProcessedData** folder contains processed statistics of hotfixes identified, bump commits and hotfixes per bump commits ration. 
Produced by applying parseFiles.py script:

> python parseFiles.py RawBoaData/HotFixes/{source_filepath} ProcessedData/{output_filepath}


