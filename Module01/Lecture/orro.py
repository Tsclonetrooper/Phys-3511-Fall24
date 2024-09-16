list = [1,3,5,4,6,9,8]
number = 0

for item in list:
    if item < number:
        number = item

print(number)


fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.16,0.45,0.4,0.4])
axes1.plot(x,y)
axes2.plot(y,x)
axes1.set_title('Large Plot')
axes2.set_title('Small Plot');
#stop print out after plot with ;