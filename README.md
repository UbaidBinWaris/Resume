# Personal Resume Website

A modern, responsive, and printable resume website built with pure HTML, CSS, and JavaScript. This project showcases a professional resume that can be viewed in a browser and exported to PDF format.

## Features

- **Responsive Design**: Clean and professional layout optimized for web viewing
- **PDF Export**: Built-in functionality to download resume as PDF using html2pdf.js
- **Modern UI**: Professional color scheme with teal (#449399) accents and clean typography
- **Organized Sections**: 
  - Personal information with profile picture
  - Contact details (Email, Phone, Location, LinkedIn, GitHub, Stack Overflow)
  - Education history
  - Professional skills
  - Work experience
  - Personal projects
  - Certificates
  - Languages
  - Interests

## Demo

Open `index.html` in any modern web browser to view the resume.

## Prerequisites

- Any modern web browser (Chrome, Firefox, Safari, Edge)
- No server or build tools required - this is a static website

## Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/UbaidBinWaris/Resume.git
   cd Resume
   ```

2. **Open the resume**
   - Simply open `index.html` in your web browser
   - Or use a local server:
     ```bash
     # Using Python 3
     python -m http.server 8000
     
     # Using Node.js http-server
     npx http-server
     ```

3. **Export to PDF**
   - Open browser developer console (F12)
   - Copy and paste the following code:
     ```javascript
     var script = document.createElement('script');
     script.src = 'https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js';
     document.head.appendChild(script);

     setTimeout(() => {
       var element = document.querySelector(".resume");
       html2pdf()
         .from(element)
         .set({
           margin: [-0.7, 0, 0, 0],
           filename: 'Ubaid.pdf',
           html2canvas: { scale: 2 },
           jsPDF: { unit: 'in', format: 'a4', orientation: 'portrait' }
         })
         .save();
     }, 1000);
     ```

## Project Structure

```
Resume/
├── index.html          # Main HTML file with resume content
├── style.css           # Styling and responsive design
├── script.js           # PDF export functionality (console commands)
├── resources/          # Images and icons
│   ├── me.jpg         # Profile picture
│   ├── mail.svg       # Email icon
│   ├── phone.svg      # Phone icon
│   ├── location.svg   # Location icon
│   ├── linkin.svg     # LinkedIn icon
│   ├── github.svg     # GitHub icon
│   └── stackoverflow.svg # Stack Overflow icon
└── README.md          # Project documentation
```

## Customization

### Changing Colors
Edit `style.css` and update the color values:
- Primary color: `#449399` (teal)
- Dark color: `#313c4e`
- Background: `rgb(49, 59, 71)`

### Updating Content
Edit `index.html` to modify:
- Personal information
- Education details
- Skills list
- Work experience
- Projects
- Contact information

### Adding Your Photo
Replace `resources/me.jpg` with your own professional photo (recommended: 500x500px, square format)

## Technologies Used

- **HTML5**: Semantic markup and structure
- **CSS3**: Modern styling with Flexbox layout
- **JavaScript**: PDF export functionality
- **html2pdf.js**: Library for converting HTML to PDF
- **Google Fonts**: Roboto font family
- **SVG Icons**: Scalable vector graphics for contact information

## Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge
- Opera

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**Ubaid Bin Waris**
- Email: ubaidwaris34@gmail.com
- LinkedIn: [linkedin.com/in/ubaid-waris-441942284](https://linkedin.com/in/ubaid-waris-441942284)
- GitHub: [@UbaidBinWaris](https://github.com/UbaidBinWaris)
- Stack Overflow: [ubaid-bin-waris](https://stackoverflow.com/users/21611585/ubaid-bin-waris)

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/UbaidBinWaris/Resume/issues).

## Show your support

Give a star if this project helped you!u!

## Notes

- The resume is designed for A4 paper size (210mm × 297mm)
- Print styles are optimized for best PDF output quality
- All icons should be in SVG format for crisp rendering
- The layout uses absolute positioning for precise element placement

---

**Made by Ubaid Bin Waris**
