#This is a program by Lynn Mutuku F16/..../2018

#DEFINITIONS OF TERMS RANDOM IN THE PROJECT
# Prompt the user for a number between 1 and 20, which is initialized as an integer
number = int(input("Enter a number between 1 and 20: "))

# Check the entered number using if and else statements and give out a random definition
if number == 1:
    print(" Slump measures the consistency of fresh concrete, indicating its workability and the ease with which it can be placed and compacted. A high slump indicates that the concrete is more workable, while a low slump indicates that the concrete is less workable.")
elif number == 2:
    print("Recycled concrete aggregates, RCAs are made up of crushed concrete debris. RCAs are aggregates created by processing materials previously used to make a product or for construction.")
elif number == 3:
    print("In the ancient times when red lime was used as a cementing component,sand, gravel and water were the main components in making concrete.")
elif number == 4:
    print("Naturally occurring concrete aggregates are those already existing while Recycled Concrete Aggregates are obtained from conrete which has been demolished.")
elif number == 5:
    print("In testing concrete to determine the concrete class, cubes measuring 150mm and cylinders 150mm in diameter and 300mm length are used as molds. ")
elif number == 6:
    print("The compaction factor is the ratio of weights of partially compacted to fully compacted concrete. This is an experiment done on fresh concrete to determine its workability.")
elif number == 7:
    print("Compressive strength is the capacity of a material or structure to withstand axially directed forces/ axial loading. The compressive strength is measured by destructive testing of cylindrical or cubical concrete specimens in a compression-testing machine")
elif number == 8:
    print("Concrete's tensile strength is its ability to resist cracking or breaking under tension. Due to its brittle nature, concrete is exceedingly weak in tension and needs to be reinforced with steel")
elif number == 9:
    print("Sieve analysis is a test performed on aggregates to determine their size, grade them and classify them as fine or as coarse aggregates")
elif number == 10:
    print("Density refers to the measure of mass per unit volume of a material. Density determinations are done on cubes at the 7-day and 28-day mark prior to testing for strength")
elif number == 11:
    print("With regards to coarse aggregates, the Aggregate Crushing Value test (ACV) provides a relative assessment of an aggregate's resistance to crushing under gradually applied compressive load.")
elif number == 12:
    print("Toughness refers to the ability of a material to withstand impact and it is determined by the Aggregate Impact Value test (AIV)")
elif number == 13:
    print("water/cement ratios is the ratios by mass of free-water to cement in the mix and these, as well as the free-water contents, are based on the aggregates being in a saturated surface-dry condition")
elif number == 14:
    print("Water Absorption of aggregates is the percentage of water absorbed by an air-dried aggregate when immersed in water at 27°C for a period of 24hours")
elif number == 15:
    print("Recycled aggregate calcination is necessary to dehydrate the cement paste, which reduces adhesion of the hardened mortar to the aggregate grains and finally makes it easier to remove it from the surface of the aggregate. It is done in an oven at 300 degrees.")
elif number == 16:
    print("Workability of concrete refers to the ease with which it can be poured during the construction process. It should be paid attention to")
elif number == 17:
    print("According to BS 410:1986, well and uniformly graded aggregates enhance concrete workability by minimizing voids in the mix as they are filled by smaller particles of the aggregates")
elif number == 18:
    print("Concrete is usually compacted using a vibrator to reduce voids which may be in it. In the lab, it is easier to use a table vibrator for the purpose of testing.")
elif number == 19:
    print("When carrying out tests on concrete, the engineer needs to do batching and mixing carefully by weight so as to get quality and accurate results from the samples")
elif number == 20:
    print("Have a lovely day ;-) haha ")
else:
    print("Invalid input. The number should be between 1 and 20.")


##########TEST LAB ANALYSIS###############
#########
#SIEVE ANALYSIS
#Initialize the variables as floats so that they can take decimals, otherwise known as floating points
total_Mass_Of_Aggregates_Retained = float(input("Enter the total mass of aggregates retained: "))
total_Mass_Of_Aggregates = float(input("Enter the total mass of aggregates: "))

#Return the mass of aggregates retained as a percentage of the total mass entred
mass_Of_Aggregate_Retained = float (total_Mass_Of_Aggregates_Retained/total_Mass_Of_Aggregates) * 100

########
#AGGREGATE CRUSHING VALUE TEST ACV
total_Mass_Of_Aggregates_Passing_2_36_sieve_size = float(input("Enter the total mass of aggregates passing 2.36 sieve size: "))
aggregate_Crushing_Value = float (total_Mass_Of_Aggregates_Passing_2_36_sieve_size/total_Mass_Of_Aggregates) * 100

