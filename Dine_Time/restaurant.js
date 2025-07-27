// Restaurant Page JavaScript
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
