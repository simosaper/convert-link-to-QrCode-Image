import os
import sys
import subprocess
import qrcode
import time

def install_dependencies():
    try:
        import qrcode
    except ImportError:
        print("Installing required packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "qrcode[pillow]"])
        print("Packages installed successfully!")

def generate_qr(url):
    """Generate and display QR code in terminal and save as image"""
    # Create QR code instance
    qr = qrcode.QRCode()
    qr.add_data(url)
    
    # Display in terminal
    qr.print_ascii()
    
    # Save as PNG image
    img = qr.make_image(fill_color="black", back_color="white")
    filename = f"qr_{int(time.time())}.png"
    img.save(filename)
    print(f"\nQR code saved as: {os.path.abspath(filename)}")
    return filename

def get_url():
    """Get URL from user input with basic validation"""
    while True:
        print("""
                                         
                                 
    █▀▀▀▀▀█ ▀  █ ▀▄▀█ █▀▀▀▀▀█    
    █ ███ █ ▄▀▀█ ▄█ ▄ █ ███ █    
    █ ▀▀▀ █ █▀▄▀ ██▀█ █ ▀▀▀ █    
    ▀▀▀▀▀▀▀ █▄▀▄█ █▄▀ ▀▀▀▀▀▀▀    
    █▄▄ ▀▄▀███▄█▀▄ █▄▀▀███ ▄▀    
    ▀ ▄█▀ ▀ ▄█▀█   █▀▄█▄ ▀█▄     
    ▄ █▀██▀▄█ █▀▄▄▄█▄▀▀ ▄▀▀█▀    
       ▄▄ ▀▄ ▄▄█▀ █▀▄ ▀██▀█▄     
    ▀▀▀▀ ▀▀ ▄▄  ▀▄ ▄█▀▀▀█▀▀      
    █▀▀▀▀▀█ ▀█  ▄▀  █ ▀ █▄▄▄▄    
    █ ███ █ ▀▀█▀▄▀█▄████▀▀███    
    █ ▀▀▀ █  ███▀█▀▄ ▀▀▄▄█▄█     
    ▀▀▀▀▀▀▀ ▀   ▀▀   ▀▀   ▀▀▀  

        by: @simosaper11
        """)
        url = input("Enter URL to convert: ").strip()
        if url.startswith(('http://', 'https://')):
            return url
        print("Invalid URL! Please include http:// or https://")

def main():
    install_dependencies()
    print("\n=== QR Code Generator ===")
    url = get_url()
    print("\nScan this QR code:")
    filename = generate_qr(url)
    print(f"\nContains: {url}")
    print("coder: @simosaper11")
    print("share and support: @slmosaper")
    time.sleep(100)

if __name__ == "__main__":
    main()