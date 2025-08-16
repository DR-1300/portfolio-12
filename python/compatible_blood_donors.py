compatible_donors = {
    'A+' : ['A+', 'A-', 'O+', 'O-'],
    'A-' : ['A-', 'O+', 'O-'],
    'B+' : ['B+', 'B-', 'O+', 'O-'],
    'B-' : ['B-', 'O+', 'O-'],
    'AB+' : ['AB+', 'AB-', 'A+', 'A-', 'B+', 'B-', 'O+', 'O-'],
    'AB-' : ['AB-', 'A+', 'A-', 'B+', 'B-', 'O+', 'O-'],
    'O+' : ['O+', 'O-'],
    'O-' : ['O-']
}

recipient = input("Enter your blood group: ").strip().upper()

if recipient in compatible_donors:
    print(f"\nCompatible donors groups for {recipient}:")
    for bg in compatible_donors[recipient]:
        print(f"- {bg}")
else:
    print("Invalid blood group")