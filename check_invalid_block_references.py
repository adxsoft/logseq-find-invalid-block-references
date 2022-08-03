import re
import os

# Check Logseq journals and pages folders for any blocks that are referred to
# with (()) references eg ((e5f6ca4a-e894-474c-8643-1d561b637c22))
# that DO NOT EXIST ie. there is no markdown page with a
# correspondingblock id tag eg id:: 621728dd-7e3a-40c7-99e3-1b5db7a80280

# To run this script
# - you need python3 installed
# - change 'logseqpath' to the FULL path to your graph
# - change 'operatingsystem' to WINDOWS or MAC or LINUX (mobile not supported)

# =================================================
# CHANGE THESE VARIABLES BEFOER RUNNING THE SCRIPT
# =================================================

# The full path to your logseq graph for example /Users/adxsoft/mylogseqgraph/
logseqpath = "FULLPATHTOYOURLOGSEQGRAPH"
logseqpath = "/Users/allandavies/Dropbox/Apps/ADLiveCode/ADPKM/Logseq/Golf"

# the operating system of your desktop WINDOWS, MAC or LINUX
opsys = "MAC"

# =================================================


# Script starts here

logseqgraphname = logseqpath.split("/")[-1]
if opsys == "MAC" or opsys == "LINUX":
    separator = "/"
else:
    separator = "\\"  # Windows file separator


def get_graph_filenames(graphname):
    filenames = []
    filenames += get_list_of_filenames(logseqpath+separator+"pages")
    filenames += get_list_of_filenames(logseqpath+separator+"journals")
    return filenames

# get list of markdown files in the logseq graph


def get_list_of_filenames(PATH):
    fullfilenames = []
    list_of_files = os.listdir(PATH)
    for file in list_of_files:
        if len(file) < 1:
            continue
        if not file.endswith('.md'):
            continue
        fullfilenames.append(PATH+separator+file)
    return fullfilenames


def get_lines_in_file(filename):
    lines = []
    if len(filename) < 1:
        return
    if not filename.endswith('.md'):
        return
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    return lines


def get_all_blockids_in_file(filename):
    blockids = []
    for line in get_lines_in_file(filename):
        line = line.strip()  # remove /n
        # Ignore if no block ids in the line
        if line.find("id:: ") > -1:
            line = line[line.find("id:: "):]
            blockid = line[5:].strip()
            blockids.append(blockid)
    return blockids


def get_all_blockrefs_in_file(filename):
    blockrefs = []
    for line in get_lines_in_file(filename):
        line = line[:-1]  # remove /n
        # Ignore if no block reference in the line
        uuid_extract_pattern = "\(\([0-9a-f]{8}-[0-9a-f]{4}-[0-5][0-9a-f]{3}-[089ab][0-9a-f]{3}-[0-9a-f]{12}\)\)"
        matches = re.findall(uuid_extract_pattern, line)
        if len(matches) > 0:
            for match in matches:
                blockrefs.append(match[2:-2]+"|"+filename)
    return blockrefs


def getfileinfo(path):
    fields = path.split(separator)
    gfp = fields[-3:]
    graphname = gfp[0]
    folder = gfp[1]
    filename = gfp[2]
    return graphname+separator+folder+separator+filename


def make_array_unique(array):
    uniquelist = []
    for item in array:
        if item not in uniquelist:
            uniquelist.append(item)
    return uniquelist


# scan for block ids
graphblockids = []
graphblockrefrecords = []
graphblockrefs = []
graphblockrefsdict = {}
filestocheck = get_graph_filenames(logseqgraphname)
for filename in filestocheck:
    graphblockids += get_all_blockids_in_file(filename)
    graphblockrefrecords += get_all_blockrefs_in_file(filename)
    for record in graphblockrefrecords:
        fields = record.split("|")
        blockid = fields[0]
        thefilename = fields[1]
        graphblockrefs += [blockid]
        graphblockrefsdict[blockid] = getfileinfo(thefilename)

graphblockids = make_array_unique(graphblockids)
graphblockrefs = make_array_unique(graphblockrefs)
graphblockids.sort()
graphblockrefs.sort()
print("\nLogseq Graph: "+logseqgraphname)

if graphblockids == graphblockrefs:
    print("  -  block references are ok")
else:
    msg = ""
    for ref in graphblockrefs:
        if not ref in graphblockids:
            msg += "    => "+ref+" \n       on page " + \
                graphblockrefsdict[ref]+"\n\n"
    if len(msg) > 0:
        print("\n  - ** invalid block references\n")
        print(msg)
