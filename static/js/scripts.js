//GLobal regular expressions used to validate forms
const lettersOnlyRegex = new RegExp("^.[A-z ]*$");
const lettersNumbersParenthesesAndSpacesOnlyRegex = new RegExp("^.[A-z0-9() ]*$");
const lettersNumbersParenthesesSpacesAndCertainCharactersOnlyRegex = new RegExp("^.[A-z0-9()?,\n\r ]*$")

$(document).ready(function() {

    // Allow the instrument filters to be applied when option is adjusted
    $("#sortByForm").on("change", function() {
        this.submit();
    })
    $("#filterByForm").on("change", function() {
        this.submit();
    })
    
     // Prevent the instrument form from being submitted unless it is validated
     $("#registrationForm").on("submit", function(event) {
        // Get the form values
        let fName = $("input[name = 'f_name']");
        let lName = $("input[name = 'l_name']");
        let email = $("input[name = 'email']");
        let password = $("input[name = 'password']");
        let passwordConfirm = $("input[name = 'password_confirm']");
        
        //If passwords provided match and the form only contains accepted characters, submit it
        if((password.val() == passwordConfirm.val()) && (lettersOnlyRegex.test(fName.val()) && lettersOnlyRegex.test(lName.val()))) {
            return true;
        } else {
            event.preventDefault();
            // If the passwords dont match, display an error message
			if (password.val() != passwordConfirm.val()) {
				displayFormError(password, "Passwords don't match");
				//Remove the error message if both passwords match after user changes values
			} else {
				removeFormError(password);
			}
			//If there is an error for user's submitted first name, display an error
			if (!lettersOnlyRegex.test(fName.val())) {
				displayFormError(fName, "Only letters can be accepted as inputs");
				//Remove the error message if first name is valid 
			} else {
				removeFormError(fName);
			}
			//If there is an error for user's submitted last name, display an error
			if (!lettersOnlyRegex.test(lName.val())) {
				displayFormError(lName, "Only letters can be accepted as inputs");
				//Remove the error message if last name is valid 
			} else {
				removeFormError(lName);
			}
        }
     });
     
     
    // Prevent the instrument form from being submitted unless it is validated
    $("#productForm").on("submit", function(event) {
        // Get the form values
        let brand = $("input[name = 'brand']");
        let model = $("input[name = 'model']");
        let type = $("input[name = 'type']");
        let description = $("textarea");

        // Make sure the values entered are only valid characters
        if (lettersNumbersParenthesesSpacesAndCertainCharactersOnlyRegex.test(model.val())) {
            return true;
        }
        else {
            //If values aren't matching values contained in regular expression stop the form from being submitted
            event.preventDefault();
            let errorMsg = "Invalid characters detected\nLetters, numbers, spaces, dots, commas, parenthesis and qustion marks only accepted";
            if (!lettersNumbersParenthesesSpacesAndCertainCharactersOnlyRegex.test(model.val())) {
                displayFormError(model, errorMsg);
            }
            else {
                //Remove the error message if model name is valid 
                removeFormError(model)
            }
            if (!lettersNumbersParenthesesSpacesAndCertainCharactersOnlyRegex.test(description.val())) {
                displayFormError(description, errorMsg);
            }
            else {
                removeFormError(description)
            }
        }
    });

    // Prevent the supplier form from being submitted unless it is validated
    $("#supplierForm").on("submit", function(event) {
        let supplier = $("input[name = 'supplier']");
        // Make sure the values entered are only valid characters
        if(lettersNumbersParenthesesAndSpacesOnlyRegex.test(supplier.val())) {
            return true;
        } else {
           // If the value entered can't be validated display an error message
           event.preventDefault();
           displayFormError(supplier, "Invalid characters detected\nLetters, numbers, spaces and parenthesis only accepted");
        }
    });
    
    // Prevent the instrument type form from being submitted unless it is validated
    $("#instrumentTypeForm").on("submit", function(event) {
        let type = $("input[name = 'instrument_type']");
        // Make sure the values entered are only valid characters
        if(lettersNumbersParenthesesAndSpacesOnlyRegex.test(type.val())) {
            return true;
        } else {
           // If the value entered can't be validated display an error message
           event.preventDefault();
           displayFormError(type, "Invalid characters detected\nLetters, numbers, spaces and parenthesis only accepted");
        }
    });
    // Stripe JS
    let stripe = Stripe("pk_test_51K2dXzFGKYruxG0TBF3X93vMIo9hSKNBw74xfkocV5Atz6v1pyrhwpgfwUqXPWkPXKjERIXYdVrjBxcoaD6axKP400D1FM11fS");
    let elements = stripe.elements();
    if(document.querySelector("#cardNumber")) {
        var cardNumber = elements.create("cardNumber");
	    cardNumber.mount("#cardNumber");
	    cardNumber.on('change', ({ error }) => {
		    if (error) {
			    validInput = false;
			    displayFormError($("#cardNumber"), error.message);
    		} else {
    			validInput = true;
    			removeFormError($("#cardNumber"));
    		}
    	});
        let cardExpiry = elements.create("cardExpiry");
    	cardExpiry.mount('#cardExpiry');
    	cardExpiry.on('change', ({ error }) => {
    		if (error) {
    			validInput = false;
    			displayFormError($("#cardExpiry"), error.message);
    		} else {
    			validInput = true;
    			removeFormError($("#cardExpiry"));
    		}
    	});
    	let cardCvc = elements.create('cardCvc');
    	cardCvc.mount('#cardCvc');
    }
	$("#paymentForm").on("submit", function (event) {
	    event.preventDefault();
	    loading(true);
	    // Fetches a payment intent and captures the client secret
        var response = fetch('create_payment_intent').then(function(response) {
            return response.json();
        }).then(function(responseJson) {
            var clientSecret = responseJson.client_secret;
            responseJson.payment_method = cardNumber;
            payWithCard(stripe, cardNumber, clientSecret);
            event.currentTarget.submit();
        });
    });
})

