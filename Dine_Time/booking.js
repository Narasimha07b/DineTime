// Booking Page JavaScript
class BookingPage {
  constructor() {
    this.restaurantManager = window.restaurantManager;
    this.currentStep = 1;
    this.bookingData = {};
    this.init();
  }

  async init() {
    await this.loadRestaurantOptions();
    this.setupForm();
    this.setupValidation();
    this.handleUrlParams();
    this.setupDateTimeRestrictions();
  }

  async loadRestaurantOptions() {
    try {
      const restaurants = await this.restaurantManager.fetchRestaurants();
      const restaurantSelect = document.getElementById('restaurant');

      if (restaurantSelect && restaurants.length > 0) {
        // Clear existing options except the first one
        const firstOption = restaurantSelect.firstElementChild;
        restaurantSelect.innerHTML = '';
        restaurantSelect.appendChild(firstOption);

        // Add restaurant options
        restaurants.forEach(restaurant => {
          const option = document.createElement('option');
          option.value = restaurant.name;
          option.textContent = restaurant.name;
          restaurantSelect.appendChild(option);
        });
      }
    } catch (error) {
      console.error('Failed to load restaurant options:', error);
    }
  }

  handleUrlParams() {
    const restaurantParam = DineTimeUtils.getQueryParam('restaurant');
    if (restaurantParam) {
      const restaurantSelect = document.getElementById('restaurant');
      if (restaurantSelect) {
        for (const option of restaurantSelect.options) {
          if (option.value === restaurantParam) {
            option.selected = true;
            break;
          }
        }
      }
    }
  }

  setupDateTimeRestrictions() {
    // Set minimum date to today
    const dateInput = document.getElementById('date');
    if (dateInput) {
      const today = new Date().toISOString().split('T')[0];
      dateInput.min = today;

      // Set maximum date to 3 months from now
      const maxDate = new Date();
      maxDate.setMonth(maxDate.getMonth() + 3);
      dateInput.max = maxDate.toISOString().split('T')[0];
    }

    // Set time restrictions
    const timeInput = document.getElementById('time');
    if (timeInput) {
      timeInput.min = '10:00';
      timeInput.max = '22:00';
      timeInput.step = '1800'; // 30-minute intervals
    }
  }

  setupForm() {
    const form = document.getElementById('bookingForm');
    if (!form) return;

    // Add progress indicator
    this.addProgressIndicator();

    // Add real-time validation feedback
    const inputs = form.querySelectorAll('input, select, textarea');
    inputs.forEach(input => {
      input.addEventListener('blur', () => this.validateField(input));
      input.addEventListener('input', () => this.clearFieldError(input));
    });

    // Add booking summary
    this.addBookingSummary();

    form.addEventListener('submit', this.handleSubmit.bind(this));
  }

  addProgressIndicator() {
    const form = document.getElementById('bookingForm');
    const progressDiv = document.createElement('div');
    progressDiv.className = 'progress-indicator';
    progressDiv.innerHTML = `
      <div class="progress-step active">1</div>
      <div class="progress-step">2</div>
      <div class="progress-step">3</div>
    `;
    form.insertBefore(progressDiv, form.firstChild);
  }

  addBookingSummary() {
    const form = document.getElementById('bookingForm');
    const summaryDiv = document.createElement('div');
    summaryDiv.id = 'bookingSummary';
    summaryDiv.className = 'booking-summary d-none';
    summaryDiv.innerHTML = `
      <h4>Booking Summary</h4>
      <div class="summary-item">
        <span>Restaurant:</span>
        <span id="summaryRestaurant">-</span>
      </div>
      <div class="summary-item">
        <span>Date:</span>
        <span id="summaryDate">-</span>
      </div>
      <div class="summary-item">
        <span>Time:</span>
        <span id="summaryTime">-</span>
      </div>
      <div class="summary-item">
        <span>Guests:</span>
        <span id="summaryGuests">-</span>
      </div>
    `;

    const submitButton = form.querySelector('button[type="submit"]');
    form.insertBefore(summaryDiv, submitButton.parentElement);
  }

  setupValidation() {
    // Enhanced validation rules
    const validationRules = {
      name: {
        required: true,
        minLength: 2,
        pattern: /^[a-zA-Z\s]+$/,
        message: 'Please enter a valid name (letters only, minimum 2 characters)'
      },
      email: {
        required: true,
        pattern: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
        message: 'Please enter a valid email address'
      },
      phone: {
        required: true,
        pattern: /^\+?[0-9\-\s]{7,15}$/,
        message: 'Please enter a valid phone number'
      },
      restaurant: {
        required: true,
        message: 'Please select a restaurant'
      },
      date: {
        required: true,
        custom: this.validateDate,
        message: 'Please select a valid date'
      },
      time: {
        required: true,
        custom: this.validateTime,
        message: 'Please select a valid time'
      },
      guests: {
        required: true,
        min: 1,
        max: 20,
        message: 'Number of guests must be between 1 and 20'
      }
    };

    this.validationRules = validationRules;
  }

