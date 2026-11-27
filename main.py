# main.py
from src.nfa import NFA
from src.converter import NFAtoDFAConverter

def main():
    print("=" * 55)
    print(" PROGRAM SIMULASI FINITE AUTOMATA & KONVERSI NFA KE DFA")
    print("=" * 55)
    
    # 1. Definisi NFA (Contoh: Kasus string berakhiran 'ab')
    # Sesuai rancangan di laporan Bab II & III
    nfa_example = NFA(
        states={'q0', 'q1', 'q2'},
        alphabet={'a', 'b'},
        transitions={
            'q0': {'a': {'q0', 'q1'}, 'b': {'q0'}},
            'q1': {'b': {'q2'}},
            'q2': {}
        },
        start_state='q0',
        accept_states={'q2'}
    )

    print("\n[INFO] NFA berhasil diinisialisasi.")
    print(f"- States      : {nfa_example.states}")
    print(f"- Alfabet     : {nfa_example.alphabet}")
    print(f"- State Awal  : {nfa_example.start_state}")
    print(f"- State Akhir : {nfa_example.accept_states}")

    # 2. Proses Konversi NFA ke DFA (Menggunakan Algoritma Subset Construction oleh Anggota 2)
    print("\n[PROSES] Melakukan konversi NFA ke DFA...")
    dfa_converted = NFAtoDFAConverter.convert(nfa_example)
    print("[INFO] Konversi berhasil! DFA baru telah dibentuk.")
    print(f"- State DFA Hasil Konversi : {dfa_converted.states}")
    print(f"- State Awal DFA           : {dfa_converted.start_state}")
    print(f"- State Akhir DFA          : {dfa_converted.accept_states}")
    print(f"- Tabel Transisi DFA       :")
    for state, trans in dfa_converted.transitions.items():
        print(f"  {state} --> {trans}")

    # 3. Pengujian Konsistensi String pada NFA dan DFA Hasil Konversi
    test_strings = ["ab", "aab", "aba", "b", "abb", "aaab"]
    
    print("\n" + "=" * 55)
    print(" PENGUJIAN KONSISTENSI STRING (NFA vs DFA KONVERSI)")
    print("=" * 55)
    print(f"{'String':<10} | {'NFA Result':<12} | {'DFA Result':<12} | {'Status Konsistensi'}")
    print("-" * 55)

    for s in test_strings:
        nfa_res, _ = nfa_example.process_string(s)
        dfa_res, _ = dfa_converted.process_string(s)
        
        is_consistent = (nfa_res == dfa_res)
        status_str = "KONSISTEN (MATCH)" if is_consistent else "TIDAK KONSISTEN"
        
        print(f"'{s}'".ljust(10) + " | " + str(nfa_res).ljust(12) + " | " + str(dfa_res).ljust(12) + " | " + status_str)
    
    print("=" * 55)

if __name__ == "__main__":
    main()