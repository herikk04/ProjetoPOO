// EXECUTA NA PÁGINA DE ADICIONAR QUADRAS
if (window.location.pathname === '/add_courts') {
    const ownedCourtsNum = localStorage.getItem('ownedCourtsNum');
    const checkboxContainer = document.getElementById('hour-selector');
    const checkboxes = checkboxContainer.querySelectorAll('div input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
    checkbox.addEventListener('change', function () {
        this.value = this.checked ? '1' : '0';
    });
        checkbox.value = '0'; 
    });
    

    if(ownedCourtsNum==0) {
        var newURL = window.location.origin + '/user_created';
        window.location.replace(newURL); // redireciona para página de usuário criado com sucesso
    }

    const form = document.querySelector('#form-add-courts');
    form.addEventListener('submit', function onSubmitForm(e) {
        let n = ownedCourtsNum;
        e.preventDefault();
        localStorage.setItem('ownedCourtsNum', n-1);
        if (n > 0) {
            let n = localStorage.getItem('ownedCourtsNum');
            console.log(n)
            const params = new URLSearchParams(window.location.search);
            const userID = params.get('userID');
            const userType = params.get('userType');
            var newURL = window.location.pathname + '?userID=' + userID + '&userType=' + userType;
            const formData = {};
            const formFields = form.elements;
            for (let i = 0; i < formFields.length; i++) {
                let field = formFields[i];
                if (field.name) {
                    formData[field.name] = field.value;
                }
            }
            console.log(formData)
            let jsonData = JSON.stringify(formData);
            var responseClone;
            fetch(newURL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                  },
                body: jsonData
            })
            .then(function(response) {
                responseClone = response.clone();
                return response.json();
            })
            .then(jsonData => {
                console.log('Success:', jsonData);
                window.location.reload();
            },
            function (rejectionReason) { 
                console.log('Error parsing JSON from response:', rejectionReason, responseClone);
                responseClone.text()
                .then(function (bodyText) {
                    console.log('Received the following instead of valid JSON:', bodyText);
                });
            })
            .catch(error => console.error('Error:', error));
        }
    });
}

// EXECUTA NA PÁGINA DE ADICIONAR LOCATÁRIO
if (window.location.pathname === '/add_user_locator') {
    window.onload = function() {
        localStorage.clear();
    }
    const formElement = document.querySelector("#form-add-user-locator");

    formElement.addEventListener('submit', (e) => {
        const ownedCourtsNum = document.getElementById('ownedCourtsNum').value;
        console.log(ownedCourtsNum)
        localStorage.setItem('ownedCourtsNum', ownedCourtsNum);
    })
}


var divs = document.querySelectorAll("div.clickable-div");
divs.forEach(function(div) {
    div.addEventListener("click", function(event) {
        if (event.target.type !== 'checkbox' && event.target.tagName !== 'LABEL') {
            var checkbox = div.querySelector('input[type="checkbox"]');
            if (checkbox) {
                checkbox.checked = !checkbox.checked;
                checkbox.dispatchEvent(new Event('change'));
            }
        }
    });
});

if (window.location.pathname === '/dashboard') {
    function showLocatorCourts(courtsData) {
        // Get the court container
        var courtContainer = document.getElementById('courtContainer');

        // Clear existing content in the container
        courtContainer.innerHTML = '';

        // Iterate through the courts data and create divs
        courtsData.forEach(function(court, index) {
            // Create a new div element
            var courtDiv = document.createElement('div');
            courtDiv.classList.add('court-div');
            courtDiv.setAttribute('data-locator', court.locatorId);
            courtDiv.setAttribute('data-court', court.courtId);

            // Set content for the div (you can customize this based on your data)
            courtDiv.innerHTML = `
                <h2>Court ${index + 1} for Locator ${court.locatorId}</h2>
                <p>This is the content for Locator ${court.locatorId}'s Court ${court.courtId}.</p>
            `;

            // Append the new div to the container
            courtContainer.appendChild(courtDiv);
        });

        // Show the dynamically created court divs
        var courtDivs = document.getElementsByClassName('court-div');
        for (var i = 0; i < courtDivs.length; i++) {
            courtDivs[i].style.display = 'block';
        }
    }

    // Example data for the courts of a specific locator (replace with actual data received from server)
    var locatorCourtsData = [
        { locatorId: 'locator1', courtId: 'court1' },
        { locatorId: 'locator1', courtId: 'court2' },
        // Add more court data as needed
    ];

    // Show divs for the received locator's courts data
    showLocatorCourts(locatorCourtsData);
}