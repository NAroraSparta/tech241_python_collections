# Your Hero Story!
#
# This is all about dictionaries. Note the method I didn’t show in class was .items(). it returns the key values pairs in the dictionary back as a list of tuples. Try it out!
#
# Summary
# Your going to write a story, cut it into section, store the section in a python dictionary!
#
# Tasks
#
# define a dictionary
#
# add your content as values for keys
#
# follow the instruction in the pseudo code below:
#
# **Dictionary basics :D
# **
# 1 - Define a dictionary call story1, it should have the following keys:
# #"start", "middle" and "end"
story_1 = {
    "start": "Long time ago, there lived a girl who loved to read, dream, paint and cook. Her passion was guessing what others had in their minds.",
    "middle": "One day, while trying to guess what her mum was thinking, she started hearing for some calls for help from a woman. She ran outside but didn't see anyone. "
              "She then started talking to that woman in her mind. She asked the woman for directions to her location. "
              "It wasn't long before she got to the woman. The woman had hurt herself by falling into an empty but concealed well. "
              "With her help,the woman was taken out of the well and given medical care. This made her wonder how could she hear someone she had never met. It started occuring every day and she was able to help anyone in need.",
    "end": "In the years that followed, people started calling her for help and she never let anyone down ever!"
}
# 2 - Print the entire dictionary
print(story_1)

# 3 - Print the type of your dictionary
print(type(story_1))

# 4 - Print only the keys
print(story_1.keys())

# 5 - Print only the values
print(story_1.values())

# 6 - Print the individual values using the keys (individually, lots of print commands)
print(story_1["start"])
print(story_1["middle"])
print(story_1["end"])

# 7 - Now let's add a new key:value pair.
story_1["hero"]= "Intuitive Aurora"