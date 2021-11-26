//GLobal regular expressions used to validate forms
const lettersNumbersParenthesesAndSpacesOnlyRegex = new RegExp("^.[A-z0-9() ]*$");
const lettersNumbersParenthesesSpacesAndCertainCharactersOnlyRegex = new RegExp("^.[A-z0-9()?, \n]*$")

$(document).ready(function() {
    // Prevent the instrument form from being submitted unless it is validated
    $("#productForm").on("submit", function(event) {
        // Get the form values
        let brand = $("input[name = 'brand']");
        let model = $("input[name = 'model']");
        let type = $("input[name = 'type']");
        let description = $("textarea");

        // Make sure the values entered are only valid characters
        if (lettersNumbersParenthesesSpacesAndCertainCharactersOnlyRegex.test(model.val()) && lettersNumbersParenthesesSpacesAndCertainCharactersOnlyRegex.test(description.val())) {
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
})


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
