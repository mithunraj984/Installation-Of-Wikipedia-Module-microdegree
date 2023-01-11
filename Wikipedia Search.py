# Importing Wikipedia module
# To install pip install wikipedia
import wikipedia  as wiki

# Setting language here hindi is set
wiki.set_lang("hi")

# Printing the summary from wikipedia
print(wiki.summary("Python"))