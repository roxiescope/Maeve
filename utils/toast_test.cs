using Microsoft.Toolkit.Uwp.Notifications; // Notifications library

// Construct the content and schedule the toast!
new ToastContentBuilder()
    .AddArgument("action", "viewItemsDueToday")
    .AddText("ASTR 170B1")
    .AddText("You have 3 items due today!")
    .Schedule(DateTime.Now.AddSeconds(5));