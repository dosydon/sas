begin_version
3
end_version
begin_metric
0
end_metric
9
begin_variable
var0
-1
3
Atom at(ball1, rooma)
Atom at(ball1, roomb)
<none of those>
end_variable
begin_variable
var1
-1
3
Atom at(ball2, rooma)
Atom at(ball2, roomb)
<none of those>
end_variable
begin_variable
var2
-1
3
Atom at(ball3, rooma)
Atom at(ball3, roomb)
<none of those>
end_variable
begin_variable
var3
-1
3
Atom at(ball4, rooma)
Atom at(ball4, roomb)
<none of those>
end_variable
begin_variable
var4
-1
2
Atom at-robby(rooma)
Atom at-robby(roomb)
end_variable
begin_variable
var5
-1
5
Atom carry(ball1, left)
Atom carry(ball2, left)
Atom carry(ball3, left)
Atom carry(ball4, left)
Atom free(left)
end_variable
begin_variable
var6
-1
5
Atom carry(ball1, right)
Atom carry(ball2, right)
Atom carry(ball3, right)
Atom carry(ball4, right)
Atom free(right)
end_variable
begin_variable
var7
0
2
NegatedAtom((4, 0),)
Atom((4, 0),)
end_variable
begin_variable
var8
0
2
NegatedAtom((4, 1),)
Atom((4, 1),)
end_variable
7
begin_mutex_group
4
0 0
0 1
5 0
6 0
end_mutex_group
begin_mutex_group
4
1 0
1 1
5 1
6 1
end_mutex_group
begin_mutex_group
4
2 0
2 1
5 2
6 2
end_mutex_group
begin_mutex_group
4
3 0
3 1
5 3
6 3
end_mutex_group
begin_mutex_group
2
4 0
4 1
end_mutex_group
begin_mutex_group
5
5 0
5 1
5 2
5 3
5 4
end_mutex_group
begin_mutex_group
5
6 0
6 1
6 2
6 3
6 4
end_mutex_group
begin_state
0
0
0
0
0
4
4
0
0
end_state
begin_goal
4
0 1
1 1
2 1
3 1
end_goal
32
begin_operator
drop ball1 rooma left
1
7 1
3
0 0 -1 0
0 4 -1 0
0 5 0 4
1
end_operator
begin_operator
drop ball1 rooma right
1
7 1
3
0 0 -1 0
0 4 -1 0
0 6 0 4
1
end_operator
begin_operator
drop ball1 roomb left
1
8 1
3
0 0 -1 1
0 4 -1 1
0 5 0 4
1
end_operator
begin_operator
drop ball1 roomb right
1
8 1
3
0 0 -1 1
0 4 -1 1
0 6 0 4
1
end_operator
begin_operator
drop ball2 rooma left
1
7 1
3
0 1 -1 0
0 4 -1 0
0 5 1 4
1
end_operator
begin_operator
drop ball2 rooma right
1
7 1
3
0 1 -1 0
0 4 -1 0
0 6 1 4
1
end_operator
begin_operator
drop ball2 roomb left
1
8 1
3
0 1 -1 1
0 4 -1 1
0 5 1 4
1
end_operator
begin_operator
drop ball2 roomb right
1
8 1
3
0 1 -1 1
0 4 -1 1
0 6 1 4
1
end_operator
begin_operator
drop ball3 rooma left
1
7 1
3
0 2 -1 0
0 4 -1 0
0 5 2 4
1
end_operator
begin_operator
drop ball3 rooma right
1
7 1
3
0 2 -1 0
0 4 -1 0
0 6 2 4
1
end_operator
begin_operator
drop ball3 roomb left
1
8 1
3
0 2 -1 1
0 4 -1 1
0 5 2 4
1
end_operator
begin_operator
drop ball3 roomb right
1
8 1
3
0 2 -1 1
0 4 -1 1
0 6 2 4
1
end_operator
begin_operator
drop ball4 rooma left
1
7 1
3
0 3 -1 0
0 4 -1 0
0 5 3 4
1
end_operator
begin_operator
drop ball4 rooma right
1
7 1
3
0 3 -1 0
0 4 -1 0
0 6 3 4
1
end_operator
begin_operator
drop ball4 roomb left
1
8 1
3
0 3 -1 1
0 4 -1 1
0 5 3 4
1
end_operator
begin_operator
drop ball4 roomb right
1
8 1
3
0 3 -1 1
0 4 -1 1
0 6 3 4
1
end_operator
begin_operator
pick ball1 rooma left
1
7 1
3
0 0 0 2
0 4 -1 0
0 5 4 0
1
end_operator
begin_operator
pick ball1 rooma right
1
7 1
3
0 0 0 2
0 4 -1 0
0 6 4 0
1
end_operator
begin_operator
pick ball1 roomb left
1
8 1
3
0 0 1 2
0 4 -1 1
0 5 4 0
1
end_operator
begin_operator
pick ball1 roomb right
1
8 1
3
0 0 1 2
0 4 -1 1
0 6 4 0
1
end_operator
begin_operator
pick ball2 rooma left
1
7 1
3
0 1 0 2
0 4 -1 0
0 5 4 1
1
end_operator
begin_operator
pick ball2 rooma right
1
7 1
3
0 1 0 2
0 4 -1 0
0 6 4 1
1
end_operator
begin_operator
pick ball2 roomb left
1
8 1
3
0 1 1 2
0 4 -1 1
0 5 4 1
1
end_operator
begin_operator
pick ball2 roomb right
1
8 1
3
0 1 1 2
0 4 -1 1
0 6 4 1
1
end_operator
begin_operator
pick ball3 rooma left
1
7 1
3
0 2 0 2
0 4 -1 0
0 5 4 2
1
end_operator
begin_operator
pick ball3 rooma right
1
7 1
3
0 2 0 2
0 4 -1 0
0 6 4 2
1
end_operator
begin_operator
pick ball3 roomb left
1
8 1
3
0 2 1 2
0 4 -1 1
0 5 4 2
1
end_operator
begin_operator
pick ball3 roomb right
1
8 1
3
0 2 1 2
0 4 -1 1
0 6 4 2
1
end_operator
begin_operator
pick ball4 rooma left
1
7 1
3
0 3 0 2
0 4 -1 0
0 5 4 3
1
end_operator
begin_operator
pick ball4 rooma right
1
7 1
3
0 3 0 2
0 4 -1 0
0 6 4 3
1
end_operator
begin_operator
pick ball4 roomb left
1
8 1
3
0 3 1 2
0 4 -1 1
0 5 4 3
1
end_operator
begin_operator
pick ball4 roomb right
1
8 1
3
0 3 1 2
0 4 -1 1
0 6 4 3
1
end_operator
4
begin_rule
1
4 0
7 0 1
end_rule
begin_rule
1
4 1
8 0 1
end_rule
begin_rule
1
7 1
8 0 1
end_rule
begin_rule
1
8 1
7 0 1
end_rule
2
begin_removed_operator
move rooma roomb
0
1
0 4 0 1
1
end_removed_operator
begin_removed_operator
move roomb rooma
0
1
0 4 1 0
1
end_removed_operator
32
begin_remained_operator
drop ball1 rooma left
1
4 0
2
0 0 -1 0
0 5 0 4
1
end_remained_operator
begin_remained_operator
drop ball1 rooma right
1
4 0
2
0 0 -1 0
0 6 0 4
1
end_remained_operator
begin_remained_operator
drop ball1 roomb left
1
4 1
2
0 0 -1 1
0 5 0 4
1
end_remained_operator
begin_remained_operator
drop ball1 roomb right
1
4 1
2
0 0 -1 1
0 6 0 4
1
end_remained_operator
begin_remained_operator
drop ball2 rooma left
1
4 0
2
0 1 -1 0
0 5 1 4
1
end_remained_operator
begin_remained_operator
drop ball2 rooma right
1
4 0
2
0 1 -1 0
0 6 1 4
1
end_remained_operator
begin_remained_operator
drop ball2 roomb left
1
4 1
2
0 1 -1 1
0 5 1 4
1
end_remained_operator
begin_remained_operator
drop ball2 roomb right
1
4 1
2
0 1 -1 1
0 6 1 4
1
end_remained_operator
begin_remained_operator
drop ball3 rooma left
1
4 0
2
0 2 -1 0
0 5 2 4
1
end_remained_operator
begin_remained_operator
drop ball3 rooma right
1
4 0
2
0 2 -1 0
0 6 2 4
1
end_remained_operator
begin_remained_operator
drop ball3 roomb left
1
4 1
2
0 2 -1 1
0 5 2 4
1
end_remained_operator
begin_remained_operator
drop ball3 roomb right
1
4 1
2
0 2 -1 1
0 6 2 4
1
end_remained_operator
begin_remained_operator
drop ball4 rooma left
1
4 0
2
0 3 -1 0
0 5 3 4
1
end_remained_operator
begin_remained_operator
drop ball4 rooma right
1
4 0
2
0 3 -1 0
0 6 3 4
1
end_remained_operator
begin_remained_operator
drop ball4 roomb left
1
4 1
2
0 3 -1 1
0 5 3 4
1
end_remained_operator
begin_remained_operator
drop ball4 roomb right
1
4 1
2
0 3 -1 1
0 6 3 4
1
end_remained_operator
begin_remained_operator
pick ball1 rooma left
1
4 0
2
0 0 0 2
0 5 4 0
1
end_remained_operator
begin_remained_operator
pick ball1 rooma right
1
4 0
2
0 0 0 2
0 6 4 0
1
end_remained_operator
begin_remained_operator
pick ball1 roomb left
1
4 1
2
0 0 1 2
0 5 4 0
1
end_remained_operator
begin_remained_operator
pick ball1 roomb right
1
4 1
2
0 0 1 2
0 6 4 0
1
end_remained_operator
begin_remained_operator
pick ball2 rooma left
1
4 0
2
0 1 0 2
0 5 4 1
1
end_remained_operator
begin_remained_operator
pick ball2 rooma right
1
4 0
2
0 1 0 2
0 6 4 1
1
end_remained_operator
begin_remained_operator
pick ball2 roomb left
1
4 1
2
0 1 1 2
0 5 4 1
1
end_remained_operator
begin_remained_operator
pick ball2 roomb right
1
4 1
2
0 1 1 2
0 6 4 1
1
end_remained_operator
begin_remained_operator
pick ball3 rooma left
1
4 0
2
0 2 0 2
0 5 4 2
1
end_remained_operator
begin_remained_operator
pick ball3 rooma right
1
4 0
2
0 2 0 2
0 6 4 2
1
end_remained_operator
begin_remained_operator
pick ball3 roomb left
1
4 1
2
0 2 1 2
0 5 4 2
1
end_remained_operator
begin_remained_operator
pick ball3 roomb right
1
4 1
2
0 2 1 2
0 6 4 2
1
end_remained_operator
begin_remained_operator
pick ball4 rooma left
1
4 0
2
0 3 0 2
0 5 4 3
1
end_remained_operator
begin_remained_operator
pick ball4 rooma right
1
4 0
2
0 3 0 2
0 6 4 3
1
end_remained_operator
begin_remained_operator
pick ball4 roomb left
1
4 1
2
0 3 1 2
0 5 4 3
1
end_remained_operator
begin_remained_operator
pick ball4 roomb right
1
4 1
2
0 3 1 2
0 6 4 3
1
end_remained_operator
begin_removed_goal
4
0 1
1 1
2 1
3 1
end_removed_goal
