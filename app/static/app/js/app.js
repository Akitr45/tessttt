const stars = document.querySelectorAll('.stars input[type="radio"]');
stars.forEach(star => {
    star.addEventListener('change', e => {
        let selectedValue = e.target.value;
        console.log(`Selected value: ${selectedValue}`);
    });
});
