import matplotlib.pyplot as plt

vals = [24, 17, 53, 21, 35]
labels = ["Ford", "Toyota", "BMW", "Audi", "Jaguar"]
plt.pie(vals, labels=labels)
plt.title("Распределение марок автомобилей на дороге")
plt.savefig("krug.png")