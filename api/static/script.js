document.getElementById('runScriptButton').addEventListener('click', function () {
    fetch('/run_script', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ arg1: 'value1', arg2: 'value2' })
    });
});
