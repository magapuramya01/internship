class Hospital:
    def treatment(self):
        print("General treatment")


class SpecializedHospital(Hospital):
    def treatment(self):
        print("Specialized treatment")


SpecializedHospital().treatment()