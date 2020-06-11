from parser.sol_parser import SolParser
from pathlib import Path

if __name__ == '__main__':
	file_name = 'TZ.SOL'
	dir_path = Path("""/gpfs/data1/cmongp/ujjwal/tanzania/tanzania_soil/""")

	parse_obj = SolParser()
	parse_obj.load_data_src(dir_path,file_name)
	print(parse_obj.file_name)
	print(parse_obj.dir_path)
	parse_obj.generate_component()	
