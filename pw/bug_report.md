# Bug Report Summary



## Name of the Bug: Fixed 2.00 Point Offset Error in All Reward Redemptions (UI ONLY)

### What is happening?

The rewards application has a visual bug where the advertised point cost
on the reward cards is consistently inflated by a fixed offset of 2.00
points within the user interface.

**CLARIFICATION NOTES:** The backend logic calculates the price
correctly. The deduction applied to the user's points is the correct
amount (e.g., 2.75 points). The bug is only in the presentation of the
price to the user.

-   Observed UI Price: Item cost (X) is displayed as (X + 2.00pts).
    E.g., The "Wand of Presentation" (1.50pts) is displayed as 3.50pts.
-   Actual Backend Charge: The charge is X (1.50pts).

**Result:** Users are visually misled about the true cost of the
rewards, leading to confusion and preventing users from accurately
predicting their point totals.

### How do you reproduce it?

#### Case A: Visual Discrepancy and calculation

1.  Setup: View the main rewards page.
2.  Action: Locate any reward item and compare the advertised price in
    the database (or what you know the true price to be) with the price
    displayed on the card.
3.  Observation: All rewards are visually displayed as their true cost
    plus 2.00 points.
    -   Example: "Tote Bag of Holding" (True Cost 2.75pts) is displayed
        as 4.75pts.
    -   Example: "Wand of Presentation" (True Cost 1.50pts) is displayed
        as 3.50pts.

#### Case B: Frontend Blocking Due to Inflated Price

1.  Setup: Click one of the "Earn bonus points" buttons (e.g., the +5
    button) to set the user's 'Points Remaining' to 5.00 points.
