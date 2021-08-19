Description
-----------

This tool is designed to visualize plant organization based on data from
Prairie Moon Nursery (PMN).

For each plant, PMN lists other plants that will pair well with it under
the category "Pair with..." at the bottom of the product listing.
For each plant specified, a node (circle) is created. If a plant is 
considered a good pairing according to PMN, an edge (line) is drawn between
the nodes for each plant.

Use
---

Current operation requires a CSV file (can be created in Excel or Google Sheets),
that contains the pairing information.

To run:

> plot_network.py plant-pairing-data.csv