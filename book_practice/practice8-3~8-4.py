# 练习8-3
def make_shirt(size,shape):
    print("这个T恤的尺码是",size,"，字样是",shape,"。")
make_shirt('L','Love')

# 练习8-4
def make_shirt(size='XL',shape='I love Python'):
    print("这个T恤的尺码是",size,"，字样是",shape,"。")
make_shirt()
make_shirt('L')
make_shirt('XL','Yes')