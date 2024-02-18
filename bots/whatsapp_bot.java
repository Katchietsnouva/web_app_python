// Share WhatsApp Web without Scanning QR code using Python
// Read
// Courses
// Practice
// Prerequisite: Selenium, Browser Automation Using Selenium

// Failed to build pyautogui pymsgbox
// ERROR: Could not build wheels for pyautogui, pymsgbox, which is required to install pyproject.toml-based projects

// PS C:\Desktop\django_tut\web_app_python>

function getResultFromRequest(request) {
    return new Promise((resolve, reject) => {
        request.onsuccess = function (event) {
            resolve(request.result);
        };
    });
}
  
async function getDB() {
    var request = window.indexedDB.open("wawc");
    return await getResultFromRequest(request);
}
  
async function readAllKeyValuePairs() {
    var db = await getDB();
    var objectStore = db.transaction("user").objectStore("user");
    var request = objectStore.getAll();
       return await getResultFromRequest(request);
}
  
session = await readAllKeyValuePairs();
console.log(session);

// Now we get those key-value pairs as text by running the following line of code. 
JSON.stringify(session);



// Now let’s copy that text to a file to save a session and clear both localStorage and IndexedDB to log out. Now we can run the following code to inject a session by assigning the value of the session string we just copied to a file to variable SESSION_STRING. Then refresh the page and we will log in again without scanning the QR code. 
function getResultFromRequest(request) {
	return new Promise((resolve, reject) => {
		request.onsuccess = function(event) {
			resolve(request.result);
		};
	})
}

async function getDB() {
	var request = window.indexedDB.open("wawc");
	return await getResultFromRequest(request);
}

async function injectSession(SESSION_STRING) {
	var session = JSON.parse(SESSION_STRING);
	var db = await getDB();
	var objectStore = db.transaction("user", "readwrite").objectStore("user");
	for(var keyValue of session) {
		var request = objectStore.put(keyValue);
		await getResultFromRequest(request);
	}
}

var SESSION_STRING = "";
await injectSession(SESSION_STRING);
