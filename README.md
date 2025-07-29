# Raytracer

A simple Python raytracer project in development.

## Features

- **Vector math**: Custom `vec3` class for 3D vector operations.
- **Image viewer**: Live 720p window for displaying rendered images, updatable at runtime.
- **Unit tests**: Comprehensive tests for vector operations.
- **Modular structure**: Easy to extend and maintain.

## Requirements

- Python 3.8+
- [numpy](https://numpy.org/)
- [pygame](https://www.pygame.org/) (for the image viewer)

Install dependencies with:

```sh
pip install numpy pygame
```

## Project Structure

```
raytracer/
├── scripts/
│   ├── main.py      # Entry point, launches the viewer
│   ├── vec3.py      # 3D vector math
│   └── viewer.py    # Image viewer (window)
├── tests/
│   └── test_vec3.py # Unit tests for vec3
└── README.md
```

## Usage

Run the main script to start the image viewer:

```sh
python scripts/main.py
```

You can update the displayed image at runtime by calling `viewer.set_image(img)` with a NumPy array of shape `(720, 1280, 3)`.

## Development

- Extend `vec3` for more vector operations as needed.
- Implement raytracing logic in new modules.
- Add more tests in the `tests/` directory.

## Progress

Current progress is shown in `projectmanagement.md`

## License

MIT License