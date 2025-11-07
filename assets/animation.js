document.addEventListener("touchend", function() {
  try {
    const activeElement = document.activeElement;
    if (activeElement) {
      activeElement.blur();
    }
  } catch (e) {
    console.error("Error on touchend:", e);
  }
});