## Create automated scripts to test ecommerce mobile app place order as a guest feature

App file is located
at [Download APK File From Here](https://brainstationo365-my.sharepoint.com/:u:/g/personal/borhan_brainstation-23_com/EUeMsjFUXFpJrYMh74TuHFQBYDXrvCTF-OUoNsmfPoUyaA?e=qpo3eq)

### Please write automation script to automate the below scenarios

 **Scenario: 01** Customer add products in his shopping cart  
>  ***Given:*** Mike on home page after opening nopCart mobile app  
   ***When:*** Mike click "electronics" from our categories list from home page  
   ***And:*** Mike click to "Nokia Lumia 1020" product details page  
   ***Then:*** Mike select size "Large" from product details page  
   ***And:*** Mike click plus button to increase Qty by "2"  
   ***Then:*** Mike click add to cart button to add the product in his cart  


**Scenario: 02** Customer successfully place order as a guest user
 > ***Given:*** Mike go to shopping cart by clicking top cart icon  
   ***When:*** Mike click checkout button from shopping cart page  
   ***And:*** Mike select checkout as guest from shopping cart page  
   ***Then:*** Mike input all the details in checkout billing details page and click continue  
   ***And:*** Mike select "Next Day Air" as shipping method and click continue  
   ***And:*** Mike select "Check/Money Order" as payment method and click continue  
   ***And:*** Mike click next button on payment information page  
   ***Then:*** Mike click confirm button to place the order  
   ***And:*** Verify order place successfully with popup message "Your order has been successfully processed!"


### Additional functionalities, that may be covered:

1. The more, the better. Only if it makes sense :smirk: Use your imagination and write some additional tests if you feel you can cover other important functionalities.
2. Please include any third party test reporting tools(Ex. Extent Report, Allure report) in your automation project.
3. Please use Excel/csv file as external test data provider and your automation script have the ability to read and write data from excel/csv for above scenario(Ex. Billing/shipping address and all the quoted value in scenario step can be read from excel as test data)


### Using automation framework is a must:

You can feel free to choose the framework, that suits you best, along with the Java or other programming language as you preferred.

### Record a video of tests execution:

Record a video to show how your tests are interacting with the mobile app(In Emulator). Attach the video as part of your solution.


### Task Submission:
You can put the code publicly (in GitHub or similar code control systems) if you want, but please do not use BS-23 or Brainstation-23
name in title, description or the code itself. This helps others to find the libraries that are really related to our services and/or are developed and maintained by our team.  

Send it in your favourite format (link to versioned code, code in zip file etc.) to us.