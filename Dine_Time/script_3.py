# Create specific CSS files for different pages
# Home page specific styles
home_css = """/* Home Page Specific Styles */
.hero-section {
  background: linear-gradient(
      rgba(0, 0, 0, 0.7),
      rgba(0, 0, 0, 0.7)
    ),
    url("images/hero-bg.jpg");
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  color: var(--light-color);
  padding: 8rem 0;
  margin-bottom: 4rem;
  position: relative;
  overflow: hidden;
  min-height: 70vh;
}

.hero-section::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    135deg,
    rgba(139, 95, 38, 0.3) 0%,
    rgba(212, 167, 98, 0.3) 100%
  );
  z-index: 1;
}

.hero-content {
  position: relative;
  z-index: 2;
  animation: fadeIn 1s ease forwards;
}

.hero-section h1 {
  font-size: 3.5rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

.hero-section .lead {
  font-size: 1.25rem;
  margin-bottom: 2rem;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
}

.features-section {
  padding: 5rem 0;
  background-color: var(--light-color);
}

.feature-card {
  text-align: center;
  padding: 2rem;
  border-radius: 10px;
  transition: transform 0.3s ease;
  height: 100%;
}

.feature-card:hover {
  transform: translateY(-5px);
}

.feature-icon {
  font-size: 3rem;
  color: var(--primary-color);
  margin-bottom: 1rem;
}

.stats-section {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--accent-color) 100%);
  color: var(--light-color);
  padding: 4rem 0;
}

.stat-item {
  text-align: center;
  padding: 1rem;
}

.stat-number {
  font-size: 3rem;
  font-weight: 700;
  display: block;
}

.stat-label {
  font-size: 1.1rem;
  opacity: 0.9;
}

@media (max-width: 768px) {
  .hero-section {
    padding: 5rem 0;
  }
  
  .hero-section h1 {
    font-size: 2.5rem;
  }
  
  .features-section {
    padding: 3rem 0;
  }
}
"""

# Booking page specific styles
booking_css = """/* Booking Page Specific Styles */
.booking-container {
  min-height: 80vh;
  display: flex;
  align-items: center;
  padding: 2rem 0;
}

.booking-form {
  max-width: 700px;
  margin: 0 auto;
  padding: 3rem;
  background: var(--light-color);
  border-radius: 20px;
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
  position: relative;
}

.booking-form::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, var(--primary-color), var(--accent-color));
  border-radius: 20px 20px 0 0;
}

.form-section {
  margin-bottom: 2.5rem;
  padding: 2rem;
  background: rgba(139, 95, 38, 0.05);
  border-radius: 15px;
  border: 1px solid rgba(139, 95, 38, 0.1);
}

.form-section h3 {
  color: var(--primary-color);
  margin-bottom: 1.5rem;
  font-weight: 600;
  display: flex;
  align-items: center;
}

.form-section h3::before {
  content: '';
  width: 4px;
  height: 20px;
  background-color: var(--primary-color);
  margin-right: 10px;
  border-radius: 2px;
}

.floating-label {
  position: relative;
  margin-bottom: 1.5rem;
}

.floating-label input,
.floating-label select,
.floating-label textarea {
  width: 100%;
  padding: 1rem;
  border: 2px solid #e0e0e0;
  border-radius: 10px;
  font-size: 1rem;
  transition: all 0.3s ease;
  background-color: transparent;
}

.floating-label input:focus,
.floating-label select:focus,
.floating-label textarea:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(139, 95, 38, 0.1);
}

.booking-summary {
  background: linear-gradient(135deg, var(--primary-color), var(--accent-color));
  color: var(--light-color);
  padding: 2rem;
  border-radius: 15px;
  margin-top: 2rem;
}

.booking-summary h4 {
  margin-bottom: 1rem;
  font-weight: 600;
}

.summary-item {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.5rem;
  padding: 0.5rem 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
}

.progress-indicator {
  display: flex;
  justify-content: center;
  margin-bottom: 2rem;
}

.progress-step {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background-color: #e0e0e0;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 10px;
  font-weight: bold;
  transition: all 0.3s ease;
}

.progress-step.active {
  background-color: var(--primary-color);
  color: var(--light-color);
}

.progress-step.completed {
  background-color: var(--success-color);
  color: var(--light-color);
}

@media (max-width: 768px) {
  .booking-form {
    padding: 2rem;
    margin: 1rem;
  }
  
  .form-section {
    padding: 1.5rem;
  }
}
"""

# Restaurant page specific styles
restaurant_css = """/* Restaurant Page Specific Styles */
.page-header {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--accent-color) 100%);
  color: var(--light-color);
  padding: 4rem 0;
  text-align: center;
  margin-bottom: 3rem;
}

.filter-bar {
  background: var(--light-color);
  padding: 1.5rem;
  border-radius: 15px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  margin-bottom: 3rem;
}

.filter-controls {
  display: flex;
  gap: 1rem;
  align-items: center;
  flex-wrap: wrap;
}

.filter-select {
  min-width: 150px;
}

.sort-controls {
  display: flex;
  gap: 0.5rem;
  margin-left: auto;
}

.sort-btn {
  background: none;
  border: 1px solid var(--primary-color);
  color: var(--primary-color);
  padding: 0.5rem 1rem;
  border-radius: 5px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.sort-btn:hover,
.sort-btn.active {
  background-color: var(--primary-color);
  color: var(--light-color);
}

.restaurant-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-bottom: 3rem;
}

.restaurant-card {
  position: relative;
  overflow: hidden;
}

.restaurant-card .card-img-overlay {
  background: linear-gradient(transparent, rgba(0, 0, 0, 0.7));
  opacity: 0;
  transition: opacity 0.3s ease;
}

.restaurant-card:hover .card-img-overlay {
  opacity: 1;
}

.rating-badge {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: rgba(255, 255, 255, 0.9);
  padding: 0.5rem;
  border-radius: 20px;
  font-weight: bold;
  color: var(--primary-color);
}

.quick-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid #eee;
}

.cuisine-tag {
  background-color: var(--secondary-color);
  color: var(--primary-color);
  padding: 0.25rem 0.75rem;
  border-radius: 15px;
  font-size: 0.875rem;
  font-weight: 500;
}

.loading-skeleton {
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200% 100%;
  animation: loading 1.5s infinite;
}

@keyframes loading {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

@media (max-width: 768px) {
  .filter-controls {
    flex-direction: column;
    align-items: stretch;
  }
  
  .sort-controls {
    margin-left: 0;
    justify-content: center;
  }
  
  .restaurant-grid {
    grid-template-columns: 1fr;
  }
}
"""

# Write the CSS files
with open('css/home.css', 'w', encoding='utf-8') as f:
    f.write(home_css)

with open('css/booking.css', 'w', encoding='utf-8') as f:
    f.write(booking_css)

with open('css/restaurant.css', 'w', encoding='utf-8') as f:
    f.write(restaurant_css)

print("✅ Created css/home.css")
print("✅ Created css/booking.css") 
print("✅ Created css/restaurant.css")