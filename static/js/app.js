$( document ).ready(function() {
  // Handler for .ready() called.



  $('#clientPriority').keypress(function() {
        var numbers = $(this).val();
        $(this).val(numbers.replace(/\D+/, '0'));
    });

  $('#targetDate').datepicker();
  	$( '#submit' ).click(function() {
		if (!isEmpty('#titleText')){
			alert('Title Field is Empty')
			return false;
		}
		if (!isEmpty('#descriptionText')){
			alert('Description Field is Empty')
			return false;
		}
		if (!$.isNumeric($('#clientPriority').val())){
			alert('Client Priority Field can only be Numeric')
			return false;
		}
		if (!isEmpty('#clientPriority')){
			alert('Client Priority Field is Empty')
			return false;
		}
		
		if (!isEmpty('#targetDate')){

			alert('Target Date Field is Empty')
			return false;
		}
		if (!isEmpty('#targetURL')){

			alert('Target URL Field is Empty')
			return false;
		}



	});
  	
  	
	function isEmpty(selector){
		return $(selector).val()
	}
});