# Format and print the ACV as a percentage
formatted_ACV = "{:.2f}%".format(aggregate_Crushing_Value)

########
#AGGREGATE IMPACT VALUE TEST AIV
total_Mass_Of_Aggregates_Passing_2_36_sieve_size = float(input("Enter the total mass of aggregates passing 2.36 sieve size: "))
aggregate_Impact_Value = float (total_Mass_Of_Aggregates_Passing_2_36_sieve_size/total_Mass_Of_Aggregates) * 100

# Format and print the ACV as a percentage
formatted_AIV = "{:.2f}%".format(aggregate_Impact_Value)

####is ACV and AIV the same thing?

#WATER ABSORPTION OD AGGREGATES AND SPECIFIC GRAVITY TEST
#WATER ABSORPTION
weight_Of_Surface_Dry_Aggregates = float (input("Enter the weight of Surface Dry Aggregates:"))
weight_Of_Oven_Dry_Aggregates = float (input("Enter the weight of Oven Dry Aggregates:"))
oven_Dried_Weight = float (input("Enter the oven_Dried_Weight:"))
submerged_Weight = float (input("Enter the submerged_Weight:"))


water_Absorption = float ((weight_Of_Surface_Dry_Aggregates - weight_Of_Oven_Dry_Aggregates)/weight_Of_Oven_Dry_Aggregates)

amount_Specific_Gravity = float (oven_Dried_Weight/(oven_Dried_Weight - submerged_Weight))

gross_Specific_Gravity = float (weight_Of_Surface_Dry_Aggregates/(weight_Of_Surface_Dry_Aggregates - submerged_Weight))

##############
#SAMPLES OF CONCRETE
#To achieve a class 25 concrete
#Volume of a cube
length = 150 #length of the m=cube mold in mm
cube_Volume = float ((length * length * length)/1000000000) #Calculate the volume and convert it to metres cubed

#Volume of a cylinder
r = 75 #the radius of a test cylinder mold
h = 300 #the height of a test cylinder mold

pi = 3.142 #Initialize the value of pi to be used
cylinder_Volume = float ((pi * r * r * h)/1000000000) #volume of a cylinder is pi * r^2 * h

#Total Batch Volume
volume = cube_Volume + cylinder_Volume

#Total Volume for a single Batch
#This will be 4 cubes and 2 cylinders
total_Volume_For_A_Single_Batch = float ((4 * cube_Volume) + (2 * cylinder_Volume))

#Wastage 
#Account for wastage of concrete by adding 20% more to the Total Volume for a single Batch
total_Volume_For_A_Single_Batch_Wastage = float (1.20 * total_Volume_For_A_Single_Batch)

#Mix ratio for a single batch
#Prompt the user to enter the densities of materials in consideration
cement_Density = float (input("Enter the density of cement in kg/m^3: "))
sand_Density = float (input("Enter the density of sand in kg/m^3: "))
coarse_Aggregate_Density = float (input("Enter the density of coarse_Aggregate in kg/m^3: "))

#Mass of the materials in a single batch of concrete
cement_Mass = float (cement_Density * total_Volume_For_A_Single_Batch_Wastage)
sand_Mass = float (sand_Density * total_Volume_For_A_Single_Batch_Wastage)
coarse_Aggregate_Mass = float (coarse_Aggregate_Density * total_Volume_For_A_Single_Batch_Wastage)

#Mix ratio for 11 cubes and 8 cylinders
#CEMENT : SAND : COARSE AGGREGATES

#OUTPUTS OF THE ANALYSIS
#concatenation in python requires you to pass floats as strings, that is why the values are wrapped str(float)
print ("The aggregate crushing value in percentage is" + formatted_ACV)
print ("The aggregate impact value in percentage is " + formatted_AIV)
print ("The Water absorption of samples is:" + str(water_Absorption))
print ("The amount specific gravity of samples is:" + str(amount_Specific_Gravity))
print ("The gross specific gravity of samples is:" + str(gross_Specific_Gravity))
print ("The volume of a single cube is:" + str(cube_Volume))
print ("The volume of a single cylinder is:" + str(cylinder_Volume))
print ("The volume sum of a single cube and cylinder is:" + str(volume))
print ("The volume for a single batch is:" + str(total_Volume_For_A_Single_Batch))
print ("The volume for a single batch considering 20% wastage is:" + str(total_Volume_For_A_Single_Batch_Wastage))
print ("The mass in kg of cement is:" + str(cement_Mass))
print ("The mass in kg of sand is:" + str(sand_Mass))
print ("The mass in kg of coarse aggregates is:" + str(coarse_Aggregate_Mass))
print ("Success!! Concrete of class 25 is achieved.")