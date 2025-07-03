while True:
    
    for i in range(10, 101, 10):
        print(i)
    
    again = input("Nog een keer proberen? (ja/nee of j/n) ").lower()
    if again in ['nee', 'n']:
        print("Tot ziens!")
        break
      
"""	
06 Tientallen
Gebruik een lus om alle tientallen van 10 tot en met 100 op het scherm te tonen.
"""
