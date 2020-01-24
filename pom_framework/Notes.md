root directory:
* conftest.py
1. pages
    * modules for each page
        * class inherit BasePage
            * locators
            * actions - for example: loginpage.py -> dologin(username, password) 
                        homepage.py -> click_signin_button()
    * basepage
        * class BasePage
            * selenium interaction
                * click
                * type
                * waitforelement
2. reports 
    * ctreport-selenium
    * pytest report
    * junit xml report
3. testdata
    * xlsx files
    * read_excel_data.py
4. tests
    * pytest files
        * addnewpayee.py
        * search.py