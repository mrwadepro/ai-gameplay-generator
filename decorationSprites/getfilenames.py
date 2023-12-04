import os
f = open("filenames.txt", "w")
f.write("\n".join(item for item in os.listdir("images/All")))
f.close()