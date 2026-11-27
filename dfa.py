# src/dfa.py

class DFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states                      # set(str)
        self.alphabet = alphabet                  # set(str)
        self.transitions = transitions            # dict: {state: {symbol: next_state}}
        self.start_state = start_state            # str
        self.accept_states = accept_states        # set(str)

    def process_string(self, input_string):
        """
        Menyimulasikan jalannya DFA terhadap input string.
        """
        current_state = self.start_state
        
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False, f"Simbol '{symbol}' tidak ada dalam alfabet."
            
            if current_state in self.transitions and symbol in self.transitions[current_state]:
                current_state = self.transitions[current_state][symbol]
            else:
                return False, "Trap State / Transisi tidak terdefinisi."

        is_accepted = current_state in self.accept_states
        return is_accepted, current_state