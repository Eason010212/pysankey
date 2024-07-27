import sankeyStream as sks

sankey = sks.Sankey()
sankey.add_node('A', label='Node A', color='blue', weight=1, depth=0)
sankey.add_node('B', label='Node B', color='red', weight=1, depth=1)
sankey.add_link('A', 'B', value=1)

sankey.draw().display()