# Add toast notification styles and other enhancements to the main CSS file
additional_css = """
/* Toast Notification Styles */
.toast-notification {
  position: fixed;
  top: 20px;
  right: 20px;
  max-width: 350px;
  background: var(--light-color);
  border-radius: 10px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  transform: translateX(400px);
  opacity: 0;
  transition: all 0.3s ease;
  z-index: 9999;
}

.toast-notification.show {
  transform: translateX(0);
  opacity: 1;
}

.toast-content {
  display: flex;
  align-items: center;
  padding: 1rem;
}

.toast-message {
  flex-grow: 1;
  color: var(--dark-color);
  font-size: 0.95rem;
}

.toast-close {
  background: none;
  border: none;
  font-size: 1.5rem;
  color: #999;
  cursor: pointer;
  margin-left: 1rem;
  transition: color 0.3s ease;
}

.toast-close:hover {
  color: var(--dark-color);
}

.toast-success {
  border-left: 4px solid var(--success-color);
}

.toast-error {
  border-left: 4px solid var(--danger-color);
}

.toast-info {
  border-left: 4px solid var(--info-color);
}

.toast-warning {
  border-left: 4px solid var(--warning-color);
}

/* Enhanced Button Animations */
.btn-primary .btn-spinner {
  margin-left: 0.5rem;
}

.btn:disabled {
  cursor: not-allowed;
  opacity: 0.6;
}

/* Modal Enhancements */
.modal-content {
  border-radius: 15px;
  border: none;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
}

.modal-header {
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
}

.modal-footer {
  border-top: 1px solid rgba(0, 0, 0, 0.1);
}

/* Enhanced Form Validation */
.form-control.is-valid {
  border-color: var(--success-color);
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3e%3cpath fill='%2328a745' d='m2.3 6.73.94-.94 1.06 1.06-1.88 1.88L.7 7.01l.94-.94L2.3 6.73z'/%3e%3c/svg%3e");
  background-repeat: no-repeat;
  background-position: right calc(0.375em + 0.1875rem) center;
  background-size: calc(0.75em + 0.375rem) calc(0.75em + 0.375rem);
}

.form-control.is-invalid {
  border-color: var(--danger-color);
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3e%3cpath fill='%23dc3545' d='M7.5 1.5L6.5.5 4 3 1.5.5.5 1.5 3 4 .5 6.5 1.5 7.5 4 5 6.5 7.5 7.5 6.5 5 4 7.5 1.5z'/%3e%3c/svg%3e");
  background-repeat: no-repeat;
  background-position: right calc(0.375em + 0.1875rem) center;
  background-size: calc(0.75em + 0.375rem) calc(0.75em + 0.375rem);
}

/* Scroll to Top Button */
.scroll-to-top {
  position: fixed;
  bottom: 30px;
  right: 30px;
  width: 50px;
  height: 50px;
  background-color: var(--primary-color);
  color: var(--light-color);
  border: none;
  border-radius: 50%;
  cursor: pointer;
  display: none;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  transition: all 0.3s ease;
  z-index: 1000;
}

.scroll-to-top:hover {
  background-color: var(--accent-color);
  transform: translateY(-3px);
  box-shadow: 0 5px 15px rgba(139, 95, 38, 0.3);
}

.scroll-to-top.show {
  display: flex;
}

/* Improved Responsive Design */
@media (max-width: 992px) {
  .hero-section h1 {
    font-size: 2.5rem !important;
  }
  
  .display-4 {
    font-size: 2rem !important;
  }
  
  .display-5 {
    font-size: 1.75rem !important;
  }
}

@media (max-width: 576px) {
  .toast-notification {
    right: 10px;
    left: 10px;
    max-width: none;
    transform: translateY(-100px);
  }
  
  .toast-notification.show {
    transform: translateY(0);
  }
  
  .scroll-to-top {
    bottom: 20px;
    right: 20px;
    width: 45px;
    height: 45px;
  }
}

/* Print Styles */
@media print {
  .navbar,
  .footer,
  .btn,
  .toast-notification,
  .scroll-to-top {
    display: none !important;
  }
  
  .modal-content {
    box-shadow: none !important;
    border: 1px solid #ddd !important;
  }
  
  body {
    background-color: white !important;
    color: black !important;
  }
}
"""

# Append the additional CSS to the main style.css file
with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write('\n\n' + additional_css)

print("✅ Enhanced css/style.css with additional features")