
# ARG1=${1:-NULL} //programming or scripting language
# ARG2=${2:-NULL} //file name
# cat python/linked_list.py
# if [ $ARG1 = "NULL" ]; then
#     echo "Please enter the programming/scripting language for which you need to see the file as the 1st argument"
# if [ $ARG2 = "NULL" ]; then
#     echo "Please enter the file name as the 2nd argument"

# else
#     if [ $ARG1 = "python" ]; then
ARG1= "python" 
ARG2= "linked_list"
cat python/linked_list.py
    