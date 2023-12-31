from PIL import Image

icon = Image.open("image/reload_icon.png")
reload_icon = icon.resize((40, 40), Image.LANCZOS)

icon_2 = Image.open("image/logout.png")
logout_icon = icon_2.resize((30, 30), Image.LANCZOS)

icon_3 = Image.open("image/chatroom.png")
chatroom_icon = icon_3.resize((70, 45), Image.LANCZOS)

icon_4 = Image.open("image/R.jpg")
public_icon = icon_4.resize((70, 45), Image.LANCZOS)

img = Image.open("image/im.png")
request_image = img.resize((90, 55), Image.LANCZOS)

img_2 = Image.open("image/im2.png")
friend_image = img_2.resize((70, 70), Image.LANCZOS)

img_3 = Image.open("image/signup.jpg")
signup_image = img_3.resize((520, 480), Image.LANCZOS)

img_4 = Image.open("image/login.jpg")
login_image = img_4.resize((520, 480), Image.LANCZOS)
