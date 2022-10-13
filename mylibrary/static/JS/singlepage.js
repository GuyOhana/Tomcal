
       // Shows one page and hides the other two
       function showPage(page) {
        // Hide all of the divs:
        document.querySelector(`#container2`).style.display = 'none';
        document.querySelector(`#container3`).style.display = 'none';
        // Hide books' third bar
        document.querySelectorAll('div.book_containers div').forEach(div => {
                div.style.display = 'none';
        });
        //return book buttons styles to noraml
        document.querySelectorAll('div#container3 button').forEach(button => {
            {
                button.style.color = 'black';
                button.style.backgroundColor = 'white';
            }
            })
        

        // Show the div provided in the argument
        document.querySelector(`#${page}`).style.display = 'block';

        //switches buttons style
        if(`#${page}` == '#container2')
        {
            document.querySelector(`#button1`).style.color = ' white';
            document.querySelector(`#button1`).style.backgroundColor = '#003459';
            document.querySelector(`#button2`).style.color = ' black';
            document.querySelector(`#button2`).style.backgroundColor = 'white';
        }
        if(`#${page}` == '#container3')
        {
            document.querySelector(`#button2`).style.color = ' white';
            document.querySelector(`#button2`).style.backgroundColor = '#003459';
            document.querySelector(`#button1`).style.color = ' black';
            document.querySelector(`#button1`).style.backgroundColor = 'white';
        }
        }

    // Wait for page to loaded:
    document.addEventListener('DOMContentLoaded', function() {
        // Select all buttons in container1
        document.querySelectorAll('div#container1 button').forEach(button => {
            document.getElementById('button1').click();
            // When a button is clicked, switch to that page
            button.onclick = function() {
                showPage(this.dataset.page);
                
            }
        })
    })
    