import matplotlib.pyplot as plt

x = [0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.47, 0.48, 0.49, 0.5, 0.52, 0.53, 0.54, 0.55, 0.56, 0.59, 0.6, 0.61, 0.62, 0.63, 0.67, 0.68, 0.69, 0.7, 0.71, 0.72, 0.78, 0.79, 0.8, 0.81, 0.82, 0.83, 0.84, 0.85, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1.0, 1.01, 1.02, 1.17, 1.18, 1.19, 1.2, 1.21, 1.22, 1.23, 1.24, 1.25, 1.26, 1.27, 1.28, 1.56, 1.57, 1.58, 1.59, 1.6, 1.61, 1.62, 1.63, 1.64, 1.65, 1.66, 1.67, 1.68, 1.69, 1.7, 1.71]
y = [500.0, 463.6684, 500.0211, 457.2288, 490.4712, 442.17, 393.6256, 419.4304, 446.0544, 390.15, 413.4375, 355.6224, 375.6536, 396.2336, 334.1637, 351.52, 369.3157, 387.5508, 319.5072, 334.5408, 349.92, 294.0179, 306.6624, 319.5731, 332.75, 270.4, 280.9, 291.6, 302.5, 313.6, 253.7649, 262.44, 271.2609, 280.2276, 289.3401, 229.8368, 236.7488, 243.7632, 250.88, 258.0992, 265.4208, 208.6812, 214.0663, 219.52, 225.0423, 230.6332, 236.2927, 242.0208, 247.8175, 190.8576, 194.94, 199.0656, 203.2344, 207.4464, 211.7016, 216.0, 220.3416, 224.7264, 171.1125, 174.05, 177.0125, 180.0, 183.0125, 186.05, 189.1125, 192.2, 195.3125, 198.45, 201.6125, 204.8, 155.7504, 157.7536, 159.7696, 161.7984, 163.84, 165.8944, 167.9616, 170.0416, 172.1344, 174.24, 176.3584, 178.4896, 180.6336, 182.7904, 184.96, 187.1424]

print len(x), len(y)

plt.plot(x, y, 'r--')
plt.axis([0, 2.1, 100, 500])
plt.xlabel('k')
plt.ylabel('(l^3)(k^2)')
plt.show()