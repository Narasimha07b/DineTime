// Home Page JavaScript
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
