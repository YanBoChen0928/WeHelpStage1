// JavaScript code to fetch data and update HTML content
fetch('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1')
    .then(response => response.json()) // Parse the JSON response
    .then(data => {
        // Store the fetched data in the jsonData variable
        const jsonData = data;

        // Select SBcontainer element
        const SBcontainer = document.getElementById('SBcontainer');

        // Iterate over the data and insert each item into SBcontainer
        jsonData.data.results.slice(0, 3).forEach((spot, index) => {
            const SB = document.createElement('div');
            SB.classList.add('SB', 'item' + (index + 1));

            const img = document.createElement('img');
            img.src = spot.filelist.split('https:')[1]; // Use the image URL from the fetched data
            img.alt = 'Spot Image';

            const text = document.createElement('div');
            text.classList.add('text');
            text.textContent = spot.stitle; // Use the title from the fetched data

            SB.appendChild(img);
            SB.appendChild(text);

            SBcontainer.appendChild(SB);
        });

        // Similarly, handle BBcontainer
        const BBcontainer = document.getElementById('BBcontainer');

        jsonData.data.results.slice(3, 13).forEach((spot, index) => {
            const BB = document.createElement('div');
            BB.classList.add('BB', 'item' + (index + 1));

            const img = document.createElement('img');
            img.src = spot.filelist.split('https:')[1];
            img.alt = 'Spot Image';

            const overlayText = document.createElement('div');
            overlayText.classList.add('overlayText');
            overlayText.textContent = spot.stitle;

            const overlayStar = document.createElement('div');
            overlayStar.classList.add('overlayStar');
            const starText = document.createTextNode('\u2605'); // 使用 HTML 實體字符（★）的 Unicode 編碼
            overlayStar.appendChild(starText);
            //不用innerHTML的做法

            BB.appendChild(img);
            BB.appendChild(overlayText);
            BB.appendChild(overlayStar);

            BBcontainer.appendChild(BB);
        });
    })
    .catch(error => console.error('Error fetching data:', error)); // Handle errors
