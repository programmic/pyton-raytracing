from viewer import ImageViewer
import numpy as np
import time
from vec3 import Vec3
from sphere import Sphere
from camera import Camera
import pygame
from material import Material
from PIL import Image, ImageDraw, ImageFont

def clamp(val, minv, maxv):
    return max(minv, min(val, maxv))

if __name__ == '__main__':
    # --- Set your render and output resolution here ---
    render_width, render_height = 640, 360      # Raytracer resolution (fast)
    output_width, output_height = 1280, 720     # Display resolution (upscaled)

    viewer = ImageViewer(width=output_width, height=output_height)
    viewer.start()
    print("Viewer started. Window should be black.")

    aspect = render_width / render_height

    # Camera setup
    camera = Camera(
        resolution=(render_width, render_height),
        pos=Vec3(0, 0, -3),
        rot=Vec3(0, 0, 0),
        fov=60.0
    )

    # Scene: multiple spheres
    spheres = [
        Sphere(Vec3(0, 0, 2), 0.5,          Material((255,   0,   0), 0.5)),
        Sphere(Vec3(-1, 0.5, 3), 0.5,       Material((  0, 255,   0), 0.5)),
        Sphere(Vec3(1, -0.5, 4), 0.5,       Material((  0,   0, 255), 0.5)),
        Sphere(Vec3(0.5, 1, 3.5), 0.4,      Material((255, 255,   0), 0.5)),
        Sphere(Vec3(-1.2, -0.8, 2.8), 0.3,  Material((255,   0, 255), 0.5)),
    ]

    # --- Interactive loop with WASD and mouse ---
    pygame.init()
    clock = pygame.time.Clock()

    move_speed = 0.75
    mouse_sens = 0.2
    running = True

    bounces = 15

    print("Use WASD to move, mouse to look. ESC to quit.")

    # FPS counter setup
    frame_count = 0
    fps = 0.0
    last_fps_time = time.time()
    font = pygame.font.SysFont("consolas", 24)

    while running and viewer._running:
        frame_start = time.time()
        dt = clock.tick(60) / 1000.0
        pygame.event.pump()  # Only needed for input

        # Handle events
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                print("\033[22mClosing window...\033[0;0m")
                running = False

        # Mouse look
        mx, my = pygame.mouse.get_rel()
        camera.rot.y += mx * mouse_sens
        camera.rot.x -= my * mouse_sens
        camera.rot.x = clamp(camera.rot.x, -89, 89)  # Prevent flipping

        # Calculate forward and right vectors for movement
        yaw_rad = np.deg2rad(camera.rot.y)
        forward = Vec3(np.sin(yaw_rad), 0, np.cos(yaw_rad)).normalize()
        right = Vec3(np.cos(yaw_rad), 0, -np.sin(yaw_rad)).normalize()

        # WASD movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            camera.pos += forward * move_speed
        if keys[pygame.K_s]:
            camera.pos -= forward * move_speed
        if keys[pygame.K_a]:
            camera.pos -= right * move_speed
        if keys[pygame.K_d]:
            camera.pos += right * move_speed
        if keys[pygame.K_SPACE]:
            camera.pos.y += move_speed
        if keys[pygame.K_LSHIFT]:
            camera.pos.y -= move_speed

        # Render and display
        img = camera.render_frane(render_width, render_height, camera, spheres, bounces)
        # Upscale to output resolution using pygame's smoothscale for quality
        surf = pygame.surfarray.make_surface(img.swapaxes(0, 1))
        surf_up = pygame.transform.smoothscale(surf, (output_width, output_height))
        img_up = pygame.surfarray.array3d(surf_up).swapaxes(0, 1)

        # FPS calculation
        frame_count += 1
        now = time.time()
        elapsed = now - last_fps_time
        if elapsed > 0:
            fps = 1.0 / (now - frame_start) if (now - frame_start) > 0 else 0.0

        # Draw FPS on image
        fps_text = f"FPS: {fps:.3f}"
        # Convert numpy array to PIL Image
        img_pil = Image.fromarray(img_up)
        draw = ImageDraw.Draw(img_pil)
        # Use a truetype font or default
        try:
            pil_font = ImageFont.truetype("consola.ttf", 24)
        except:
            pil_font = ImageFont.load_default()
        draw.text((5, 5), fps_text, font=pil_font, fill=(255, 255, 255))

        # Convert back to numpy array
        img_with_fps = np.array(img_pil)

        viewer.set_image(img_with_fps)

    viewer.stop()
    print("Viewer stopped.")
