import csv
import math
import matplotlib.pyplot as plt
import numpy as np
with open("energy_data.csv" , "r") as file:
    reader = csv.reader(file)
    next(reader)
    totalSaved = 0
    totalBefore = 0
    totalAfter = 0
    count = 0
    maxBefore = 0
    maxApplianceBefore = ""
    maxApplianceAfter = ""
    maxAfter = 0
    maxSaved = 0
    maxApplianceSaved = ""
    beforeValues = []
    afterValues = []
    savedValues = []
    applianceNames = []
    for row in reader:
       count += 1
       before = int(row[1])
       after = int(row[2])
       saved = before - after
       totalBefore += before
       totalAfter += after
       totalSaved += saved
       percentageSaved = (saved / before) * 100
       if maxBefore < before:
           maxBefore = before
           maxApplianceBefore = row[0]
       if maxAfter < after:
            maxAfter = after
            maxApplianceAfter = row[0]
       if maxSaved < saved:
            maxSaved = saved
            maxApplianceSaved = row[0]

       if percentageSaved >= 30:
            recommendation = "Excellent Optimization"
            suggestion = "Keep the current optimization settings."

       elif percentageSaved >= 15:
            recommendation = "Good Optimization"
            suggestion = "Small improvements can further reduce consumption."

       elif percentageSaved >= 5:
            recommendation = "Average Optimization"
            suggestion = "Consider using the appliance more efficiently."

       else:
            recommendation = "Needs Improvement"
            suggestion = "Inspect the appliance or reduce unnecessary usage."
       beforeValues.append(before)
       afterValues.append(after)
       savedValues.append(saved)
       applianceNames.append(row[0])
       print("Appliance:" , row[0])
       print("Before: ",before)
       print("After: ",after)
       print("Saved:",saved)
       print(f"Percentage Saved: {round(percentageSaved, 2)}%")
       print("Recommendation:", recommendation)
       print("Suggestion:", suggestion)
    print("\n==========================")
    print("  ENERGY ANALYSIS REPORT")
    print("==========================\n")
    print("Total Before:",totalBefore)
    print("Total After:",totalAfter)
    averageBefore = totalBefore / count
    averageAfter = totalAfter / count
    print("Average Before:",round(averageBefore, 2))
    print("Average After:", round(averageAfter , 2))
    print("Total Energy Saved:",totalSaved)
    print(f"Highest Comsuption Before: {maxApplianceBefore} ({maxBefore} units)")
    print(f"Highest Consuption After: {maxApplianceAfter} ({maxAfter} units)")
    print(f"Highest Saving Appliance: {maxApplianceSaved} ({maxSaved} units)")
    print(beforeValues)
    print(afterValues)
    print(savedValues)
    print(applianceNames)
    
    sumSquareDiff = 0
    for value in beforeValues:
        difference = value - averageBefore
        squaredDiff = difference ** 2
        sumSquareDiff += squaredDiff
        
    variance = sumSquareDiff / count
    standardDeviation = math.sqrt(variance)
    print("Variance:", variance)
    print("Standard Deviation:", standardDeviation)
    
    cleanApplianceNames =[]
    cleanBeforeValues = []
    cleanAfterValues = []
    cleanSavedValues = []
    for i  in range(len(beforeValues)):
        distance = abs(beforeValues[i] - averageBefore)
        if distance > 2 * standardDeviation:
            print("Outlier Found:", applianceNames[i])
        else:
            cleanApplianceNames.append(applianceNames[i])
            cleanBeforeValues.append(beforeValues[i])
            cleanAfterValues.append(afterValues[i])
            cleanSavedValues.append(savedValues[i])
            
    print("\nClean Data")
    print(cleanApplianceNames)
    print(cleanBeforeValues)
    print(cleanAfterValues)
    print(cleanSavedValues)   
    
with open("cleaned_energy_data.csv","w",newline="")as file:
    writer = csv.writer(file)
    writer.writerow(["Appliance","Before","After","Saved"])
    for i in range(len(cleanApplianceNames)):
        writer.writerow([
            cleanApplianceNames[i],
            cleanBeforeValues[i],
            cleanAfterValues[i],
            cleanSavedValues[i]
        ])
plt.figure(figsize=(10,5))
x= np.arange(len(cleanApplianceNames))
width = 0.35

plt.bar(x- width/2,cleanBeforeValues , width , label ="Before")
plt.bar(x + width/2 , cleanAfterValues, width, label = "After")
plt.xlabel("Appliances")
plt.ylabel("Energy Consuption")
plt.title("Energy Consuption Before vs After Optimization")

plt.legend()
plt.xticks(x,cleanApplianceNames, rotation = 45)

plt.show()

plt.figure(figsize=(10,5))
plt.bar(cleanApplianceNames,cleanSavedValues)

plt.xlabel("Appliances")
plt.ylabel("Energy Saved (Units)")
plt.title("Energy Saved by Each Appliance")
plt.xticks(rotation=45)

plt.show()