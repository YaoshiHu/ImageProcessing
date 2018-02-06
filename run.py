import Uniform
import orderDither
import FloydSteinbergDither


# Uniform.uniformQuan('../img/wallpaper.jpg', './uniformQuan.jpg', 600, 8)
Uniform.noiseQuan('../img/Einstein.jpg', './noiseQuan.jpg', 600, 64)
# orderDither.orderDither('../img/Einstein.jpg', './ditherQuan.jpg', 600, 3)
FloydSteinbergDither.fsDitherQuan('../img/Einstein.jpg', './FStDitherQuan.jpg', 600, 64)
