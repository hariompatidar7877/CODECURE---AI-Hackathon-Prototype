class PolicyAgent:

    def suggest(self, risk):

        if risk == "High Risk":
            return [
                "Increase testing",
                "Limit public mobility",
                "Accelerate vaccination"
            ]

        elif risk == "Medium Risk":
            return [
                "Monitor hotspots",
                "Encourage masking"
            ]

        else:
            return [
                "Maintain surveillance"
            ]
