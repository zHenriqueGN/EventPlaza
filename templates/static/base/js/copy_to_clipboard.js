function copyToClipboard(elementId) {
    var copyText = document.getElementById(elementId);
  
    text = copyText.getAttribute("toCopy");
  
    navigator.clipboard.writeText(text);

    Swal.fire({
        position: 'center',
        width: '20rem',
        icon: 'success',
        title: 'Copied to clipboard!',
        showConfirmButton: false,
        timer: 1000,
      })
}