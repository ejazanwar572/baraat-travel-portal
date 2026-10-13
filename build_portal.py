import json

passengers = [
    # C2 Coach on Shatabdi (Groom's core party)
    {
        "id": "p1",
        "name": "Md Ejaz Anwar (Groom)",
        "short_name": "Ejaz Anwar",
        "age": 30, "gender": "M", "relation": "Groom",
        "phone": "+91 9852218098",
        "leg1": {"train": "12397 Mahabodhi", "coach": "M2", "seat": "10", "berth": "MB (Middle)", "pnr": "650-8443973", "status": "CNF"},
        "leg2": {"train": "12040 Shatabdi", "coach": "C2", "seat": "40", "berth": "Window Side", "pnr": "2842449153", "status": "CNF", "catering": "Non-Veg"},
        "leg3": {"train": "13010 Doon Exp", "coach": "TBD", "seat": "TBD", "berth": "TBD", "pnr": "Pending", "status": "Pending"}
    },
    {
        "id": "p2",
        "name": "Masroor Jahan",
        "short_name": "Masroor Jahan",
        "age": 26, "gender": "F", "relation": "Family",
        "leg1": {"train": "12397 Mahabodhi", "coach": "B1", "seat": "38", "berth": "UB (Upper)", "pnr": "694-8548028", "status": "CNF"},
        "leg2": {"train": "12040 Shatabdi", "coach": "C2", "seat": "41", "berth": "Middle", "pnr": "2842449153", "status": "CNF", "catering": "Non-Veg"},
        "leg3": {"train": "13010 Doon Exp", "coach": "TBD", "seat": "TBD", "berth": "TBD", "pnr": "Pending", "status": "Pending"}
    },
    {
        "id": "p3",
        "name": "Imran Khan",
        "short_name": "Imran Khan",
        "age": 35, "gender": "M", "relation": "Family / Friend",
        "leg1": {"train": "12397 Mahabodhi", "coach": "M3", "seat": "21", "berth": "MB (Middle)", "pnr": "6208461284", "status": "CNF"},
        "leg2": {"train": "12040 Shatabdi", "coach": "C2", "seat": "42", "berth": "Aisle", "pnr": "2842449153", "status": "CNF", "catering": "Non-Veg"},
        "leg3": {"train": "13010 Doon Exp", "coach": "TBD", "seat": "TBD", "berth": "TBD", "pnr": "Pending", "status": "Pending"}
    },
    {
        "id": "p4",
        "name": "Neyaz Apsar",
        "short_name": "Neyaz Apsar",
        "age": 27, "gender": "M", "relation": "Family / Friend",
        "leg1": {"train": "12397 Mahabodhi", "coach": "M3", "seat": "22", "berth": "UB (Upper)", "pnr": "6208461284", "status": "CNF"},
        "leg2": {"train": "12040 Shatabdi", "coach": "C2", "seat": "43", "berth": "Aisle", "pnr": "2842449153", "status": "CNF", "catering": "Non-Veg"},
        "leg3": {"train": "13010 Doon Exp", "coach": "TBD", "seat": "TBD", "berth": "TBD", "pnr": "Pending", "status": "Pending"}
    },
    {
        "id": "p5",
        "name": "Rizwan Khan",
        "short_name": "Rizwan Khan",
        "age": 25, "gender": "M", "relation": "Family / Friend",
        "leg1": {"train": "12397 Mahabodhi", "coach": "M2", "seat": "13", "berth": "MB (Middle)", "pnr": "650-8443973", "status": "CNF"},
        "leg2": {"train": "12040 Shatabdi", "coach": "C2", "seat": "44", "berth": "Window Side", "pnr": "2842449153", "status": "CNF", "catering": "Non-Veg"},
        "leg3": {"train": "13010 Doon Exp", "coach": "TBD", "seat": "TBD", "berth": "TBD", "pnr": "Pending", "status": "Pending"}
    },
    {
        "id": "p6",
        "name": "Aftab Alam",
        "short_name": "Aftab Alam",
        "age": 28, "gender": "M", "relation": "Family / Friend",
        "leg1": {"train": "12397 Mahabodhi", "coach": "M2", "seat": "12", "berth": "LB (Lower)", "pnr": "650-8443973", "status": "CNF"},
        "leg2": {"train": "12040 Shatabdi", "coach": "C2", "seat": "45", "berth": "Window Side", "pnr": "2842449153", "status": "CNF", "catering": "Non-Veg"},
        "leg3": {"train": "13010 Doon Exp", "coach": "TBD", "seat": "TBD", "berth": "TBD", "pnr": "Pending", "status": "Pending"}
    },
    {
        "id": "p7",
        "name": "Md Tarique",
        "short_name": "Md Tarique",
        "age": 30, "gender": "M", "relation": "Family / Friend",
        "leg1": {"train": "12397 Mahabodhi", "coach": "M2", "seat": "39", "berth": "SL (Side Lower)", "pnr": "654-8443673", "status": "CNF"},
        "leg2": {"train": "12040 Shatabdi", "coach": "C2", "seat": "33", "berth": "Aisle", "pnr": "2461846773", "status": "CNF", "catering": "Non-Veg"},
        "leg3": {"train": "13010 Doon Exp", "coach": "TBD", "seat": "TBD", "berth": "TBD", "pnr": "Pending", "status": "Pending"}
    },
    {
        "id": "p8",
        "name": "Ejaz Khan",
        "short_name": "Ejaz Khan",
        "age": 30, "gender": "M", "relation": "Family / Friend",
        "leg1": {"train": "12397 Mahabodhi", "coach": "M2", "seat": "35", "berth": "UB (Upper)", "pnr": "654-8443673", "status": "CNF"},
        "leg2": {"train": "12040 Shatabdi", "coach": "C2", "seat": "34", "berth": "Middle", "pnr": "2461846773", "status": "CNF", "catering": "Non-Veg"},
        "leg3": {"train": "13010 Doon Exp", "coach": "TBD", "seat": "TBD", "berth": "TBD", "pnr": "Pending", "status": "Pending"}
    },

    # Elders / Senior Group (C3 Coach on Shatabdi & 1A on Doon Exp)
    {
        "id": "p9",
        "name": "Md Azad Anwar (Father of Groom)",
        "short_name": "Azad Anwar",
        "age": 55, "gender": "M", "relation": "Father of Groom",
        "leg1": {"train": "12397 Mahabodhi", "coach": "M2", "seat": "26", "berth": "MB (Middle)", "pnr": "640-8444042", "status": "CNF"},
        "leg2": {"train": "12040 Shatabdi", "coach": "C3", "seat": "70", "berth": "Window Side", "pnr": "2957815277", "status": "CNF", "catering": "Non-Veg"},
        "leg3": {"train": "13010 Doon Exp", "coach": "1A", "seat": "Cabin/Coupe", "berth": "First AC (CNF)", "pnr": "2623649572", "status": "CNF"}
    },
    {
        "id": "p10",
        "name": "Sohail Akhtar",
        "short_name": "Sohail Akhtar",
        "age": 40, "gender": "M", "relation": "Senior Family",
        "leg1": {"train": "12397 Mahabodhi", "coach": "M2", "seat": "30", "berth": "UB (Upper)", "pnr": "640-8444042", "status": "CNF"},
        "leg2": {"train": "12040 Shatabdi", "coach": "C3", "seat": "TBD (Ticket 1)", "berth": "TBD", "pnr": "Ticket 1", "status": "CNF", "catering": "Non-Veg"},
        "leg3": {"train": "13010 Doon Exp", "coach": "1A", "seat": "Cabin/Coupe", "berth": "First AC (CNF)", "pnr": "2623649572", "status": "CNF"}
    },
    {
        "id": "p11",
        "name": "Md Maaz Khan",
        "short_name": "Md Maaz Khan",
        "age": 55, "gender": "M", "relation": "Senior Family",
        "leg1": {"train": "12397 Mahabodhi", "coach": "M2", "seat": "11", "berth": "UB (Upper)", "pnr": "650-8443973", "status": "CNF"},
        "leg2": {"train": "12040 Shatabdi", "coach": "C3", "seat": "59", "berth": "Window Side", "pnr": "2842448764", "status": "CNF", "catering": "Non-Veg"},
        "leg3": {"train": "13010 Doon Exp", "coach": "1A", "seat": "Cabin/Coupe", "berth": "First AC (CNF)", "pnr": "2461735759", "status": "CNF"}
    },
    {
        "id": "p12",
        "name": "Md Mustaq Alam",
        "short_name": "Mustaq Alam",
        "age": 58, "gender": "M", "relation": "Senior Family",
        "leg1": {"train": "12397 Mahabodhi", "coach": "M2", "seat": "9", "berth": "LB (Lower)", "pnr": "650-8443973", "status": "CNF"},
        "leg2": {"train": "12040 Shatabdi", "coach": "C3", "seat": "18", "berth": "Middle", "pnr": "2361756513", "status": "CNF", "catering": "Non-Veg"},
        "leg3": {"train": "13010 Doon Exp", "coach": "1A", "seat": "Cabin/Coupe", "berth": "First AC (CNF)", "pnr": "2461735759", "status": "CNF"}
    },
    {
        "id": "p13",
        "name": "Md Shami Akhtar",
        "short_name": "Shami Akhtar",
        "age": 56, "gender": "M", "relation": "Senior Family",
        "leg1": {"train": "12397 Mahabodhi", "coach": "M2", "seat": "27", "berth": "UB (Upper)", "pnr": "640-8444042", "status": "CNF"},
        "leg2": {"train": "12040 Shatabdi", "coach": "C3", "seat": "16", "berth": "Aisle", "pnr": "2361756513", "status": "CNF", "catering": "Non-Veg"},
        "leg3": {"train": "13010 Doon Exp", "coach": "3A", "seat": "WL 246", "berth": "Waitlisted", "pnr": "2842426597", "status": "WL"}
    },
    {
        "id": "p14",
        "name": "Sarfaraz Khan",
        "short_name": "Sarfaraz Khan",
        "age": 48, "gender": "M", "relation": "Family",
        "leg1": {"train": "12397 Mahabodhi", "coach": "M2", "seat": "37", "berth": "MB (Middle)", "pnr": "654-8443673", "status": "CNF"},
        "leg2": {"train": "12040 Shatabdi", "coach": "C3", "seat": "71", "berth": "Middle", "pnr": "2957815277", "status": "CNF", "catering": "Non-Veg"},
        "leg3": {"train": "13010 Doon Exp", "coach": "TBD", "seat": "TBD", "berth": "TBD", "pnr": "Pending", "status": "Pending"}
    },
    {
        "id": "p15",
        "name": "Naushad Alam",
        "short_name": "Naushad Alam",
        "age": 48, "gender": "M", "relation": "Family",
        "leg1": {"train": "12397 Mahabodhi", "coach": "B1", "seat": "16", "berth": "SU (Side Upper)", "pnr": "694-8548028", "status": "CNF"},
        "leg2": {"train": "12040 Shatabdi", "coach": "C3", "seat": "19", "berth": "Window Side", "pnr": "2361756513", "status": "CNF", "catering": "Non-Veg"},
        "leg3": {"train": "13010 Doon Exp", "coach": "TBD", "seat": "TBD", "berth": "TBD", "pnr": "Pending", "status": "Pending"}
    },
    {
        "id": "p16",
        "name": "Md Aklimuddin",
        "short_name": "Aklimuddin",
        "age": 47, "gender": "M", "relation": "Family",
        "leg1": {"train": "12397 Mahabodhi", "coach": "M2", "seat": "29", "berth": "MB (Middle)", "pnr": "640-8444042", "status": "CNF"},
        "leg2": {"train": "12040 Shatabdi", "coach": "C3", "seat": "72", "berth": "Aisle", "pnr": "2957815277", "status": "CNF", "catering": "Non-Veg"},
        "leg3": {"train": "13010 Doon Exp", "coach": "TBD", "seat": "TBD", "berth": "TBD", "pnr": "Pending", "status": "Pending"}
    },
    {
        "id": "p17",
        "name": "Minhaj Khan",
        "short_name": "Minhaj Khan",
        "age": 45, "gender": "M", "relation": "Family",
        "leg1": {"train": "12397 Mahabodhi", "coach": "M2", "seat": "32", "berth": "SU (Side Upper)", "pnr": "640-8444042", "status": "CNF"},
        "leg2": {"train": "12040 Shatabdi", "coach": "C3", "seat": "67", "berth": "Middle", "pnr": "2842448764", "status": "CNF", "catering": "Non-Veg"},
        "leg3": {"train": "13010 Doon Exp", "coach": "TBD", "seat": "TBD", "berth": "TBD", "pnr": "Pending", "status": "Pending"}
    },
    {
        "id": "p18",
        "name": "Md Siraj Anwar",
        "short_name": "Siraj Anwar",
        "age": 34, "gender": "M", "relation": "Family",
        "leg1": {"train": "12397 Mahabodhi", "coach": "M2", "seat": "14", "berth": "UB (Upper)", "pnr": "650-8443973", "status": "CNF"},
        "leg2": {"train": "12040 Shatabdi", "coach": "C3", "seat": "68", "berth": "Aisle", "pnr": "2842448764", "status": "CNF", "catering": "Non-Veg"},
        "leg3": {"train": "13010 Doon Exp", "coach": "TBD", "seat": "TBD", "berth": "TBD", "pnr": "Pending", "status": "Pending"}
    },
    {
        "id": "p19",
        "name": "Md Haider Khan",
        "short_name": "Haider Khan",
        "age": 34, "gender": "M", "relation": "Family",
        "leg1": {"train": "12397 Mahabodhi", "coach": "M2", "seat": "34", "berth": "MB (Middle)", "pnr": "654-8443673", "status": "CNF"},
        "leg2": {"train": "12040 Shatabdi", "coach": "C3", "seat": "74", "berth": "Window Side", "pnr": "2957815277", "status": "CNF", "catering": "Non-Veg"},
        "leg3": {"train": "13010 Doon Exp", "coach": "TBD", "seat": "TBD", "berth": "TBD", "pnr": "Pending", "status": "Pending"}
    },
    {
        "id": "p20",
        "name": "Shahrukh Khan",
        "short_name": "Shahrukh Khan",
        "age": 33, "gender": "M", "relation": "Family / Friend",
        "leg1": {"train": "12397 Mahabodhi", "coach": "M3", "seat": "19", "berth": "UB (Upper)", "pnr": "6208461284", "status": "CNF"},
        "leg2": {"train": "12040 Shatabdi", "coach": "C3", "seat": "76", "berth": "Aisle", "pnr": "2842448764", "status": "CNF", "catering": "Non-Veg"},
        "leg3": {"train": "13010 Doon Exp", "coach": "TBD", "seat": "TBD", "berth": "TBD", "pnr": "Pending", "status": "Pending"}
    },
    {
        "id": "p21",
        "name": "Md Irfan Alam",
        "short_name": "Irfan Alam",
        "age": 32, "gender": "M", "relation": "Family",
        "leg1": {"train": "12397 Mahabodhi", "coach": "B1", "seat": "34", "berth": "MB (Middle)", "pnr": "694-8548028", "status": "CNF"},
        "leg2": {"train": "12040 Shatabdi", "coach": "C3", "seat": "66", "berth": "Window Side", "pnr": "2842448764", "status": "CNF", "catering": "Non-Veg"},
        "leg3": {"train": "13010 Doon Exp", "coach": "TBD", "seat": "TBD", "berth": "TBD", "pnr": "Pending", "status": "Pending"}
    },
    {
        "id": "p22",
        "name": "Md Imtiyaz Alam",
        "short_name": "Imtiyaz Alam",
        "age": 32, "gender": "M", "relation": "Family",
        "leg1": {"train": "12397 Mahabodhi", "coach": "B1", "seat": "35", "berth": "UB (Upper)", "pnr": "694-8548028", "status": "CNF"},
        "leg2": {"train": "12040 Shatabdi", "coach": "C3", "seat": "69", "berth": "Window Side", "pnr": "2842448764", "status": "CNF", "catering": "Non-Veg"},
        "leg3": {"train": "13010 Doon Exp", "coach": "TBD", "seat": "TBD", "berth": "TBD", "pnr": "Pending", "status": "Pending"}
    },
    {
        "id": "p23",
        "name": "Mokhatib Alam",
        "short_name": "Mokhatib Alam",
        "age": 30, "gender": "M", "relation": "Family",
        "leg1": {"train": "12397 Mahabodhi", "coach": "M2", "seat": "48", "berth": "SU (Side Upper)", "pnr": "640-8444042", "status": "CNF"},
        "leg2": {"train": "12040 Shatabdi", "coach": "C3", "seat": "73", "berth": "Middle", "pnr": "2957815277", "status": "CNF", "catering": "Non-Veg"},
        "leg3": {"train": "13010 Doon Exp", "coach": "TBD", "seat": "TBD", "berth": "TBD", "pnr": "Pending", "status": "Pending"}
    },
    {
        "id": "p24",
        "name": "Md Shahil Anwar",
        "short_name": "Shahil Anwar",
        "age": 28, "gender": "M", "relation": "Family",
        "leg1": {"train": "12397 Mahabodhi", "coach": "M2", "seat": "38", "berth": "UB (Upper)", "pnr": "654-8443673", "status": "CNF"},
        "leg2": {"train": "12040 Shatabdi", "coach": "C3", "seat": "17", "berth": "Middle", "pnr": "2361756513", "status": "CNF", "catering": "Non-Veg"},
        "leg3": {"train": "13010 Doon Exp", "coach": "3A", "seat": "WL 245", "berth": "Waitlisted", "pnr": "2842426597", "status": "WL"}
    },
    {
        "id": "p25",
        "name": "Nedayur Rehman",
        "short_name": "Nedayur Rehman",
        "age": 28, "gender": "M", "relation": "Family / Friend",
        "leg1": {"train": "12397 Mahabodhi", "coach": "B1", "seat": "37", "berth": "MB (Middle)", "pnr": "694-8548028", "status": "CNF"},
        "leg2": {"train": "12040 Shatabdi", "coach": "C3", "seat": "33", "berth": "Aisle", "pnr": "2361756513", "status": "CNF", "catering": "Non-Veg"},
        "leg3": {"train": "13010 Doon Exp", "coach": "TBD", "seat": "TBD", "berth": "TBD", "pnr": "Pending", "status": "Pending"}
    },
    {
        "id": "p26",
        "name": "Amjad Khan",
        "short_name": "Amjad Khan",
        "age": 27, "gender": "M", "relation": "Family / Friend",
        "leg1": {"train": "12397 Mahabodhi", "coach": "M2", "seat": "40", "berth": "SU (Side Upper)", "pnr": "654-8443673", "status": "CNF"},
        "leg2": {"train": "12040 Shatabdi", "coach": "C3", "seat": "75", "berth": "Window Side", "pnr": "2957815277", "status": "CNF", "catering": "Non-Veg"},
        "leg3": {"train": "13010 Doon Exp", "coach": "3A", "seat": "WL 243", "berth": "Waitlisted", "pnr": "2842426597", "status": "WL"}
    },
    {
        "id": "p27",
        "name": "Md Alatamas Khan",
        "short_name": "Alatamas Khan",
        "age": 23, "gender": "M", "relation": "Youth / Cousin",
        "leg1": {"train": "12397 Mahabodhi", "coach": "B1", "seat": "42", "berth": "MB (Middle)", "pnr": "660-8443705", "status": "CNF"},
        "leg2": {"train": "12040 Shatabdi", "coach": "C3", "seat": "34", "berth": "Window Side", "pnr": "2361756513", "status": "CNF", "catering": "Non-Veg"},
        "leg3": {"train": "13010 Doon Exp", "coach": "TBD", "seat": "TBD", "berth": "TBD", "pnr": "Pending", "status": "Pending"}
    },
    {
        "id": "p28",
        "name": "Senior Guest 1 (M 60)",
        "short_name": "Guest (M 60)",
        "age": 60, "gender": "M", "relation": "Elder Relative",
        "leg1": {"train": "12397 Mahabodhi", "coach": "B1", "seat": "43", "berth": "UB (Upper)", "pnr": "660-8443705", "status": "CNF"},
        "leg2": {"train": "12040 Shatabdi", "coach": "C3 (TBD)", "seat": "TBD", "berth": "Ticket 1 Pending", "pnr": "Ticket 1", "status": "CNF", "catering": "Non-Veg"},
        "leg3": {"train": "13010 Doon Exp", "coach": "TBD", "seat": "TBD", "berth": "TBD", "pnr": "Pending", "status": "Pending"}
    },
    {
        "id": "p29",
        "name": "Family Guest 2 (M 19)",
        "short_name": "Guest (M 19)",
        "age": 19, "gender": "M", "relation": "Youth / Relative",
        "leg1": {"train": "12397 Mahabodhi", "coach": "B1", "seat": "45", "berth": "MB (Middle)", "pnr": "660-8443705", "status": "CNF"},
        "leg2": {"train": "12040 Shatabdi", "coach": "C3 (TBD)", "seat": "TBD", "berth": "Ticket 1 Pending", "pnr": "Ticket 1", "status": "CNF", "catering": "Non-Veg"},
        "leg3": {"train": "13010 Doon Exp", "coach": "TBD", "seat": "TBD", "berth": "TBD", "pnr": "Pending", "status": "Pending"}
    },
    {
        "id": "p30",
        "name": "Youth Guest 3 (M 16)",
        "short_name": "Guest (M 16)",
        "age": 16, "gender": "M", "relation": "Youth / Relative",
        "leg1": {"train": "12397 Mahabodhi", "coach": "B1", "seat": "40", "berth": "SU (Side Upper)", "pnr": "694-8548028", "status": "CNF"},
        "leg2": {"train": "12040 Shatabdi", "coach": "C3 (TBD)", "seat": "TBD", "berth": "Ticket 1 Pending", "pnr": "Ticket 1", "status": "CNF", "catering": "Non-Veg"},
        "leg3": {"train": "13010 Doon Exp", "coach": "TBD", "seat": "TBD", "berth": "TBD", "pnr": "Pending", "status": "Pending"}
    }
]

print(f"Loaded {len(passengers)} passengers successfully.")
