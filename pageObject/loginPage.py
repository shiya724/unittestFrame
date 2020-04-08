from pageObject.basePage import BasePage, log


class LoginPage(BasePage):
    def login(self):
        log.logger.info("登录")
