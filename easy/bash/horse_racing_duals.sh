<<comment
HORSE-RACING DUALS
Difficulty: Easy
Link: https://www.codingame.com/training/easy/horse-racing-duals
comment

declare -a strengths # declaring an array that will keep the strength of each horse 
diff=9999999 # the difference between the two closest strengths; the initial value of variable is the biggest possible difference

read N

for (( i=0; i<$N; i++ )); do
    read strengths[i]
done

readarray -t sorted < <(printf '%s\n' "${strengths[@]}" | sort -g) # sorting strengths; adding elements to 'sorted' array

for (( i=0; i<${#sorted[@]}-1; i++ ))
do
current_diff=$((${sorted[$i+1]}-${sorted[$i]})) # difference between the current element and the following
if [[ $current_diff -ge 0 && $current_diff -le $diff ]]
then
diff=$current_diff
fi
done

echo $diff