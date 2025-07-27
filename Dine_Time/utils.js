// DINETIME - Utility Functions
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
