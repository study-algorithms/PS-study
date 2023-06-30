routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]

def solution(routes):
    routes = sorted(routes)

    new_cam_pos = routes[0][1]

    cam = []
    for i in range(1, len(routes)):
        if routes[i][0] <= new_cam_pos:
            new_cam_pos = min(new_cam_pos, routes[i][1])
        else:
            cam.append(new_cam_pos)
            new_cam_pos = routes[i][1]
    cam.append(new_cam_pos)
    return len(cam)

print(solution(routes))