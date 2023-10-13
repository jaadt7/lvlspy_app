import lvlspy.spcoll as lc
new_coll = lc.SpColl()
new_coll.update_from_xml('nuc_data_test.xml')

kr85 = new_coll.get()['kr85']

levels = kr85.get_levels()
l_rm = levels[191]
upper_conn = kr85.get_upper_linked_levels(levels[191])
lower_conn = kr85.get_lower_linked_levels(levels[191])

for l in upper_conn:
    t = kr85.get_level_to_level_transition(l,l_rm)
    if t is None:
        continue
    else:
        kr85.remove_transition(t)

for l in lower_conn:
    t = kr85.get_level_to_level_transition(l_rm,l)
    if t is None: 
        continue
    else:
        kr85.remove_transition(t)

kr85.remove_level(l_rm)

rm = kr85.compute_rate_matrix(1e+9)
print(rm)
levels = kr85.get_levels()
print(len(levels))

t =kr85.get_transitions()
print(len(t))

