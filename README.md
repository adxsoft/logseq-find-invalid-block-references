# logseq-find-invalid-block-references

A Python 3 script I developed for myself to find invalid block references in a logseq graph

This script scans all markdown files in the pages and journals folders of a logseq graph.

Each block reference is checked to confirm it actually exists in any of the pages in the pages or journals folder.

If an invalid block reference is discovered it is reported together with the markdown file it exists in.

There is no attempt to check within the internal logseq database. Once you have fixed any invalid bock references then a logseq graph re-index will ensure logseq's internal databases are update

# To run this script
 - you need python3 installed
 - Click the green Code button and choose Download Zip
 - unzip the downloaded file```
 - in a text editor change the script 'check_invalid_block_references.py' as follows
   - change 'logseqpath' to the FULL path to your graph
   - change 'operatingsystem' to WINDOWS or MAC or LINUX (mobile not supported)
   - save the script
 - open a terminal and type
   - python3 check_invalid_block_references.py
 # Sample output
 ```
 Logseq Graph: Golf

  - ** invalid block references

    => 623accb6-d0f3-4d83-934b-5b58b50eb516 
       on page Golf/pages/Methods%2FJack Kuykendall.md

    => 627a1398-7451-45ed-ba21-83245aa9dd50 
       on page Golf/journals/2022_05_04.md
```


