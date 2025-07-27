# Create the enhanced project structure with separated HTML, CSS, and JS files
import os
import json

# Create directories if they don't exist
os.makedirs('css', exist_ok=True)
os.makedirs('js', exist_ok=True)
os.makedirs('images', exist_ok=True)

# First, let's create the main CSS file that will be shared across all pages
main_css = """/* DINETIME - Main CSS File */
:root {
  --primary-color: #8b5f26;
  --secondary-color: #f8f1e5;
  --accent-color: #d4a762;
  --dark-color: #1a1a1a;
  --light-color: #ffffff;
  --success-color: #28a745;
  --warning-color: #ffc107;
  --danger-color: #dc3545;
  --info-color: #17a2b8;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: "Montserrat", sans-serif;
  background-color: var(--secondary-color);
  color: var(--dark-color);
  line-height: 1.6;
}

/* Navigation Styles */
.navbar {
  background-color: var(--light-color) !important;
  box-shadow: 0 2px 30px rgba(0, 0, 0, 0.1);
  padding: 1rem 0;
  transition: all 0.3s ease;
}

.navbar-brand {
  font-weight: 700;
  font-size: 1.5rem;
  color: var(--primary-color) !important;
  transition: color 0.3s ease;
}

.navbar-brand:hover {
  color: var(--accent-color) !important;
}

.nav-link {
  font-weight: 500;
  margin: 0 0.5rem;
  color: var(--dark-color) !important;
  transition: all 0.3s ease;
  position: relative;
}

.nav-link:hover {
  color: var(--primary-color) !important;
}

.nav-link.active {
  color: var(--primary-color) !important;
  font-weight: 600;
}

.nav-link.active::after {
  content: '';
  position: absolute;
  bottom: -5px;
  left: 50%;
  transform: translateX(-50%);
  width: 20px;
  height: 2px;
  background-color: var(--primary-color);
}

/* Button Styles */
.btn-primary {
  background-color: var(--primary-color);
  border-color: var(--primary-color);
  font-weight: 500;
  padding: 0.5rem 1.5rem;
  border-radius: 50px;
  transition: all 0.3s ease;
}

.btn-primary:hover {
  background-color: var(--accent-color);
  border-color: var(--accent-color);
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(139, 95, 38, 0.3);
}

.btn-primary:focus {
  box-shadow: 0 0 0 0.25rem rgba(139, 95, 38, 0.25);
}

.btn-lg {
  padding: 0.75rem 2rem;
  font-size: 1.1rem;
}

/* Card Styles */
.restaurant-card {
  transition: all 0.3s ease;
  margin-bottom: 2rem;
  border: none;
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  background: var(--light-color);
}

.restaurant-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
}

.card-img-top {
  height: 220px;
  object-fit: cover;
  width: 100%;
  transition: transform 0.3s ease;
}

.restaurant-card:hover .card-img-top {
  transform: scale(1.05);
}

.card-body {
  padding: 1.5rem;
}

.card-title {
  font-weight: 600;
  color: var(--primary-color);
  margin-bottom: 0.75rem;
}

.card-text {
  color: #666;
  font-size: 0.95rem;
}

/* Form Styles */
.form-control,
.form-select {
  padding: 0.75rem 1rem;
  border-radius: 8px;
  border: 1px solid #ddd;
  transition: all 0.3s ease;
  font-size: 1rem;
}

.form-control:focus,
.form-select:focus {
  border-color: var(--primary-color);
  box-shadow: 0 0 0 0.25rem rgba(139, 95, 38, 0.25);
}

.form-label {
  font-weight: 500;
  color: var(--dark-color);
  margin-bottom: 0.5rem;
}

.invalid-feedback {
  display: block;
  color: var(--danger-color);
  font-size: 0.875rem;
  margin-top: 0.25rem;
}

/* Footer */
footer {
  background-color: var(--dark-color);
  color: var(--light-color);
  padding: 3rem 0;
  margin-top: 5rem;
}

/* Animations */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slideInLeft {
  from {
    opacity: 0;
    transform: translateX(-30px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes slideInRight {
  from {
    opacity: 0;
    transform: translateX(30px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.animate-fade {
  animation: fadeIn 0.8s ease forwards;
}

.animate-slide-left {
  animation: slideInLeft 0.8s ease forwards;
}

.animate-slide-right {
  animation: slideInRight 0.8s ease forwards;
}

/* Utility Classes */
.fade-out {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.fade-in {
  opacity: 1;
  transform: translateY(0);
  transition: opacity 0.3s ease, transform 0.3s ease;
}

/* Loading spinner */
.loading-spinner {
  display: inline-block;
  width: 20px;
  height: 20px;
  border: 3px solid rgba(139, 95, 38, 0.3);
  border-radius: 50%;
  border-top-color: var(--primary-color);
  animation: spin 1s ease-in-out infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Responsive Styles */
@media (max-width: 768px) {
  .navbar-brand {
    font-size: 1.25rem;
  }
  
  .hero-section {
    padding: 5rem 0 !important;
  }
  
  .card-body {
    padding: 1rem;
  }
  
  .btn-lg {
    padding: 0.5rem 1.5rem;
    font-size: 1rem;
  }
}

@media (max-width: 576px) {
  .container {
    padding: 0 15px;
  }
  
  .restaurant-card {
    margin-bottom: 1.5rem;
  }
}
"""

# Write main CSS file
with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(main_css)

print("✅ Created css/style.css")