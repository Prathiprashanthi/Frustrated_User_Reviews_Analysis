function verifyOTP() {
    const otpEntered = document.getElementById('otp').value;
    // Simulate OTP verification
    const otpGenerated = /* You would get the generated OTP from the backend */;
    
    if (otpEntered === otpGenerated) {
        alert('OTP verification successful! You can now proceed with registration.');
        // Here, you can redirect the user to the next page or handle the registration process
    } else {
        alert('OTP verification failed. Please try again.');
    }
}