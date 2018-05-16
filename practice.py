def file_to_lower(infile, outfile):
    with open(infile) as f:
        lines = f.read().lower()
    with open(outfile, "w") as f:
        f.write(lines)
    
    
file_to_lower("data.txt", "practice.txt")
