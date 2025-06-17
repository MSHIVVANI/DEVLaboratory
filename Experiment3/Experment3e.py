# Example 1: Single plot with customized spines
import matplotlib.pyplot as plt

a = [1, 2, 3, 4, 5]
b = [0, 0.6, 0.2, 15, 10, 8, 16, 21]
c = [4, 2, 6, 8, 3, 20, 13, 15]

plt.plot(a)
plt.plot(b, "or")
plt.plot(list(range(0, 22, 3)))
plt.plot(c, label='4th Rep')

plt.xlabel('Day->')
plt.ylabel('Temp->')

# Customize plot spines and ticks
ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_bounds(3, 40)
plt.xticks(list(range(3, 10)))
plt.yticks(list(range(3, 20, 3)))

plt.show()

# Example 2: Subplot grid (2x2)
import matplotlib.pyplot as plt

a = [1, 2, 3, 4, 5]
b = [0, 0.6, 0.2, 15, 10, 8, 16, 21]
c = [4, 2, 6, 8, 3, 20, 13, 15]

# Create figure and subplots
fig = plt.figure(figsize=(10, 10))
sub1 = plt.subplot(2, 2, 1)
sub2 = plt.subplot(2, 2, 2)
sub3 = plt.subplot(2, 2, 3)
sub4 = plt.subplot(2, 2, 4)

# First subplot
sub1.plot(a, 'sb')
sub1.set_xticks(list(range(0, 10, 1)))
sub1.set_title('1st Rep')

# Second subplot
sub2.plot(b, 'or')
sub2.set_xticks(list(range(0, 10, 2)))
sub2.set_title('2nd Rep')

# Third subplot
sub3.plot(list(range(0, 22, 3)), 'vg')
sub3.set_xticks(list(range(0, 10, 1)))
sub3.set_title('3rd Rep')

# Fourth subplot
sub4.plot(c, 'Dm')
sub4.set_yticks(list(range(0, 24, 2)))
sub4.set_title('4th Rep')

plt.show()