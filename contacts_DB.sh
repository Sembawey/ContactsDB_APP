#!/usr/bin/bash
#function======================================================
main_menu () {
	echo " Welcome to the Main Menu"
	echo "- press i to add new contact"
        echo "- press v to view all contacts"
        echo "- press s to search for record"
        echo "- press e to delete all contacts"
        echo "- press d to delete one contact"
        echo "- press q to exit"
	read -p "Please enter you input: " choice
}
#==============================================================
add_contact () {
	read -p "Enter your first name: " fname
	read -p "Enter your last name: " lname
	read -p "Enter your Email: " email
	read -p "Enter your phone number: " phone
	echo "First Name: $fname Last Name: $lname Email: $email Phone Number: $phone" >> database.txt
}
#==============================================================
quit() {
	read -p "To return to main menu press(m) or (q) for exit: " q
	if [ "$q" == "m" ] || [ "$q" == "M" ]
	then
		main_menu
	elif [ "$q" == "q" ] || [ "$q" == "Q" ]
	then
		echo " Exiting ... "
		exit
	else
	       	echo " Wrong Selection "
		quit
	fi
}
#============================ Code ============================
#============================ Code ============================
main_menu
while [ true ]
do
	if [ "$choice" == "i" ] || [ "$choice" == "I" ]
	then
		echo "Adding New Contact ..."
		add_contact
		echo "Contact Added to DB Sucessfully"
		quit


	elif [ "$choice" == "v" ] || [ "$choice" == "V" ]
	then
		echo "== All Contacts=="
		cat database.txt
		echo ""
		echo ""
		quit


	elif [ "$choice" == "s" ] || [ "$choice" == "S" ]
	then
		read -p "Please enter contact Pattern: " search
		echo "Searched Contact Details: "
		grep "$search" database.txt --color
		quit


	elif [ "$choice" == "e" ] || [ "$choice" == "E" ]
	then
		echo "Deleting All Contacts ..."
		echo "" > database.txt
		echo "All Contacts Deleted Sucessfully"
		quit


	elif [ "$choice" == "d" ] || [ "$choice" == "D" ]
	then
		read -p "Enter the pattern for the contact to be deleted: " del_contact
		sed -i "/$del_contact/d" database.txt
		echo "Cotact $del_contact Deleted Sucessfully"
		quit


	elif [ "$choice" == "q" ] || [ "$choice" == "Q" ]
	then
		echo " Exiting ... "
                exit


	else
		echo " Wrong Initial Input "
		main_menu
	fi
done
#==============================================================
