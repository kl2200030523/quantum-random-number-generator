document.getElementById('generateBtn').addEventListener('click', async function() {
    try {
        const response = await fetch('random_numbers.json');
        const data = await response.json();

        // Get the keys of the data object
        const keys = Object.keys(data);

        // Select a random key
        const randomKey = keys[Math.floor(Math.random() * keys.length)];

        // Get the corresponding random number
        const randomValue = data[randomKey];

        // Display the random number
        document.getElementById('randomNumber').innerText = `Random Number: ${randomValue}`;
    } catch (error) {
        console.error('Error:', error);
    }
});
