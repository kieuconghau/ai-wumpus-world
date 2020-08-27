# Quy định chung
## Actions
1. Turn left
2. Turn right
3. Turn up
4. Turn down
5. Move forward
    - Sau khi tiến tới, ô phía sau được explored.
    - Trừ 10 điểm.
6. Pick up Gold
    - Cộng 100 điểm.
7. Perceive Breeze
8. Perceive Stench
9. Shoot an Arrow
    - Trừ 100 điểm.
10. Kill Wumpus
    - Ô chứa Wumpus bị bắn chính là ô phía trước mặt của Agent, ô này được explored.
    - Bỏ các Stench xung quanh của ô chứa Wumpus này.
11. Be eaten by Wumpus
    - Trừ 10000 điểm.
    - Set state thành Gameover.
    - Hiện màn hình Gameover.
12. Fall into Pit
    - Trừ 10000 điểm.
    - Set state thành Gameover.
    - Hiện màn hình Gameover.
13. Kill all Wumpus and Grab all Gold
    - Set state thành Victory.
14. Climb out of the cave.
    - Cộng 10 điểm.
    - Nếu state hiện tại là:
        - Victory: hiện màn hình Victory.
        - TryYourBest: hiện màn hình TryYourBest.

Lưu ý: state mặc định là TryYourBest (tức thoát được hang nhưng chưa giết hết Wumpus và chưa nhặt hết Gold).

## Tọa độ của Map
<p align='center'><img align='center' src="Assets/Readme/map_coordinate.png" alt='Map Coordinate'></p>