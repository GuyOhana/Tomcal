       // Shows one page and hides the other two
       function showPage2(page) {
        // Hide all of the divs inside book_containers:
        document.querySelectorAll('div.book_containers div').forEach(div => {
            div.style.display = 'none';
        });

        // Show the div provided in the argument
        document.querySelector(`.${page}`).style.display = 'block';

    }


       // switches buttons style
        function changeStyle(pressed_button) {
            // Select all buttons in container3
            document.querySelectorAll('div#container3 button').forEach(button => {
                if(button == pressed_button)
                {
                    pressed_button.style.color = '#20232a';
                    pressed_button.style.backgroundColor = '#61dafb';        
                }
                else{
                    button.style.color = 'white';
                    button.style.backgroundColor = '#282c34';
        
                }
                })
        }
    // Wait for page to loaded:
    document.addEventListener('DOMContentLoaded', function() {
    
        // Select all buttons in container3
        document.querySelectorAll('div#container3 button').forEach(button => {
    
            // When a button is clicked, switch to that page
            button.onclick = function() {
                showPage2(this.dataset.page);
                changeStyle(button)
            }
        })
    })
    