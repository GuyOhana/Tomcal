       // Shows one page and hides the other two
       function showPage(page) {

        // Hide all of the divs:
        document.querySelectorAll('div').forEach(div => {
            div.style.display = 'none';
        });
        // Show the div provided in the argument
        document.querySelector(`#container1`).style.display = 'block';
    
    
        // Show the div provided in the argument
        document.querySelector(`#${page}`).style.display = 'block';
        }

    // Wait for page to loaded:
    document.addEventListener('DOMContentLoaded', function() {
    
        // Select all buttons in container1
        document.querySelectorAll('div#container1 button').forEach(button => {
    
            // When a button is clicked, switch to that page
            button.onclick = function() {
                showPage(this.dataset.page);
            }
        })
    })
    