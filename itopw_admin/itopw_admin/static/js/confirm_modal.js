/* Project specific Javascript goes here. */
function confirmChange(fncSuccess) {
  $(document).delegate('.confirm_change', 'click', function (e) {
    swal.fire({
      title: 'Are you sure?',
      text: 'Make this change',
      type: 'warning',
      showCancelButton: true,
      confirmButtonText: 'Yes, change it!',
      cancelButtonText: 'No, cancel!',
      reverseButtons: true
    }).then(function (result) {
      if (result.value) {
        // this call back exec some ajax
        fncSuccess(e, function () {
          fireSucess()
        });
      } else if (result.dismiss === 'cancel') {
        fireCancel();
      }
    });
  });
}

function fireSucess() {
  // this callback fire an notification
  swal.fire(
    'Changed!',
    "Your action has been taken",
    'success'
  );
}

function fireCancel() {
  swal.fire(
    'Cancelled',
    'You canceled this action',
    'error'
  )
}
