import threading
import pygame
import numpy as np

class ImageViewer:
    def __init__(self, width=1280, height=720):
        self.width = width
        self.height = height
        self._image = np.zeros((height, width, 3), dtype=np.uint8)
        self._lock = threading.Lock()
        self._running = False
        self._thread = None

    def set_image(self, img: np.ndarray):
        """Update the image to display. img must be (height, width, 3) uint8."""
        if img.shape != (self.height, self.width, 3) or img.dtype != np.uint8:
            raise ValueError("Image must be shape (720, 1280, 3) and dtype uint8")
        with self._lock:
            self._image = img.copy()

    def _run(self):
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Image Viewer")
        clock = pygame.time.Clock()
        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                    break
            with self._lock:
                surf = pygame.surfarray.make_surface(self._image.swapaxes(0, 1))
            screen.blit(surf, (0, 0))
            pygame.display.flip()
        pygame.quit()

    def start(self):
        if self._thread is not None and self._thread.is_alive():
            return
        self._running = True
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()

    def stop(self):
        self._running = False
        if self._thread is not None:
            self._thread.join()