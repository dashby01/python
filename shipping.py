weight = 60

#Ground Shipping

if weight < 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3 + 20
elif weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20

print("Ground Shipping $", cost_ground)

#Ground Shipping Premium

cost_ground_premium = 125.00

print("Ground Shipping Premium $", cost_ground_premium)

#Drone Shipping

if weight < 2:
  cost_drone = weight * 1.5 + 20
elif weight <= 6:
  cost_drone = weight * 3 + 20
elif weight <= 10:
  cost_drone = weight * 4 + 20
else:
  cost_drone = weight * 4.75 + 20

print("Drone Shipping $", cost_drone)
