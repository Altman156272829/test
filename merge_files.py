import os
def merge_files(file1,file2,output_file):
    i=1
    with open(file1,"r") as File_1:
        first_file = File_1.read()
        sorted_first_file = first_file.split("\n")
    with open(file2,"r") as File_2:
        secend_file = File_2.read()
        sorted_second_file = secend_file.split("\n")
    if os.path.exists(output_file):
        with open(output_file,"a") as file:
            while i <= len(sorted_first_file) or i <= len(sorted_second_file):
                if i <= len(sorted_first_file):
                    file.write(sorted_first_file[i])
                if i <= len(sorted_second_file):
                    file.write(sorted_second_file[i])
                i +=1
    else:
        with open(output_file,"w") as file:
            while i <= len(sorted_first_file) or i <= len(sorted_second_file):
                if i <= len(sorted_first_file):
                    file.write(sorted_first_file[i])
                if i <= len(sorted_second_file):
                    file.write(sorted_second_file[i])
                i +=1
def main():
    file1 = input(" enter the location of the first file")
    file2 = input(" enter the location of the second file")
    output_file =input(" enter the location of united file (output file)")
    merge_files(file1,file2,output_file)
if __name__ == "main":
    main()    
    
    