# Create JavaScript files for each page with enhanced functionality

# Main JavaScript utilities that will be used across pages
utils_js = """// DINETIME - Utility Functions
class DineTimeUtils {
  // Debounce function to limit the rate of function calls
  static debounce(func, wait) {
    let timeout;
    return function (...args) {
      clearTimeout(timeout);
      timeout = setTimeout(() => func.apply(this, args), wait);
    };
  }

  // Show loading spinner
  static showLoading(element) {
    const spinner = document.createElement('div');
    spinner.className = 'loading-spinner';
    spinner.innerHTML = '<div class="spinner-border text-primary" role="status"><span class="visually-hidden">Loading...</span></div>';
    element.appendChild(spinner);
    return spinner;
  }

  // Hide loading spinner
  static hideLoading(spinner) {
    if (spinner && spinner.parentNode) {
      spinner.parentNode.removeChild(spinner);
    }
  }

  // Get query parameter by name
  static getQueryParam(param) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(param);
  }

  // Format date to readable string
  static formatDate(dateString) {
    const options = { 
      weekday: 'long', 
      year: 'numeric', 
      month: 'long', 
      day: 'numeric' 
    };
    return new Date(dateString).toLocaleDateString('en-US', options);
  }

  // Format time to readable string
  static formatTime(timeString) {
    const [hours, minutes] = timeString.split(':');
    const date = new Date();
    date.setHours(hours, minutes);
    return date.toLocaleTimeString('en-US', { 
      hour: 'numeric', 
      minute: '2-digit', 
      hour12: true 
    });
  }

  // Show toast notification
  static showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `toast-notification toast-${type}`;
    toast.innerHTML = `
      <div class="toast-content">
        <span class="toast-message">${message}</span>
        <button class="toast-close">&times;</button>
      </div>
    `;
    
    document.body.appendChild(toast);
    
    setTimeout(() => toast.classList.add('show'), 100);
    
    // Auto remove after 5 seconds
    setTimeout(() => {
      toast.classList.remove('show');
      setTimeout(() => document.body.removeChild(toast), 300);
    }, 5000);
    
    // Manual close
    toast.querySelector('.toast-close').addEventListener('click', () => {
      toast.classList.remove('show');
      setTimeout(() => document.body.removeChild(toast), 300);
    });
  }

  // Local storage helpers
  static saveToStorage(key, data) {
    try {
      localStorage.setItem(key, JSON.stringify(data));
      return true;
    } catch (error) {
      console.error('Failed to save to storage:', error);
      return false;
    }
  }

  static getFromStorage(key) {
    try {
      const data = localStorage.getItem(key);
      return data ? JSON.parse(data) : null;
    } catch (error) {
      console.error('Failed to retrieve from storage:', error);
      return null;
    }
  }

  // Animation helpers
  static animateOnScroll() {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('animate-fade');
        }
      });
    });

    document.querySelectorAll('.animate-on-scroll').forEach(el => {
      observer.observe(el);
    });
  }
}

// Restaurant data manager
class RestaurantManager {
  constructor() {
    this.restaurants = [];
    this.loaded = false;
  }

  async fetchRestaurants() {
    if (this.loaded) return this.restaurants;
    
    try {
      const response = await fetch('restaurants.json');
      if (!response.ok) throw new Error('Failed to load restaurant data');
      this.restaurants = await response.json();
      this.loaded = true;
      return this.restaurants;
    } catch (error) {
      console.error('Error fetching restaurants:', error);
      DineTimeUtils.showToast('Failed to load restaurant data', 'error');
      return [];
    }
  }

  searchRestaurants(searchTerm) {
    const lowerTerm = searchTerm.toLowerCase();
    return this.restaurants.filter(restaurant =>
      restaurant.name.toLowerCase().includes(lowerTerm) ||
      restaurant.description.toLowerCase().includes(lowerTerm)
    );
  }

  filterByRating(minRating) {
    return this.restaurants.filter(restaurant => restaurant.rating >= minRating);
  }

  sortRestaurants(restaurants, sortBy) {
    switch (sortBy) {
      case 'name':
        return [...restaurants].sort((a, b) => a.name.localeCompare(b.name));
      case 'rating':
        return [...restaurants].sort((a, b) => b.rating - a.rating);
      default:
        return restaurants;
    }
  }
}

// Global restaurant manager instance
window.restaurantManager = new RestaurantManager();

// Initialize animations when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  DineTimeUtils.animateOnScroll();
});
"""

