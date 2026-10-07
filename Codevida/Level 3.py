## Task 1 //


from pathlib import Path


def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')

            new_char = chr(
                (ord(char) - base + shift) % 26 + base
            )
            result += new_char
        else:
            result += char

    return result


def main():
    print("=== File Encryption & Decryption ===")
    print("1. Encrypt a file")
    print("2. Decrypt a file")

    choice = input("Choose an option (1/2): ").strip()
    file_name = input("Enter the input file path: ").strip()

    if choice not in ("1", "2"):
        print("Invalid choice!")
        return

    input_path = Path(file_name)

    if not input_path.is_file():
        print("Error: File not found!")
        return

    try:
        shift = int(input("Enter the shift key (0-25): "))
        if not 0 <= shift <= 25:
            print("Shift must be between 0 and 25.")
            return

        text = input_path.read_text(encoding="utf-8")

        if choice == "1":
            processed_text = caesar_cipher(text, shift)
            output_path = input_path.with_name(
                input_path.stem + "_encrypted.txt"
            )
            action = "encrypted"
        else:
            processed_text = caesar_cipher(text, -shift)
            output_path = input_path.with_name(
                input_path.stem + "_decrypted.txt"
            )
            action = "decrypted"

        if output_path.exists():
            print("Error: Output file already exists.")
            print("Rename or remove it before trying again.")
            return

        output_path.write_text(
            processed_text, encoding="utf-8"
        )

        print(f"File successfully {action}!")
        print(f"Saved to: {output_path.resolve()}")

    except (ValueError, OSError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()

## Task 2 //

