import cv2

from regularnet.RegularNet import RegularNet

# Parameters
input_image_name = "in/office-map-12-18.png"
output_image_name = "out/regular-net.png"
th_val = 200
num_squares = 20
show_marked = False

# Read image from file and show.
img = cv2.imread(input_image_name, cv2.IMREAD_GRAYSCALE)

# Threshold image and show.
ret, threshold = cv2.threshold(img, th_val, 255, cv2.THRESH_BINARY)

# Generate regularnet
regularnet = RegularNet()
regularnet.create_regular_net(threshold, num_squares, show_marked)

# Draw squares
img_res_regularnet = cv2.imread(input_image_name, cv2.IMREAD_GRAYSCALE)
for i in range(0, len(regularnet.nodes)):
    regularnet.nodes[i].square.draw_square(img_res_regularnet, (0, 255, 0), 1)

# Generate adjacency graph
regularnet.calculate_adjacency()
for i in regularnet.adjacency:
    for j in i:
        print(str(j) + " ", end="")
    print("")

# Print adjacents and nodes
regularnet.print_adjacents()
regularnet.print_nodes()

# Mostar imágenes y guardar
cv2.imshow('RegularNet', img_res_regularnet)
cv2.imwrite(output_image_name, img_res_regularnet)
cv2.waitKey(0)

cv2.destroyAllWindows()
