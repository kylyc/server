// Mobile Menu
const mobileMenuOpenIcon = document.querySelector('.mobile-menu-open-icon');
const mobileMenuCloseIcon = document.querySelector('.mobile-menu-close-icon');
const mobileMenu = document.querySelector('.mobile-menu');

function toggleMobileMenu() {
  mobileMenu.classList.toggle('show-menu');
}

mobileMenuOpenIcon.addEventListener('click', toggleMobileMenu);
mobileMenuCloseIcon.addEventListener('click', toggleMobileMenu);

// CounterUp
function initWaypoint(elements, callback) {
  var waypoint = new IntersectionObserver(
    function (entries, observer) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          callback(entry.target);
          observer.unobserve(entry.target);
        }
      });
    },
    {
      threshold: 0.8, // Adjust the threshold as needed
    },
  );

  elements.forEach(function (element) {
    waypoint.observe(element);
  });
}

// Find all elements with class 'counter'
var counterElements = document.querySelectorAll('.counter');

// Usage
initWaypoint(counterElements, function (target) {
  var finalValue = parseInt(target.textContent, 10);
  var duration = 2000; // Set the duration of the counter animation
  var startTime = performance.now();

  function updateValue(timestamp) {
    var progress = timestamp - startTime;
    var value = Math.floor((progress / duration) * finalValue);

    if (value <= finalValue) {
      target.textContent = value;
      requestAnimationFrame(updateValue);
    } else {
      target.textContent = finalValue;
    }
  }

  requestAnimationFrame(updateValue);
});