# Home page JavaScript
home_js = """// Home Page JavaScript
class HomePage {
  constructor() {
    this.restaurantManager = window.restaurantManager;
    this.init();
  }

  async init() {
    await this.loadFeaturedRestaurants();
    this.setupSearch();
    this.setupAnimations();
    this.loadStats();
  }

  async loadFeaturedRestaurants() {
    const container = document.getElementById('featuredRestaurantsContainer');
    if (!container) return;

    // Show loading
    const spinner = DineTimeUtils.showLoading(container);

    try {
      const restaurants = await this.restaurantManager.fetchRestaurants();
      const featured = restaurants.slice(0, 3); // Show first 3 as featured
      
      DineTimeUtils.hideLoading(spinner);
      this.renderRestaurants(featured, container);
    } catch (error) {
      DineTimeUtils.hideLoading(spinner);
      container.innerHTML = '<p class="text-center text-muted">Failed to load restaurants</p>';
    }
  }

  renderRestaurants(restaurants, container) {
    if (restaurants.length === 0) {
      container.innerHTML = '<p class="text-center text-muted">No restaurants found</p>';
      return;
    }

    container.innerHTML = '';
    
    restaurants.forEach((restaurant, index) => {
      const card = this.createRestaurantCard(restaurant);
      card.style.animationDelay = `${index * 0.2}s`;
      container.appendChild(card);
    });
  }

  createRestaurantCard(restaurant) {
    const col = document.createElement('div');
    col.className = 'col animate-on-scroll';

    col.innerHTML = `
      <div class="card restaurant-card h-100">
        <img src="${restaurant.image}" alt="${restaurant.name} Restaurant" 
             class="card-img-top" loading="lazy" 
             onerror="this.src='images/placeholder.jpg'">
        <div class="card-body">
          <h5 class="card-title">${restaurant.name}</h5>
          <p class="card-text">${restaurant.description}</p>
          <div class="d-flex justify-content-between align-items-center">
            <span class="badge bg-success">${restaurant.rating.toFixed(1)} ★</span>
            <div class="btn-group">
              <a href="restaurant.html" class="btn btn-outline-primary btn-sm">View Menu</a>
              <a href="bookings.html?restaurant=${encodeURIComponent(restaurant.name)}" 
                 class="btn btn-primary btn-sm">Book Now</a>
            </div>
          </div>
        </div>
      </div>
    `;

    return col;
  }

  setupSearch() {
    const searchForm = document.getElementById('searchForm');
    const searchInput = document.getElementById('searchInput');
    
    if (!searchForm || !searchInput) return;

    const handleSearch = DineTimeUtils.debounce(async () => {
      const searchTerm = searchInput.value.trim();
      if (searchTerm.length < 2) {
        this.loadFeaturedRestaurants();
        return;
      }

      const restaurants = await this.restaurantManager.fetchRestaurants();
      const filtered = this.restaurantManager.searchRestaurants(searchTerm);
      const container = document.getElementById('featuredRestaurantsContainer');
      this.renderRestaurants(filtered, container);
    }, 300);

    searchInput.addEventListener('input', handleSearch);
    searchForm.addEventListener('submit', (e) => {
      e.preventDefault();
      handleSearch();
    });
  }

  setupAnimations() {
    // Counter animation for stats
    const counters = document.querySelectorAll('.stat-number');
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          this.animateCounter(entry.target);
        }
      });
    });

    counters.forEach(counter => observer.observe(counter));
  }

  animateCounter(element) {
    const target = parseInt(element.getAttribute('data-target'));
    const duration = 2000;
    const step = target / (duration / 16);
    let current = 0;

    const timer = setInterval(() => {
      current += step;
      if (current >= target) {
        current = target;
        clearInterval(timer);
      }
      element.textContent = Math.floor(current).toLocaleString();
    }, 16);
  }

  loadStats() {
    // Simulate loading statistics
    const stats = [
      { element: document.querySelector('[data-target="500"]'), target: 500 },
      { element: document.querySelector('[data-target="50"]'), target: 50 },
      { element: document.querySelector('[data-target="10000"]'), target: 10000 },
      { element: document.querySelector('[data-target="99"]'), target: 99 }
    ];

    stats.forEach(stat => {
      if (stat.element) {
        stat.element.setAttribute('data-target', stat.target);
      }
    });
  }
}

// Initialize home page when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  new HomePage();
});
"""

# Write the JavaScript files
with open('js/utils.js', 'w', encoding='utf-8') as f:
    f.write(utils_js)

with open('js/home.js', 'w', encoding='utf-8') as f:
    f.write(home_js)

print("✅ Created js/utils.js")
print("✅ Created js/home.js")