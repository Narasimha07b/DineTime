# Create the remaining JavaScript files

# Restaurant page JavaScript
restaurant_js = """// Restaurant Page JavaScript
class RestaurantPage {
  constructor() {
    this.restaurantManager = window.restaurantManager;
    this.currentFilter = '';
    this.currentSort = 'name';
    this.init();
  }

  async init() {
    await this.loadRestaurants();
    this.setupSearch();
    this.setupFilters();
    this.setupSorting();
  }

  async loadRestaurants() {
    const container = document.getElementById('restaurantContainer');
    if (!container) return;

    // Show loading
    container.innerHTML = '<div class="col-12 text-center"><div class="loading-spinner"></div></div>';

    try {
      const restaurants = await this.restaurantManager.fetchRestaurants();
      this.renderRestaurants(restaurants);
    } catch (error) {
      container.innerHTML = '<div class="col-12 text-center text-muted">Failed to load restaurants</div>';
    }
  }

  renderRestaurants(restaurants) {
    const container = document.getElementById('restaurantContainer');
    if (!container) return;

    if (restaurants.length === 0) {
      container.innerHTML = '<div class="col-12 text-center text-muted">No restaurants found</div>';
      return;
    }

    container.innerHTML = '';
    
    restaurants.forEach((restaurant, index) => {
      const card = this.createRestaurantCard(restaurant);
      card.style.animationDelay = `${index * 0.1}s`;
      container.appendChild(card);
    });
  }

  createRestaurantCard(restaurant) {
    const col = document.createElement('div');
    col.className = 'col animate-on-scroll';

    col.innerHTML = `
      <div class="card restaurant-card h-100 fade-in">
        <div class="position-relative">
          <img src="${restaurant.image}" alt="${restaurant.name} Restaurant" 
               class="card-img-top" loading="lazy" 
               onerror="this.src='images/placeholder.jpg'">
          <div class="rating-badge">
            ${restaurant.rating.toFixed(1)} ★
          </div>
        </div>
        <div class="card-body">
          <h5 class="card-title">${restaurant.name}</h5>
          <p class="card-text">${restaurant.description}</p>
          <div class="quick-info">
            <span class="cuisine-tag">${this.getCuisineType(restaurant.name)}</span>
            <div class="btn-group">
              <button class="btn btn-outline-primary btn-sm" onclick="this.showRestaurantDetails('${restaurant.name}')">
                Details
              </button>
              <a href="bookings.html?restaurant=${encodeURIComponent(restaurant.name)}" 
                 class="btn btn-primary btn-sm">Book Now</a>
            </div>
          </div>
        </div>
      </div>
    `;

    return col;
  }

  getCuisineType(restaurantName) {
    const cuisineMap = {
      'DOMINOS': 'Italian',
      'HOTEL GRAND': 'International',
      'DARBAR': 'Indian',
      'RED BUCKET': 'American'
    };
    return cuisineMap[restaurantName] || 'Various';
  }

  setupSearch() {
    const searchForm = document.getElementById('searchForm');
    const searchInput = document.getElementById('searchInput');
    
    if (!searchForm || !searchInput) return;

    const handleSearch = DineTimeUtils.debounce(async () => {
      const searchTerm = searchInput.value.trim();
      const restaurants = await this.restaurantManager.fetchRestaurants();
      let filtered = restaurants;

      if (searchTerm) {
        filtered = this.restaurantManager.searchRestaurants(searchTerm);
      }

      if (this.currentFilter) {
        filtered = this.applyFilter(filtered, this.currentFilter);
      }

      filtered = this.restaurantManager.sortRestaurants(filtered, this.currentSort);
      this.renderRestaurants(filtered);
    }, 300);

    searchInput.addEventListener('input', handleSearch);
    searchForm.addEventListener('submit', (e) => {
      e.preventDefault();
      handleSearch();
    });
  }

  setupFilters() {
    // Create filter bar if it doesn't exist
    const main = document.querySelector('main');
    const existingFilter = document.querySelector('.filter-bar');
    
    if (!existingFilter) {
      const filterBar = document.createElement('div');
      filterBar.className = 'filter-bar';
      filterBar.innerHTML = `
        <div class="filter-controls">
          <label for="ratingFilter">Minimum Rating:</label>
          <select id="ratingFilter" class="form-select filter-select">
            <option value="">All Ratings</option>
            <option value="4.5">4.5+ Stars</option>
            <option value="4.0">4.0+ Stars</option>
            <option value="3.5">3.5+ Stars</option>
          </select>
          
          <div class="sort-controls">
            <button class="sort-btn active" data-sort="name">Name</button>
            <button class="sort-btn" data-sort="rating">Rating</button>
          </div>
        </div>
      `;
      
      main.insertBefore(filterBar, main.querySelector('h1').nextSibling);
    }

    // Setup filter event listeners
    const ratingFilter = document.getElementById('ratingFilter');
    if (ratingFilter) {
      ratingFilter.addEventListener('change', this.handleFilterChange.bind(this));
    }
  }

  setupSorting() {
    document.addEventListener('click', (e) => {
      if (e.target.classList.contains('sort-btn')) {
        // Update active sort button
        document.querySelectorAll('.sort-btn').forEach(btn => btn.classList.remove('active'));
        e.target.classList.add('active');
        
        this.currentSort = e.target.dataset.sort;
        this.handleFilterChange();
      }
    });
  }

  async handleFilterChange() {
    const ratingFilter = document.getElementById('ratingFilter');
    this.currentFilter = ratingFilter ? ratingFilter.value : '';

    const restaurants = await this.restaurantManager.fetchRestaurants();
    let filtered = restaurants;

    // Apply search filter
    const searchInput = document.getElementById('searchInput');
    if (searchInput && searchInput.value.trim()) {
      filtered = this.restaurantManager.searchRestaurants(searchInput.value.trim());
    }

    // Apply rating filter
    if (this.currentFilter) {
      filtered = this.applyFilter(filtered, this.currentFilter);
    }

    // Apply sorting
    filtered = this.restaurantManager.sortRestaurants(filtered, this.currentSort);
    
    this.renderRestaurants(filtered);
  }

  applyFilter(restaurants, filterValue) {
    switch (filterValue) {
      case '4.5':
        return restaurants.filter(r => r.rating >= 4.5);
      case '4.0':
        return restaurants.filter(r => r.rating >= 4.0);
      case '3.5':
        return restaurants.filter(r => r.rating >= 3.5);
      default:
        return restaurants;
    }
  }

  showRestaurantDetails(restaurantName) {
    // This could be enhanced to show a modal with more details
    DineTimeUtils.showToast(`More details for ${restaurantName} coming soon!`, 'info');
  }
}

// Initialize restaurant page when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  new RestaurantPage();
});
"""

# Booking page JavaScript
booking_js = """// Booking Page JavaScript
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
        pattern: /^[a-zA-Z\\s]+$/,
        message: 'Please enter a valid name (letters only, minimum 2 characters)'
      },
      email: {
        required: true,
        pattern: /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/,
        message: 'Please enter a valid email address'
      },
      phone: {
        required: true,
        pattern: /^\\+?[0-9\\-\\s]{7,15}$/,
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
"""

# Write the remaining JavaScript files
with open('js/restaurant.js', 'w', encoding='utf-8') as f:
    f.write(restaurant_js)

with open('js/booking.js', 'w', encoding='utf-8') as f:
    f.write(booking_js)

print("✅ Created js/restaurant.js")
print("✅ Created js/booking.js")