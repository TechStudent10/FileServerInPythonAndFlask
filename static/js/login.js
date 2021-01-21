function login(username, password) {
	fetch("/api/user/signup?username=" + username + "&password=" + password, {
		method: 'GET',
	});
	console.log("Login.");
	console.log(username);
	console.log(password);
}