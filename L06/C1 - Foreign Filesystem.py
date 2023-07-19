#
# Find the file in the alien directories in /tmp/aliendir to get the flag
#

import os

# its so long lol
[[print(file) for file in files] for root, dirs, files in os.walk("/tmp/aliendir")]
