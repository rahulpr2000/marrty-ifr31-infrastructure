
import sys

try:
    with open('template.yaml', 'rb') as f:
        content = f.read()

    # Try decoding
    try:
        text = content.decode('utf-8')
    except UnicodeDecodeError:
        try:
            text = content.decode('utf-16')
        except UnicodeDecodeError:
            text = content.decode('cp1252')
            
    # Normalize to ASCII
    text = text.encode('ascii', 'ignore').decode('ascii')
    
    # Write back as utf-8 (which is now ascii subset)
    with open('template.yaml', 'w', encoding='utf-8') as f:
        f.write(text)
    
    print("Successfully converted template.yaml to ASCII")

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
