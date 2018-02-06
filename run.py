import UniformQuan
import NoiseQuan
import orderDither
import FloydSteinbergDither


UniformQuan.main('../img/wallpaper.jpg', './unifrom.png', level=8)
NoiseQuan.main('../img/wallpaper.jpg', './Noise.png', level=4)
orderDither.main('../img/wallpaper.jpg', './orderDither.png')
# FloydSteinbergDither.fsDitherQuan('../img/Einstein.jpg', './FStDitherQuan.jpg', 600, 64)
