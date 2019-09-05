import cv2

from regulargrid.RegularGrid import RegularGrid

# Parameters
input_image_name = "in/office-map-12-18.png"
output_image_name = "out/regular-grid.png"
th_val = 200
num_squares = 20
show_marked = False

# Read image from file and show.
img = cv2.imread(input_image_name, cv2.IMREAD_GRAYSCALE)

# Threshold image and show.
ret, threshold = cv2.threshold(img, th_val, 255, cv2.THRESH_BINARY)

# Generate regulargrid
regulargrid = RegularGrid()
regulargrid.create_regular_grid(threshold, num_squares, show_marked)

# Draw squares
img_res_regulargrid = cv2.imread(input_image_name, cv2.IMREAD_GRAYSCALE)
for i in range(0, len(regulargrid.nodes)):
    regulargrid.nodes[i].square.draw_square(img_res_regulargrid, (0, 255, 0), 1)

# Generate adjacency graph
regulargrid.calculate_adjacency()
for i in regulargrid.adjacency:
    for j in i:
        print(str(j) + " ", end="")
    print("")

# Print adjacents and nodes
regulargrid.print_adjacents()
regulargrid.print_nodes()

# Mostar imágenes y guardar
cv2.imshow('RegularGrid', img_res_regulargrid)
cv2.imwrite(output_image_name, img_res_regulargrid)
cv2.waitKey(0)

cv2.destroyAllWindows()
