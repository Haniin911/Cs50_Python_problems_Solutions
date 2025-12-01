from fpdf import FPDF

def main():
    # Prompt user for their name
    name = input("Name: ").strip()
    if not name:
        print("You must enter a name.")
        return

    # Create PDF
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Add title at the top
    pdf.set_font("Arial", "B", 24)
    pdf.set_text_color(0, 0, 0)  # Black text
    pdf.cell(0, 20, "CS50 Shirtificate", ln=True, align="C")

    # Add the shirt image centered
    shirt_path = "shirtificate.png"  # Make sure this image is in the same folder
    pdf.image(shirt_path, x=55, y=50, w=100)  # x=55 centers a 100mm wide image on A4 (210mm)

    # Add user's name on top of the shirt
    pdf.set_font("Arial", "B", 32)
    pdf.set_text_color(255, 255, 255)  # White text
    pdf.set_y(90)  # Adjust vertically over the shirt
    pdf.cell(0, 10, name, ln=True, align="C")

    # Optional: Add some borders or decorations
    pdf.set_draw_color(0, 0, 0)  # Black border
    pdf.rect(10, 10, 190, 277)  # Draw border around page

    # Output PDF
    pdf.output("shirtificate.pdf")
    print("shirtificate.pdf created successfully!")

if __name__ == "__main__":
    main()
