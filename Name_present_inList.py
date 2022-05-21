from tokenize import Name


Names = ["Ahmad", "ALi", "Aslam", "Shayan", "Faisal"," Tayyab", "Tom", "Bill"]
Name = input("Enter the Name to Search or Check: ")
if Name in Names:
    print("Name is Present: ")
else:
    print("Name is not Present: ")