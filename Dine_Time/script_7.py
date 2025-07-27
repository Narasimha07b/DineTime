# Enhanced restaurant.html
restaurant_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="description" content="DINETIME - Browse and book top restaurants" />
    <title>DINETIME - Restaurants</title>
    
    <!-- Preload Bootstrap CSS -->
    <link
      rel="preload"
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/css/bootstrap.min.css"
      as="style"
      onload="this.onload=null;this.rel='stylesheet'"
    />
    <noscript>
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/css/bootstrap.min.css"
      />
    </noscript>
    
    <!-- Custom CSS -->
    <link rel="stylesheet" href="css/style.css" />
    <link rel="stylesheet" href="css/restaurant.css" />
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light sticky-top">
        <div class="container">
            <a class="navbar-brand fw-bold" href="indexx.html">DINETIME</a>
            <button
              class="navbar-toggler"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#navbarNav"
              aria-controls="navbarNav"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="indexx.html">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link active" href="restaurant.html">RESTAURANTS</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="bookings.html">BOOKINGS</a>
                    </li>
                </ul>
                <form class="d-flex" id="searchForm" role="search" aria-label="Search restaurants">
                    <input
                      class="form-control me-2"
                      type="search"
                      placeholder="Search restaurants..."
                      aria-label="Search restaurants"
                      id="searchInput"
                      autocomplete="off"
                    />
                    <button class="btn btn-primary" type="submit">Search</button>
                </form>
            </div>
        </div>
    </nav>

    <!-- Page Header -->
    <section class="page-header">
        <div class="container">
            <h1 class="display-4 fw-bold">Our Restaurants</h1>
            <p class="lead">Explore our curated collection of exceptional dining venues</p>
        </div>
    </section>

    <!-- Main Content -->
    <main class="container my-5">
        <!-- Filter and Sort Bar -->
        <div class="filter-bar">
            <div class="filter-controls">
                <div class="d-flex flex-wrap gap-3 align-items-center">
                    <div>
                        <label for="ratingFilter" class="form-label mb-1">Minimum Rating:</label>
                        <select id="ratingFilter" class="form-select filter-select">
                            <option value="">All Ratings</option>
                            <option value="4.5">4.5+ Stars</option>
                            <option value="4.0">4.0+ Stars</option>
                            <option value="3.5">3.5+ Stars</option>
                        </select>
                    </div>
                    
                    <div class="ms-auto">
                        <label class="form-label mb-1">Sort by:</label>
                        <div class="sort-controls">
                            <button class="sort-btn active" data-sort="name">Name</button>
                            <button class="sort-btn" data-sort="rating">Rating</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Restaurant Grid -->
        <div class="restaurant-grid" id="restaurantContainer">
            <!-- Restaurant cards will be dynamically inserted here -->
        </div>

        <!-- Loading State -->
        <div id="loadingState" class="text-center d-none">
            <div class="loading-spinner mx-auto mb-3"></div>
            <p class="text-muted">Loading restaurants...</p>
        </div>

        <!-- Empty State -->
        <div id="emptyState" class="text-center d-none">
            <div class="mb-4">
                <span style="font-size: 4rem; opacity: 0.3;">🍽️</span>
            </div>
            <h3>No restaurants found</h3>
            <p class="text-muted">Try adjusting your search or filter criteria</p>
            <button class="btn btn-primary" onclick="location.reload()">Reset Filters</button>
        </div>
    </main>

    <!-- Restaurant Details Modal -->
    <div class="modal fade" id="restaurantModal" tabindex="-1" aria-labelledby="restaurantModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-lg">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="restaurantModalLabel">Restaurant Details</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body" id="restaurantModalBody">
                    <!-- Restaurant details will be inserted here -->
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <a href="#" class="btn btn-primary" id="modalBookBtn">Book Now</a>
                </div>
            </div>
        </div>
    </div>

    <!-- Footer -->
    <footer class="bg-dark text-light py-4 mt-5">
        <div class="container">
            <div class="row">
                <div class="col-md-6">
                    <h5>DINETIME</h5>
                    <p class="mb-0">Your premier destination for exceptional dining experiences.</p>
                </div>
                <div class="col-md-6">
                    <div class="row">
                        <div class="col-6">
                            <h6>Quick Links</h6>
                            <ul class="list-unstyled">
                                <li><a href="indexx.html" class="text-light">Home</a></li>
                                <li><a href="restaurant.html" class="text-light">Restaurants</a></li>
                                <li><a href="bookings.html" class="text-light">Bookings</a></li>
                            </ul>
                        </div>
                        <div class="col-6">
                            <h6>Contact</h6>
                            <p class="mb-0 small">support@dinetime.com<br>(555) 123-4567</p>
                        </div>
                    </div>
                </div>
            </div>
            <hr>
            <div class="text-center">
                <p class="mb-0">&copy; 2025 DINETIME. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <!-- Toast Container -->
    <div id="toastContainer" class="position-fixed top-0 end-0 p-3" style="z-index: 9999;"></div>

    <!-- Scripts -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/js/bootstrap.bundle.min.js"></script>
    <script src="js/utils.js"></script>
    <script src="js/restaurant.js"></script>
</body>
</html>
"""

# Write the enhanced restaurant HTML file
with open('restaurant.html', 'w', encoding='utf-8') as f:
    f.write(restaurant_html)

print("✅ Created enhanced restaurant.html")