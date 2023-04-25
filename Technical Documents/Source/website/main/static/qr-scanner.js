document.getElementById('qr-icon').addEventListener('click', function () {
  // Create a new div element for the QR scanner and insert it before the existing reader div
  const qrScannerDiv = document.createElement('div');
  qrScannerDiv.id = 'qr-scanner';
  const reader = document.getElementById('reader');
  reader.parentNode.insertBefore(qrScannerDiv, reader);

  // Initialize the QR code scanner
  const scanner = new Html5QrcodeScanner('qr-scanner', {
    qrbox: {
      width: 250,
      height: 250,
    },
    fps: 20,
  });

  // Render the QR code scanner and handle success and error
  scanner.render(
    function success(result) {
      console.log(`QR code scanned: ${result}`);
      scanner.clear();
      qrScannerDiv.remove();

      let redirectToQuiz = false;

      if (result === "aSuaAkezT1") {
        redirectToQuiz = true;
        window.location.href = '/store';
      } else {
        for (const event of window.events) {
          if (event.locationId__qrCode === result) {
            redirectToQuiz = true;
            window.location.href = `/quiz/${event.eventId}`;
            break;
          }
        }
      }

      if (!redirectToQuiz) {
        alert('Invalid QR code. Please try again.');
      }
    },
    function error(err) {
      console.error(err);
    }
  );
});