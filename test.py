import main
import read_data
small=read_data.data_reading(str(input("Insert the name of the csv file you want to analyze.")))
main.display_results(small)