  validateField(field) {
    const rules = this.validationRules[field.id];
    if (!rules) return true;

    const value = field.value.trim();
    let isValid = true;
    let message = '';

    // Required validation
    if (rules.required && !value) {
      isValid = false;
      message = 'This field is required';
    }
    // Pattern validation
    else if (rules.pattern && !rules.pattern.test(value)) {
      isValid = false;
      message = rules.message;
    }
    // Length validation
    else if (rules.minLength && value.length < rules.minLength) {
      isValid = false;
      message = rules.message;
    }
    // Number validation
    else if (rules.min && parseInt(value) < rules.min) {
      isValid = false;
      message = rules.message;
    }
    else if (rules.max && parseInt(value) > rules.max) {
      isValid = false;
      message = rules.message;
    }
    // Custom validation
    else if (rules.custom && !rules.custom(value)) {
      isValid = false;
      message = rules.message;
    }

    this.setFieldValidation(field, isValid, message);
    return isValid;
  }

  validateDate(dateString) {
    const selectedDate = new Date(dateString);
    const today = new Date();
    today.setHours(0, 0, 0, 0);

    return selectedDate >= today;
  }

  validateTime(timeString) {
    const [hours, minutes] = timeString.split(':').map(Number);
    const timeInMinutes = hours * 60 + minutes;

    // Restaurant hours: 10:00 AM to 10:00 PM
    return timeInMinutes >= 600 && timeInMinutes <= 1320;
  }

  setFieldValidation(field, isValid, message) {
    const feedback = field.parentElement.querySelector('.invalid-feedback');

    if (isValid) {
      field.classList.remove('is-invalid');
      field.classList.add('is-valid');
    } else {
      field.classList.remove('is-valid');
      field.classList.add('is-invalid');
      if (feedback) {
        feedback.textContent = message;
      }
    }
  }

  clearFieldError(field) {
    field.classList.remove('is-invalid');
  }

  updateBookingSummary() {
    const summary = document.getElementById('bookingSummary');
    const restaurant = document.getElementById('restaurant').value;
    const date = document.getElementById('date').value;
    const time = document.getElementById('time').value;
    const guests = document.getElementById('guests').value;

    if (restaurant && date && time && guests) {
      document.getElementById('summaryRestaurant').textContent = restaurant;
      document.getElementById('summaryDate').textContent = DineTimeUtils.formatDate(date);
      document.getElementById('summaryTime').textContent = DineTimeUtils.formatTime(time);
      document.getElementById('summaryGuests').textContent = guests;

      summary.classList.remove('d-none');
    } else {
      summary.classList.add('d-none');
    }
  }

  async handleSubmit(e) {
    e.preventDefault();

    const form = e.target;
    let isFormValid = true;

    // Validate all fields
    const fields = form.querySelectorAll('input[required], select[required]');
    fields.forEach(field => {
      if (!this.validateField(field)) {
        isFormValid = false;
      }
    });

    if (!isFormValid) {
      form.classList.add('was-validated');
      DineTimeUtils.showToast('Please correct the errors in the form', 'error');
      return;
    }

    // Collect form data
    const formData = new FormData(form);
    const bookingData = Object.fromEntries(formData.entries());

    // Add timestamp
    bookingData.timestamp = new Date().toISOString();
    bookingData.id = 'BOOK-' + Date.now();

    // Save booking (in real app, this would go to a server)
    this.saveBooking(bookingData);

    // Show confirmation
    this.showConfirmation(bookingData);

    // Reset form
    form.reset();
    form.classList.remove('was-validated');
    document.getElementById('bookingSummary').classList.add('d-none');
  }

  saveBooking(bookingData) {
    // Save to localStorage for demo purposes
    let bookings = DineTimeUtils.getFromStorage('dinetime_bookings') || [];
    bookings.push(bookingData);
    DineTimeUtils.saveToStorage('dinetime_bookings', bookings);
  }

  showConfirmation(bookingData) {
    const message = `
      <div class="text-center">
        <div class="mb-3">
          <i class="fas fa-check-circle text-success" style="font-size: 3rem;"></i>
        </div>
        <h5>Booking Confirmed!</h5>
        <p>Thank you, <strong>${bookingData.name}</strong>, for booking with us.</p>
        <div class="alert alert-info">
          <strong>Booking ID:</strong> ${bookingData.id}<br>
          <strong>Restaurant:</strong> ${bookingData.restaurant}<br>
          <strong>Date:</strong> ${DineTimeUtils.formatDate(bookingData.date)}<br>
          <strong>Time:</strong> ${DineTimeUtils.formatTime(bookingData.time)}<br>
          <strong>Guests:</strong> ${bookingData.guests}
        </div>
        ${bookingData.special ? `<p><em>Special requests: ${bookingData.special}</em></p>` : ''}
        <p class="text-muted">We look forward to serving you!</p>
      </div>
    `;

    const confirmationMessage = document.getElementById('confirmationMessage');
    confirmationMessage.innerHTML = message;

    const confirmationModal = new bootstrap.Modal(document.getElementById('confirmationModal'));
    confirmationModal.show();
  }
}

// Add event listeners for real-time summary updates
document.addEventListener('DOMContentLoaded', () => {
  const bookingPage = new BookingPage();

  // Update summary when key fields change
  ['restaurant', 'date', 'time', 'guests'].forEach(fieldId => {
    const field = document.getElementById(fieldId);
    if (field) {
      field.addEventListener('change', () => bookingPage.updateBookingSummary());
    }
  });
});
