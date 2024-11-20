from src.static.paths.PathCheck import PathCheck


"""
All default paths are provided here
"""
static_paths = {    
    "output_dir": PathCheck("out", is_dir= True).GetPath()
}