2.  Action: Locate a high-cost reward item (e.g., "Scroll of Infinite
    WiFi" at 3.75pts).
    -   The user has 5.00 points, which is enough for the actual cost
        (3.75pts).
    -   The UI displays the cost as 5.75pts (3.75 + 2.00).
3.  Observation: When attempting to redeem, the UI blocks the action
    because it incorrectly checks if 5.00 points is greater than the
    inflated price of 5.75 points.

### Thoughts on Severity

The severity is High (2): while the system's core transactional integrity is safe
(back-end/data), the integrity of the UI is completely compromised. Incorrect
pricing data creates a poor user experience, leads to distrust, and
renders the advertised prices meaningless.

------------------------------------------------------------------------

## Name of the Bug: Point Metric Misspelling

### What is happening?

The display headers for the user's points are misspelled. They currently
read "Ponts Redeemed" and "Ponts Remaining."

### How do you reproduce it?

1 - View the homes page, the spelling is incorrect in the two main point
summary boxes.

### Thoughts on Severity

The severity is Minor (4): This is a cosmetic error that degrades the perceived quality and professionalism of the application.

------------------------------------------------------------------------

## Name of the Bug: Broken "About" Navigation Link (404 Error)

### What is happening?

The "About" link in the main navigation bar results in a "Page not
found" (404) error.
The link attempts to navigate to:
`http://localhost:3000/about//test`

### How do you reproduce it?

1 - Simply click the "About" link in the main header navigation.

**Result:** Crashed application with error:
Page not found (404)

### Thoughts on Severity

The severity is Critical (1): Navigation is a core component of any application. The application should not crash under any circunstance.

------------------------------------------------------------------------

## Name of the Bug: Success Action Styled as an Error (UI/UX)

### What is happening?

The notification banner is styled incorrectly with an error color scheme
when a successful action occurs.

### How do you reproduce it?

1.  Click the "forfeit all points" link.
2.  Observe the red error-style banner appear even though the operation
    succeeded.

### Thoughts on Severity

The severity is Medium (3): Misuse of color creates confusion in the user experience and distrust in the application's feedback.

------------------------------------------------------------------------

## Name of the Bug: Reward Claim Crash due to Missing Points Check

### What is happening?

The UI allows reward claiming even when 'Points Remaining' is zero,
causing a crash.

### How do you reproduce it?

1.  Click the "Redeem this Reward" button for all prices.
2.  Claim enough points to redeem the rewards.
3.  Click "Forfeit all points".
4.  Click "Claim my rewards" even tho 0 points available.
5.  The website crashes.

**Result:** Crashed application with error:
SuspiciousOperation django.core.exceptions.SuspiciousOperation: Invalid request; Exceeded available points 

### Thoughts on Severity

The severity is Critical (1): This bug leads to a full application crash triggered by a normal user action, indicating a missing safeguard that affects core functionality. The application should not crush any under circuntances.

------------------------------------------------------------------------

## Name of the Bug: Duplicate/Conflicting "Forgot Password" Links

### What is happening?

Two different "Forgot your password?" links appear on the Sign In page.

### How do you reproduce it?

1.  Navigate to the Sign In page.
2.  Observe the two duplicate links.

### Thoughts on Severity

The severity is Minor (4): The issue is purely cosmetic and doesn’t block any functionality.

------------------------------------------------------------------------

## Name of the Bug: Added Email Address Not Displayed in UI After Successful API Call

### What is happening?

The backend successfully return a 200 response the new email, but the UI does not
display it.

### How do you reproduce it?

1.  Navigate to the E-mail Addresses page.
2.  Add a new email.
3.  Backend returns 200 success.
4.  UI does not show the newly added email.

### Thoughts on Severity

The severity is Medium (3): In this case the backend succeeds but the user can't see the result, causing confusion and blocking the intended workflow. The action fails from the user’s perspective even though it succeeds on the server. 

------------------------------------------------------------------------

## Name of the Bug: Misleading UI Success on already registered Email Sign-up

### What is happening?

The UI suggests success when signing up with an already registered
email, but the backend correctly blocks it.

### How do you reproduce it?

1.  Navigate to Sign Up.
2.  Enter an already-registered email.
3.  Observe redirect to "Verify your email".
4.  Check email for different notification email.

### Thoughts on Severity

The severity is High (2): The UI gives a false sense of success for an action that actually failed. While data integrity is safe thanks to backend validation, the misleading user experience can significantly disrupt the sign-up.

------------------------------------------------------------------------

## Name of the Bug: [webpack-dev-server] Proxy Connection Reset (ECONNRESET) Error to Backend Service

### What is happening?

The frontend dev server cannot maintain connection to the backend,
preventing communication.

### How do you reproduce it?

1.  Start the app in dev environment.
2.  Attempt a page requiring backend communication(e.g: /login).
3.  Do login request.
4.  Logs show ECONNRESET error.

### Thoughts on Severity

The severity is High (2): The frontend can't reliably communicate with the backend, blocking core functionality and halting development or testing.
#### NOTES: If this is happening in production I will consider this as Critical (1)

------------------------------------------------------------------------

## Name of the Bug: Insecure Direct Object Reference - Unauthorized User Profile Viewing

### What is happening?

Users can view profile pages of other users by changing the URL ID in profile.

### How do you reproduce it?

1.  Log in as any user, for example user 4 (someone4@holistiplan.com).
2.  Go to "My profile" and edit URL from `/users/4/` to another user ID like `/users/5/`.
3.  The profile page for the new user ID loads without any error or requirement for authentication/authorization.


### Thoughts on Severity

The severity is Critical (1): Major security flaw - Insecure Direct Object Reference.

------------------------------------------------------------------------


## Name of the Bug: Missing State Handling / Race Condition Leading to App Crash on Rapid/multiple Clicks.

### What is happening?

The application experiences a critical crash when the user rapidly clicks links due to a race condition and missing state management.

### How do you reproduce it?

1.  Navigate to the rewards page
2.  Rapidly click the "Earn bonus points: +15" link many times in quick succession.
3.  The application will crash and display the full red "Uncaught runtime errors" screen.

### Thoughts on Severity

The severity is Critical (1): This is a severe stability bug. This can lead to multiple problems within the app leading to crashes/terrible user experience.
