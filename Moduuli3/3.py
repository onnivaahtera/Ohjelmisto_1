gender = input("Sukupuoli: ")
hemoglobin = int(input("Hemoglobiiniarvo: "))

if gender == "mies" and hemoglobin < 134 or gender == "nainen" and hemoglobin < 117:
  print("Hemoglobiiniarvo on alhainen.")
elif gender == "mies" and hemoglobin > 134 or gender == "nainen" and hemoglobin > 117:
  print("Hemoglobiiniarvo on korkea.")
else:
  print("Hemoglobiiniarvo on normaali.")
