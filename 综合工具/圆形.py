from PIL import Image, ImageDraw

# 创建一个空白的 RGBA 图像
image = Image.new("RGBA", (1024, 1024), (0, 0, 0, 0))

# 创建一个绘制对象，并设置抗锯齿
draw = ImageDraw.Draw(image)
draw.smooth = True

# 定义圆形参数
circle_radius = 500
circle_center = (512, 512)
circle_color = (0, 0, 0, 255)  # 黑色填充

# 绘制实心圆形
draw.ellipse((circle_center[0] - circle_radius, circle_center[1] - circle_radius,
              circle_center[0] + circle_radius + 1, circle_center[1] + circle_radius + 1),
             fill=circle_color)

# 保存图像为PNG格式
image.save("circle.png", "PNG")