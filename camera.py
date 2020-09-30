import cv2
import client_io
import json

WIDTH = 320
HEIGHT = 240
IP = '192.168.0.xxx'
PORT_POSE = 22223
PORT_READ = 22225

# 画面クリック時のコールバック関数
def on_cliecked(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        # クリック時は頭部動作、Ctrl+クリック時は頭部＋身体動作
        pose_map = calc_pose_map_head_body(x, y) if flags & cv2.EVENT_FLAG_CTRLKEY else calc_pose_map_head(x, y)
        send_pose(500, pose_map)
        print(pose_map)

def calc_dyaw_dpitch(x, y):
    dx = x - WIDTH / 2
    dy = y - HEIGHT / 2
    dyaw = round(dx * 48 / WIDTH) * (-1) # dx : width(pixel) = dyaw : 48deg
    dpitch = round(dy * 36 / HEIGHT) # dy : height(pixel) = dpitch : 36deg
    return (dyaw, dpitch)

def calc_pose_map_head(x, y):
    dyaw, dpitch = calc_dyaw_dpitch(x, y)
    cur_pose_map = read_pose_map()
    pose_map = {}
    # head yaw
    if   cur_pose_map['HEAD_Y'] + dyaw > 85:
        pose_map.update(HEAD_Y=85)
    elif cur_pose_map['HEAD_Y'] + dyaw < -85:
        pose_map.update(HEAD_Y=-85)
    else:
        pose_map.update(HEAD_Y=cur_pose_map['HEAD_Y'] + dyaw)
    # head pitch
    if   cur_pose_map['HEAD_P'] + dpitch > 5:
        pose_map.update(HEAD_P=5)
    elif cur_pose_map['HEAD_P'] + dpitch < -27:
        pose_map.update(HEAD_P=-27)
    else:
        pose_map.update(HEAD_P=cur_pose_map['HEAD_P'] + dpitch)
    return pose_map

def calc_pose_map_head_body(x, y):
    dyaw, dpitch = calc_dyaw_dpitch(x, y)
    cur_pose_map = read_pose_map()
    pose_map = {}
    # head and body yaw
    if   cur_pose_map['BODY_Y'] + cur_pose_map['HEAD_Y'] + dyaw > 61:
        pose_map.update(BODY_Y=61, HEAD_Y=cur_pose_map['BODY_Y'] + cur_pose_map['HEAD_Y'] + dyaw - 61)
    elif cur_pose_map['BODY_Y'] + cur_pose_map['HEAD_Y'] + dyaw < -61:
        pose_map.update(BODY_Y=-61, HEAD_Y=cur_pose_map['BODY_Y'] + cur_pose_map['HEAD_Y'] + dyaw + 61)
    else:
        pose_map.update(BODY_Y=cur_pose_map['BODY_Y'] + cur_pose_map['HEAD_Y'] + dyaw, HEAD_Y=0)
    # head pitch
    if   cur_pose_map['HEAD_P'] + dpitch > 5:
        pose_map.update(HEAD_P=5)
    elif cur_pose_map['HEAD_P'] + dpitch < -27:
        pose_map.update(HEAD_P=-27)
    else:
        pose_map.update(HEAD_P=cur_pose_map['HEAD_P'] + dpitch)
    return pose_map

def calc_pose_map_pointing():
    cur_pose_map = read_pose_map()
    direction = 'right' if cur_pose_map['BODY_Y'] < 0 else 'left'
    if direction == 'right':
        body_y = cur_pose_map['BODY_Y'] + 20
        r_shou = 3 * cur_pose_map['HEAD_P'] + 30
        print('body_y =', body_y, 'head_p =', cur_pose_map['HEAD_P'], ' r_shou =', r_shou)
        pose_map = dict(BODY_Y=body_y, HEAD_Y=-20, R_SHOU=r_shou, R_ELBO=0)
    elif direction == 'left':
        body_y = cur_pose_map['BODY_Y'] - 20
        l_shou = -3 * cur_pose_map['HEAD_P'] - 30
        print('body_y =', body_y, 'head_p =', cur_pose_map['HEAD_P'], ' l_shou =', l_shou)
        pose_map = dict(BODY_Y=body_y, HEAD_Y=20, L_SHOU=l_shou, L_ELBO=0)
    return pose_map


# ロボットの現在のポーズ（関節角度）の読込
def read_pose_map():
    client = client_io.MyClient()
    client.connect(IP, PORT_READ)
    data = client.read()
    client.close()    
    return json.loads(data.decode('utf-8'))

# ロボットのポーズの送信
def send_pose(msec, pose_map):
    data = dict(msec=msec, map=pose_map)
    cli = client_io.MyClient()
    cli.connect(IP, PORT_POSE)
    cli.write(json.dumps(data).encode('utf-8'))
    cli.close()


# メイン処理
elems = [
    'udpsrc port=5000 caps = "application/x-rtp,encoding-name=JPEG,payload=26"',
    'queue',
    'rtpjpegdepay',
    'jpegdec',
    'videoconvert',
    'appsink udpsrc port=5001 caps = "application/x-rtp,clock-rate=44100,channels=1,payload=96"',
    'queue',
    'rtpL16depay',
    'audioconvert',
    'directsoundsink'
]

src = ' ! '.join(elems)
cap = cv2.VideoCapture(src)
cv2.namedWindow('image')
cv2.setMouseCallback('image', on_cliecked)

try:
    while(cap.isOpened()):
        ret, frame = cap.read()
        if frame is None:
            break
        cv2.imshow('image',frame)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('p'):
            # send right-hand pointing
            pose_map = calc_pose_map_pointing()
            send_pose(500, pose_map)
        elif k == ord(' '):
            # send left-hand pointing
            pose_map = dict(L_SHOU=-90, R_SHOU=90)
            send_pose(500, pose_map)


except KeyboardInterrupt:
    cv2.destroyAllWindows()
