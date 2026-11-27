# src/converter.py
from src.dfa import DFA

class NFAtoDFAConverter:
    @staticmethod
    def convert(nfa):
        
        dfa_start = frozenset([nfa.start_state])
        unprocessed_states = [dfa_start]
        
        dfa_states_map = {dfa_start: f"Q_{','.join(sorted(dfa_start))}"}
        dfa_transitions = {}
        dfa_accept_states = set()
        
        visited = set()

        while unprocessed_states:
            current_set = unprocessed_states.pop(0)
            visited.add(current_set)
            
            current_dfa_name = dfa_states_map[current_set]
            dfa_transitions[current_dfa_name] = {}

            if any(state in nfa.accept_states for state in current_set):
                dfa_accept_states.add(current_dfa_name)

            for symbol in nfa.alphabet:
                next_set = set()
                for state in current_set:
                    if state in nfa.transitions and symbol in nfa.transitions[state]:
                        next_set.update(nfa.transitions[state][symbol])
                
                frozen_next = frozenset(next_set)
                
                if not frozen_next:
                    continue 

                if frozen_next not in dfa_states_map:
                    dfa_states_map[frozen_next] = f"Q_{','.join(sorted(frozen_next))}"
                
                next_dfa_name = dfa_states_map[frozen_next]
                dfa_transitions[current_dfa_name][symbol] = next_dfa_name

                if frozen_next not in visited and frozen_next not in unprocessed_states:
                    unprocessed_states.append(frozen_next)

        all_dfa_states = set(dfa_states_map.values())
        start_dfa_name = dfa_states_map[dfa_start]

        return DFA(
            states=all_dfa_states,
            alphabet=nfa.alphabet,
            transitions=dfa_transitions,
            start_state=start_dfa_name,
            accept_states=dfa_accept_states
        )