// Portfolio Interactive Script
console.log("Portfolio website loaded successfully!");

document.addEventListener("DOMContentLoaded", function() {
    initializePortfolio();
});

function initializePortfolio() {
    addSkillsAnimation();
    addContactFormValidation();
    addScrollToTopButton();
    addTypingEffect();
    addSkillsProgressBars();
}

// Add typing effect to the header
function addTypingEffect() {
    const header = document.querySelector('.header h1');
    const originalText = header.textContent;
    header.textContent = '';
    
    let index = 0;
    function typeWriter() {
        if (index < originalText.length) {
            header.textContent += originalText.charAt(index);
            index++;
            setTimeout(typeWriter, 100);
        }
    }
    typeWriter();
}

// Add hover effects and animations to skills
function addSkillsAnimation() {
    const skillItems = document.querySelectorAll('.skills li');
    
    skillItems.forEach(item => {
        item.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.05)';
            this.style.backgroundColor = '#e0f7fa';
            this.style.transition = 'all 0.3s ease';
        });
        
        item.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
            this.style.backgroundColor = '#f4f4f4';
        });
    });
}

// Add progress bars to skills
function addSkillsProgressBars() {
    const skills = [
        { name: 'HTML', level: 80 },
        { name: 'CSS', level: 80 },
        { name: 'JavaScript', level: 50 },
        { name: 'Python', level: 80 },
        { name: 'MySQL', level: 50 },
        { name: 'C++', level: 50 },
        { name: 'Git', level: 50 },
        { name: 'GitHub', level: 50 },
        { name: 'Azure', level: 50 },
        { name: 'Oracle', level: 50 }
    ];
    
    const skillsList = document.querySelector('.skills ul');
    skillsList.innerHTML = '';
    
    skills.forEach(skill => {
        const li = document.createElement('li');
        li.innerHTML = `
            <div class="skill-item">
                <span class="skill-name">${skill.name}</span>
                <div class="progress-bar">
                    <div class="progress-fill" data-level="${skill.level}"></div>
                </div>
                <span class="skill-level">${skill.level}%</span>
            </div>
        `;
        skillsList.appendChild(li);
    });
    
    // Animate progress bars
    setTimeout(() => {
        const progressFills = document.querySelectorAll('.progress-fill');
        progressFills.forEach(fill => {
            const level = fill.getAttribute('data-level');
            fill.style.width = level + '%';
        });
    }, 500);
}

// Simplify contact section - remove form, keep only links
function addContactFormValidation() {
    // Add interactive effects to contact links
    addContactAnimations();
}

// Add interactive animations to contact links
function addContactAnimations() {
    const contactItems = document.querySelectorAll('.contact-item');
    
    contactItems.forEach((item, index) => {
        // Add staggered entrance animation
        setTimeout(() => {
            item.style.opacity = '0';
            item.style.transform = 'translateY(50px)';
            item.style.transition = 'all 0.6s ease';
            
            setTimeout(() => {
                item.style.opacity = '1';
                item.style.transform = 'translateY(0)';
            }, 100);
        }, index * 200);
        
        // Add click effect
        item.addEventListener('click', function(e) {
            // Create ripple effect
            const ripple = document.createElement('div');
            ripple.className = 'ripple';
            
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = (e.clientX - rect.left - size / 2) + 'px';
            ripple.style.top = (e.clientY - rect.top - size / 2) + 'px';
            
            this.appendChild(ripple);
            
            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
        
        // Add hover sound effect (visual feedback)
        item.addEventListener('mouseenter', function() {
            const icon = this.querySelector('.contact-icon');
            icon.style.transform = 'scale(1.2) rotate(10deg)';
            icon.style.transition = 'transform 0.3s ease';
        });
        
        item.addEventListener('mouseleave', function() {
            const icon = this.querySelector('.contact-icon');
            icon.style.transform = 'scale(1) rotate(0deg)';
        });
    });
    
    // Add scroll-triggered animation
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animation = 'slideInUp 0.6s ease forwards';
            }
        });
    });
    
    contactItems.forEach(item => {
        observer.observe(item);
    });
}

// Add scroll to top button
function addScrollToTopButton() {
    const scrollBtn = document.createElement('button');
    scrollBtn.className = 'scroll-to-top';
    scrollBtn.innerHTML = '↑';
    scrollBtn.title = 'Scroll to Top';
    document.body.appendChild(scrollBtn);
    
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            scrollBtn.style.display = 'block';
        } else {
            scrollBtn.style.display = 'none';
        }
    });
    
    scrollBtn.addEventListener('click', function() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
}