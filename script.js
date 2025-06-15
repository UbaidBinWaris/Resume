<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.9.2/html2pdf.bundle.min.js"></script>

    var element = document.querySelector(".resume"); // The element you want to convert to PDF
    html2pdf()
        .from(element)
        .set({
            margin: 1,
            filename: 'myCV.pdf',
            html2canvas: { scale: 2 },
            jsPDF: { unit: 'in', format: 'a4', orientation: 'portrait' }
        })
        .save(); 


//Run in console

    //     var element = document.querySelector(".resume"); // The element you want to convert to PDF
    // html2pdf()
    // .from(element)
    // .set({
    //     margin: [-0.7, 0, 0, 0], // 0 margin for full control
    //     filename: 'myCV.pdf',
    //     html2canvas: { scale: 2 }, // Increase scale for better quality
    //     jsPDF: { unit: 'in', format: 'a4', orientation: 'portrait' }
    // })
    // .save();
