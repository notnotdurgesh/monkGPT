document.addEventListener('DOMContentLoaded', function () {
  const resultContainer = document.querySelector('.result-container p');

  if (resultContainer) {
      const text = resultContainer.textContent;
      resultContainer.innerHTML = '';
      let i = 0;

      function typeWriter() {
        if (i < text.length) {
            resultContainer.innerHTML += text.charAt(i);
            i++;
            setTimeout(typeWriter, 50); // Change this value to make the typing faster or slower
        } else {
            blinkCaret();
        }
    }

      function blinkCaret() {
          resultContainer.style.borderRight = resultContainer.style.borderRight === '2px solid #fff' ? '2px solid transparent' : '2px solid #fff';
          setTimeout(blinkCaret, 500);
      }

      typeWriter();
  }
});

