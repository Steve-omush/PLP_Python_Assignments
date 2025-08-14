class Smartphone:
    def __init__(self, brand, model, price_usd):
        self.brand = brand
        self.model = model
        self.price_usd = price_usd

    def specs(self):
        return f"{self.brand}, {self.model}, costing ${self.price_usd}"

    @staticmethod
    def call(number):
        return f"Dialing {number}"

# Subclass: Android Phone
class AndroidPhone(Smartphone):
    def __init__(self, model, price_usd, android_version):
        super().__init__('AndroidOS Manufacturer', model, price_usd)
        self.android_version = android_version

    def specs(self):
        base = super().specs()
        return f"{base}, Android {self.android_version}"

    def install_play_store(self, app_name):
        return f"Installing {app_name} from Google Play Store."

# Subclass: iPhone
class IPhone(Smartphone):
    def __init__(self, model, price_usd, ios_version):
        super().__init__('Apple', model, price_usd)
        self.ios_version = ios_version

    def specs(self):
        base = super().specs()
        return f"{base}, iOS {self.ios_version}"

    def install_app_store(self, app_name):
        return f"Installing {app_name} from App Store."

# Polymorphism demo
phones = [
    AndroidPhone('Galaxy S22', 799, '13'),
    IPhone('iPhone 15', 999, '18'),
]

for phone in phones:
    print(phone.specs())
    print(phone.call("123-456-7890"))
    if isinstance(phone, AndroidPhone):
        print(phone.install_play_store("Maps"))
    else:
        print(phone.install_app_store("Safari"))
    print("---")