function payWithCard(stripe, cardNumber, secretKey) {
	//Call the loading method to show signal payment has started 
	loading(true);
	let displayError = document.getElementById("card-errors")
	stripe.confirmCardPayment(secretKey, {
		payment_method: {
			card: cardNumber,
			billing_details: {
				name: $("#cardHolderName").val()
			}
		}
	}).then(function(result) {
		if (result.error) {
		    let response = fetch('/payment_fail');
		    return response;
			displayFormError($("#cardExpiry"), result.error.message);
 		}
	})
}
function validQuantityCheck(element, maxAmount) {
     let inputElement = element.querySelector("input[name = 'quantity']");
     // Prevent the user from using a negative number
     if(inputElement.value < 0 ) {
         inputElement.value = 0
     } 
     // Prevent the user from entering a value above the maximum stock amount
     if(inputElement.value > maxAmount) {
        inputElement.value = maxAmount;
     }
}
    
    // //Prevent the user from adding a value higher than  ap products stock value to their cart
    // $(".addToCartForm").on("change", function(event) {
    //     let input = $("input[name = 'quantity']");
    //     //If the selected amount is higher than the stock amount, prevent the form from being submit
    //     if(input.val() > input.attr('max')){

    //     } else {
    //         console.log("Thats okay");
    //     }
    //     console.log(input.attr('max'));
    //     alert("Test");
    // })

//The method below is called when payment is successful
// function paymentComplete(){
// 	//create a form
// 	let form = document.createElement("form");
// 	let formAction = "paymentSuccess"
// 	form.setAttribute("action", formAction);
// 	form.setAttribute("method", "get");
// 	document.body.appendChild(form);
// 	form.submit();
// }

//Method to show user their payment is processing
function loading(isLoading) {
  if (isLoading) {
    // Disable the button and show a spinner
    document.querySelector("button").disabled = true;
    document.querySelector("#spinner").classList.remove("hidden");
    //document.querySelector("#button-text").classList.add("hidden");
  } else {
    document.querySelector("button").disabled = false;
    document.querySelector("#spinner").classList.add("hidden");
    document.querySelector("#button-text").classList.remove("hidden");
  }
}

function displayFormError(element, errorMessage) {
    //Avoid error duplication to check if error message is already present
    if (element.parent().children().last()[0].localName != "p") {
        let formError = document.createElement("p");
        formError.style.color = "red";
        formError.innerHTML = errorMessage;
        element.parent().append(formError);
    }
}

function removeFormError(element) {
    if (element.parent().children().last()[0].localName == "p") {
        element.parent().children('p').remove();
    }
}



// // Method to display a button to add data to the database from the InstrumentForm
// function checkInstrumentDetailsExist(element, modelType) {
//     var addListener = function addListener() {}
//     if(element.querySelector("#addButton")) {
//         element.querySelector("#addButton").removeEventListener("click", test)
//     }
//     // Retrieve the value entered into the select input
//     let enteredValue = element.querySelector(".bs-searchbox input").value;
//     // Event listener to ensure button created by function is removed when the user removes focus on select element
//     element.addEventListener('focus', function() {
//         //Timeout used to ensure button still exists if user tries to click it
//         setTimeout(
//                 function() {
//                     if (element.querySelector("#addButton")) {
//                         element.querySelector("#addButton").remove();
//                     }
//                 }, 5000
//             );
//     });

//     if (enteredValue != "") {
//         let matchAmount = 0;;
//         // Convert the value entered to lower case
//         let lowerCaseEnteredValue = enteredValue.toLowerCase();
//         // Traverse all values contained within the select element and check if there is a match for the enetered value
//         let selectElement = element.querySelector("Select");
//         for (let i = 0; i<selectElement.length; i ++) {
//             // Convert the value in the select element to lower case, if there is a match to the value entered, adjust match to true
//             let existingOption = selectElement.options[i].innerHTML.toLowerCase();
//             if (existingOption.startsWith(lowerCaseEnteredValue)) {
//                 matchAmount++;
//                 break;
//             }
//         }
//         // If the match variable is false create a button which can add the value entered to the bd
//         if(!matchAmount > 0 ) {
//             //if the button doesn't exist create it, if it does exist already adjust it
//             if(!document.getElementById("addButton")) {
//                 let addButton = document.createElement("button");
//                 addButton.setAttribute('id', 'addButton');
//                 addButton.setAttribute('class', 'btn btn-primary btn-sm');
//                 addButton.innerHTML = `Add ${enteredValue}`;
//                 addButton.setAttribute('type', 'button');
//                 element.append(addButton);
//             } else {
//                 let addButton = document.getElementById("addButton");
//                 addButton.innerHTML = `Add ${enteredValue}`;
//                 addButton.addEventListener("click", addListener {
//                   addNewInstrumentDetail("test", "here");  
//                 })


//             }
//         }
//     }
// }

// function removeListener() {
//     alert("Test");
// }

// // // Method to add a instrument detail to the database if it isn't already listed
// function addNewInstrumentDetail(modelType, enteredValue) {
//     // Ensure the details are validated before being submitted to the database
//         console.log("clicked")
// }
