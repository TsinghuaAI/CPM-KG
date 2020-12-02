from cpm_kg_reader import CPMKGReader
reader = CPMKGReader("/path/to/distmult_256")
print(reader.get_entity(0))
print(reader.get_relation(0))