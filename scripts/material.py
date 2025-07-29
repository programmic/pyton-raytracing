class Material:
    def __init__(self,
                 color: tuple[int, int, int],
                 specularity: float
                 ) -> None:
        self.color = color
        self.specularity = specularity