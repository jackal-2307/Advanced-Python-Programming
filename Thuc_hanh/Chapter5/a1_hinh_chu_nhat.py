class HinhChuNhat:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def tinh_dien_tich(self):
        return self.length * self.width


if __name__ == "__main__":
    hinh = HinhChuNhat(5, 3)
    print(hinh.tinh_dien_tich())
