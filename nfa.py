# src/nfa.py

class NFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states                      # set(str)
        self.alphabet = alphabet                  # set(str)
        self.transitions = transitions            # dict: {state: {symbol: set(next_states)}}
        self.start_state = start_state            # str
        self.accept_states = accept_states        # set(str)

    def process_string(self, input_string):
        """
        Menyimulasikan jalannya NFA terhadap input string.
        Mendukung transisi bercabang (multiple next-states).
        """
        current_states = {self.start_state}
        
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False, f"Simbol '{symbol}' tidak ada dalam alfabet."
            
            next_states = set()
            for state in current_states:
                if state in self.transitions and symbol in self.transitions[state]:
                    next_states.update(self.transitions[state][symbol])
            current_states = next_states

        # Diterima jika setidaknya satu current_state berada di accept_states
        is_accepted = bool(current_states & self.accept_states)
        return is_accepted, current_states