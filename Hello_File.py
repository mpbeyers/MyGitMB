My new file!
for i in 'hello':
print ('hello')
#This is an alteration to the earlier file
np.random.seed(42)
x = np.random.randn(100)

bins = np.linspace(-5, 5, 20)
counts = np.zeros_like(bins)

i = np.searchsorted(bins, x)

np.add.at(counts, i, 1)

#plot results
plt.plot(bins, counts, linestyle='steps');
