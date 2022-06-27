def print_models (unprinted_design, completed_design):
    while unprinted_design:
        current_design = unprinted_design.pop()
        completed_design.append(current_design)
        #print(current_design)
