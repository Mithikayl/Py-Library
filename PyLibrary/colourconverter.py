def main():
    print("[*] Hex to RGB")
    hex = input("[*] Enter a hex color: \n")
    print("[+] Converting...")
    rgb = hex_to_rgb(hex)
    print("[*] RGB: {}".format(rgb))
    print("[*] Hex: {}".format(rgb_to_hex(rgb)))
    pass

def hex_to_rgb(hex):
    hex = hex.lstrip('#')
    hlen = len(hex)
    return tuple(int(hex[i:i + hlen // 3], 16) for i in range(0, hlen, hlen // 3))

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

