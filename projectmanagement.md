# Raytracer from Scratch – Full Development Checklist

## 1. Concept and Planning
- [x] Define your goal: real-time or offline rendering? Simple or physically accurate?
- [x] Decide which features you want (e.g. shadows, reflections, refractions)
- [x] Will it render to an image file or display in a window?

## 2. Project Setup
- [x] Choose your programming language (e.g. Python)
- [x] Decide on your folder and file structure
- [x] List any dependencies (e.g. Pillow for image output, NumPy for math)
- [x] Plan a simple test scene (like one sphere and one light)

## 3. Math Foundations
- [x] Implement 3D vector operations (add, subtract, scalar multiply, normalize)
- [x] Understand points, direction vectors, and unit vectors
- [x] Define a ray (origin point + direction vector)
- [x] Write intersection math (e.g. ray-sphere intersection)

## 4. Core Ray Tracing Logic
- [x] Define a camera (position, look direction, field of view, resolution)
- [x] Generate primary rays for each pixel (raycasting)
- [x] Support at least one object type, like a sphere
- [ ] Implement ray-object intersection detection
- [ ] Return a basic color when a ray hits an object

## 5. Lighting
- [ ] Add simple Lambertian diffuse lighting
- [ ] Support light sources (position, intensity, color)
- [ ] Cast shadow rays to check if surfaces are in shadow
- [ ] Add ambient lighting for base brightness

## 6. Reflections
- [ ] Calculate reflected rays (mirror angle from surface normal)
- [ ] Define reflection depth (how many times a ray can bounce)
- [ ] Blend direct light with reflected light contributions

## 7. Refractions
- [ ] Implement Snell’s Law for transparent materials
- [ ] Handle total internal reflection cases
- [ ] Add material properties like refractive index and transparency

## 8. Materials and Textures
- [ ] Define materials (color, reflectivity, transparency, shininess)
- [ ] Support basic texture mapping (e.g. checkerboard pattern)
- [ ] Modify surface normals for bump mapping effects

## 9. More Geometry and Scene Structure
- [ ] Add support for planes, triangles, boxes, and meshes
- [ ] Implement bounding volumes (Bounding Spheres or Axis-Aligned Bounding Boxes)
- [ ] Prepare for acceleration structures like BVH or KD-Trees

## 10. Image Output
- [ ] Collect pixel colors (RGB)
- [ ] Output image as PNG or BMP
- [ ] Add anti-aliasing (e.g. via supersampling)

## 11. Performance and Optimization
- [ ] Reduce redundant calculations (ray reuse, memoization)
- [ ] Use multithreading or parallel processing if possible
- [ ] Implement ray batching (process rays in groups)

## 12. Advanced Features (Optional)
- [ ] Depth of field (simulate camera focus blur)
- [ ] Motion blur (simulate moving objects/camera)
- [ ] Soft shadows (area light sources)
- [ ] Global Illumination (e.g. via path tracing)
- [ ] Photon Mapping or Radiosity
- [ ] Tone Mapping and HDR support
- [ ] Real-time rendering with GPU (e.g. OpenGL or Vulkan)

## 13. Tools & Debugging
- [ ] Visualize rays and intersections for debugging
- [ ] Output normal maps or depth maps to aid development
- [ ] Log ray bounces, intersections, and performance stats
