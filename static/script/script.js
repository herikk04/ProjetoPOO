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


    if (ownedCourtsNum == 0) {
        var newURL = window.location.origin + '/user_created';
        window.location.replace(newURL); // redireciona para página de usuário criado com sucesso
    }

    const form = document.querySelector('#form-add-courts');
    form.addEventListener('submit', function onSubmitForm(e) {
        let n = ownedCourtsNum;
        e.preventDefault();
        localStorage.setItem('ownedCourtsNum', n - 1);
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
                .then(function (response) {
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
    window.onload = function () {
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
divs.forEach(function (div) {
    div.addEventListener("click", function (event) {
        if (event.target.type !== 'checkbox' && event.target.tagName !== 'LABEL') {
            var checkbox = div.querySelector('input[type="checkbox"]');
            if (checkbox) {
                checkbox.checked = !checkbox.checked;
                checkbox.dispatchEvent(new Event('change'));
            }
        }
    });
});

// EXECUTA NA PÁGINA DASHBOARD
if (window.location.pathname === '/dashboard') {
    function showLocatorCourts(courtsData) {
        var courtContainer = document.getElementById('courtContainer');
        courtContainer.innerHTML = '';

        courtsData.forEach(function (court, index) {
            var courtDiv = document.createElement('div');
            courtDiv.classList.add('court-div');
            courtDiv.setAttribute('data-locator', court.locatorID);
            courtDiv.setAttribute('data-court', court.courtID);

            courtDiv.innerHTML = `
            <div class="court">
                <h2>Quadra ${index + 1}</h2>
                <p>Tipo de quadra: ${court.courtType}</p>
                <p>Localização: ${court.location}</p>
                <p>Preço por hora: R$${court.pricePerHour},00</p>
            </div>
            `;
            courtContainer.appendChild(courtDiv);
        });

        var courtDivs = document.getElementsByClassName('court-div');
        for (var i = 0; i < courtDivs.length; i++) {
            courtDivs[i].style.display = 'block';
        }
    }

    const urlParams = new URLSearchParams(window.location.search);
    const locatorID = urlParams.get('locatorID');
    fetch(window.location.origin + '/request_courts?locatorID=' + locatorID)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            showLocatorCourts(data['courts'])
        }
        )
        .catch(error => console.error(error));

    var userID = new URLSearchParams(window.location.search).get('locatorID');
    var profileButton = document.getElementById('profileButton');
    profileButton.addEventListener('click', function (event) {
        var newURL = window.location.origin + '/user_profile?userID=' + userID + '&userType=Locator';
        window.location.replace(newURL);
    });
}


//EXECUTA NA PÁGINA COURTS
if (window.location.pathname === '/courts') {
    function showAllCourts(courtsData) {
        var courtContainer = document.getElementById('courtContainer');

        courtContainer.innerHTML = '';

        courtsData.forEach(function (court, index) {
            var courtDiv = document.createElement('div');
            courtDiv.classList.add('court-div');
            courtDiv.setAttribute('data-locator', court.locatorID);
            courtDiv.setAttribute('data-court', court.courtID);

            courtDiv.innerHTML = `
            <div class="court">
                <h2>Quadra ${index + 1}</h2>
                <p>Locatário: ${court.locatorName}</p>
                <p>Tipo de quadra: ${court.courtType}</p>
                <p>Localização: ${court.location}</p>
                <p>Preço por hora: R$${court.pricePerHour},00</p>
                <a href="/rent_court?courtID=${court.courtID}&locatorID=${court.locatorID}">
                    <button type="button" class="locate">Alugar</button>
                </a>
            </div>
            `;

            courtContainer.appendChild(courtDiv);
        });

        var courtDivs = document.getElementsByClassName('court-div');
        for (var i = 0; i < courtDivs.length; i++) {
            courtDivs[i].style.display = 'block';
        }
    }

    const urlParams = new URLSearchParams(window.location.search);
    fetch(window.location.origin + '/request_courts')
        .then(response => response.json())
        .then(data => {
            console.log(data);
            showAllCourts(data['courts'])
        }
        )
        .catch(error => console.error(error));

    //Em andamento
    var locateButtons = document.getElementsByClassName('locate');
    for (var i = 0; i < locateButtons.length; i++) {
        locateButtons[i].addEventListener('click', function (event) {
            var locatorID = event.target.parentElement.parentElement.getAttribute('data-locator');
            var courtID = event.target.parentElement.parentElement.getAttribute('data-court');
            var newURL = window.location.origin + '/locate?locatorID=' + locatorID + '&courtID=' + courtID;
            window.location.replace(newURL);
        });
    }

    var userID = new URLSearchParams(window.location.search).get('renterID');
    var profileButton = document.getElementById('profileButton');
    profileButton.addEventListener('click', function (event) {
        var newURL = window.location.origin + '/user_profile?userID=' + userID + '&userType=Renter';
        window.location.replace(newURL);
    });
}

var logOutButton = document.getElementById('logoutButton');
logOutButton.addEventListener('click', function (event) {
    localStorage.clear();
    var newURL = window.location.origin + '/logout';
    window.location.replace(newURL);
});