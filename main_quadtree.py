import cv2

from quadtree.QuadTree import QuadTree

# Parameters
input_image_name = "in/office-map-12-18.png"
output_image_name = "out/quadtree.png"
th_val = 200
depth = 7
show_marked = False

# Read image from file and show.
img = cv2.imread(input_image_name, cv2.IMREAD_GRAYSCALE)

# Threshold image and show.
ret, threshold = cv2.threshold(img, th_val, 255, cv2.THRESH_BINARY)

# Generate quadtree
quadtree = QuadTree()
quadtree.create_quad_tree(threshold, depth, show_marked)

# Dibujar sobre el mapa los cuadrados y los centros.
img_res_quadtree = cv2.imread(input_image_name, cv2.IMREAD_GRAYSCALE)
for i in range(0, len(quadtree.nodes)):
    quadtree.nodes[i].square.draw_square(img_res_quadtree, (0, 255, 0), 1)

# Mostar imágenes y guardar
cv2.imshow('QuadTree', img_res_quadtree)
cv2.imwrite(output_image_name, img_res_quadtree)
cv2.waitKey(0)

cv2.destroyAllWindows()
