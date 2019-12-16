class CodeBreaker:
    
    def __init__(self, secret_code):
        print(secret_code)
        self.secret_code = str(secret_code)
    
    @property
    def is_valid(self):
        return self.validate_number(self.secret_code)

    def validate_number(self, number):
        try:
            int(number)
            return len(set(number)) == 4
        except Exception:
            return False
        
    def guess(self, guess_code):
        if self.validate_number(guess_code):

            if self.secret_code == guess_code:
                return f"{guess_code}: Adivinaste!"

            matches, partials = self.find_matches_and_partials(guess_code).values()

            return f"{guess_code}: {matches}M-{partials}PM"

        return False

    def find_matches_and_partials(self, guess_code):
        result = {'matches': 0, 'partials': 0}
        print(self.secret_code)
        for digit_index, digit in enumerate(guess_code):
            if digit == self.secret_code[digit_index]:
                result['matches'] += 1
            elif digit in self.secret_code:
                result['partials'] += 1
        
        return result