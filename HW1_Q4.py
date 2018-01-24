yours = ['Yale', 'MIT', 'Berkeley']
mine = ['Union', 'Yale', 'Cornell']

ours1 = mine + yours

ours2 = []
ours2.append(mine)
ours2.append(yours)

print(ours1)
print(ours2)

# ours1 is a single list of every school contained within yours and mine, while
# ours2 is a combination of the two lists, as two separate groups. This is due to
# the append command, which adds a single element to the end of the list, rather than
# combining the two.

yours[1] = 'Harvard'

print(ours1)
print(ours2)

# Changing the second element of yours changes ours2 but not ours1 because of the way
# in which we coded for the change in yours. If we instead redefined yours as
# ['Yale', 'Harvard', 'Berkeley'], then ours1 would be changed.
