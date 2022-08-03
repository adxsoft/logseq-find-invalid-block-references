# logseq-find-invalid-block-references

A Python 3 script I developed for myself to find invalid block references in a logseq graph

This script scans all markdown files in the pages and journals folders of a logseq graph.

Each block reference is checked to confirm it actually exists in any of the pages in the pages or journals folder.

If an invalid block reference is discovered it is reported together with the markdown file it exists in.

There is no attempt to check within the internal logseq database. Once you have fixed any invalid bock references then a logseq graph re-index will ensure logseq's internal databases are update

