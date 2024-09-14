let deleteForm;
        const modal = document.getElementById('deleteModal');
        const confirmYes = document.getElementById('confirmYes');
        const confirmNo = document.getElementById('confirmNo');
    
        function confirmDelete(button) {
            deleteForm = button.closest('form');
            modal.style.display = 'flex';
        }
    
        confirmYes.onclick = function() {
            deleteForm.submit();
        }
    
        confirmNo.onclick = function() {
            modal.style.display = 'none';
        }
    
        window.onclick = function(event) {
            if (event.target === modal) {
                modal.style.display = 'none';
            }
        }