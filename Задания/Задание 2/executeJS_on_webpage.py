
# Задание 2

# 3. Open webpage
# 4. Open review form
# 5. Fill the review form
# 6. Press submit

"""
    elements from the page

pre_review_form
onclick="show_addreviewform()"
class="link dashlink"

input id = 'reviewname'
maxlength="40"
value="dsjvujvhndhndhndhndhndhndhndhndhndhndhndhndhndio"

input id="reviewemail"
maxlength="60"

textarea id="reviewtext"

input id="reviewtsid"
maxlength="100"

label for="rvtype_1" +
label for="rvtype_3" 0
label for="rvtype_2" -

input id="review_button"
"""
"""
    JavaScript Example
    
  document.getElementById('reviewname').value = payload['reviewname']
  document.getElementById('reviewemail').value = payload['reviewemail']
  document.getElementById('reviewtext').value = payload['reviewtext']
  document.getElementById('reviewtsid').value = payload['reviewtsid']
  getElementById('rvtype_1').checked = payload['rvtype_1']
  document.getElementById('review_button').click()
  """

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def post_review(payload, url):
    """
    Post review to https://www.bestchange.ru
    Need to have chromedriver installed
    :param payload: dict with review
    :return: void
    """
    options = Options()
    #options.headless = True # Don't open browser window
    options.add_argument('--disable-gpu')  # Last I checked this was necessary.

    CHROMEDRIVER_PATH = 'C:\\Users\\khini\\Downloads\\chromedriver_win32(1)\\chromedriver.exe'

    driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)
    driver.get(url)
    # Run JS
    driver.find_element_by_id('ar_bullet').click()
    driver.find_element_by_id('reviewname').send_keys(payload['reviewname'])
    driver.find_element_by_id('reviewemail').send_keys(payload['reviewemail'])
    driver.find_element_by_id('reviewtext').send_keys( payload['reviewtext'])
    driver.find_element_by_id('reviewtsid').send_keys(payload['reviewtsid'])
    if payload['rvtype_1'] == 1: # 1 - положительный
        driver.find_element_by_id('rvtype_1').checked = 'true'
    elif payload['rvtype_1'] == 2: # 2 -нейтральный
        driver.find_element_by_id('rvtype_3').checked = 'true'
    elif payload['rvtype_1'] == 3: # 3 - отрецательный
        driver.find_element_by_id('rvtype_2').checked = 'true'
    time.sleep(1)
    driver.find_element_by_id('review_button').click()
    time.sleep(5)
    driver.close()
    driver.quit()
    print("Review has been posted")
    """
    # Check last review
    import time
    time.sleep(2.4)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')
    div = soup.find('input', {"id" : "reviewemail"})
    text = div.string
    print(text)
    div = soup.find('div', {"class" : 'review_text'})
    text = div.string
    print(text)
    """
