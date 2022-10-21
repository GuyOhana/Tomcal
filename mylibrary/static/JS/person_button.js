       // Shows one page and hides the other two
       function showPage3(page) {
        // Hide all of the divs inside person_containers:
        document.querySelectorAll('div.person_containers div').forEach(div => {
            div.style.display = 'none';
        });

        // Show the div provided in the argument
        document.querySelector(`.${page}`).style.display = 'block';

    }
       // switches buttons style
        function changeStyle2(pressed_button) {
            // Select all buttons in button_person
            document.querySelectorAll('div.classsome button').forEach(button => {
                if(button == pressed_button)
                {
                    button.style.color = 'black';
                    button.style.backgroundColor = '#61dafb';        
                }
                else{
                    button.style.color = 'white';
                    button.style.backgroundColor = '#282c34';        
                }
                })
        }
    // Wait for page to loaded:
    document.addEventListener('DOMContentLoaded', function() {
    
        // Select all buttons in button_person
        document.querySelectorAll('div.classsome button').forEach(button => {
    
            // When a button is clicked, switch to that page
            button.onclick = function() {
                showPage3(this.dataset.page);
                changeStyle2(button)
            }
        })
    })
    