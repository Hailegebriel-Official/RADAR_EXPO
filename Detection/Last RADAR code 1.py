import pygame
import math
import numpy as np
import pyaudio
import audioop
import matplotlib.pyplot as plt


SCREEN_WIDTH = 1538
SCREEN_HEIGHT = 800
CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
CENTER_2 = (SCREEN_WIDTH // 1.16, SCREEN_HEIGHT // 3)
CENTER_3 = (SCREEN_WIDTH // 1.16, SCREEN_HEIGHT // 1.5)
CIRCLE_RADIUS = 100
ROTATION_SPEED = 2  

FILL_THRESHOLD = 70  
FILL_SPEED = 0.1122  
sound_speed =343


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_2 = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_3 = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
 
 
screenc = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Blinking Circles")
circle_radius = 10
circle_color1 = (0, 100, 0)  # Red
circle_color2 = (0, 135, 0)  # Green
circle_color3 = (0, 255, 0)  # Blue

pygame.display.set_caption('writing color')
write_text = 'hailegebriel'


clock = pygame.time.Clock()
blink_frequency = 1  # Blinking frequency in Hz
draw_circles = True

"grid_size = 20"

font = pygame.font.Font(None, 30)


BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

pygame.display.set_caption("Rocket Icons")
rocket_icon = pygame.image.load("map2.png") 
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, 
                    channels=1, 
                    rate=44100, 
                    input=True, 
                    frames_per_buffer=1024)

angle = 0
fill_circle = False
fill_value = 0

start_time = pygame.time.get_ticks()  


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    screen_2.fill(BLACK)
    screen_3.fill(BLACK)
    
    screen.blit(rocket_icon, (165,-165))
    
    
    
    elapsed_timec = pygame.time.get_ticks() / 1000.0  # Convert elapsed time to seconds
    if elapsed_timec % (1 / blink_frequency) < 0.5:
        draw_circles = True
    else:
        draw_circles = False

    if draw_circles:
        pygame.draw.circle(screenc, circle_color1, (50, 450), circle_radius)
        pygame.draw.circle(screenc, circle_color2, (80, 450), circle_radius)
        pygame.draw.circle(screenc, circle_color3, (110, 450), circle_radius)
    
    
    
    degree_markers = [0, 90, 180, 270]
    for degree in degree_markers:
        marker_angle = math.radians(degree)
        marker_length = CIRCLE_RADIUS + 170  
        marker_x = CENTER[0] + marker_length * math.cos(marker_angle)        
        marker_y = CENTER[1] + marker_length * math.sin(marker_angle)
        
        
        pygame.draw.line(screen, GREEN, CENTER, (marker_x, marker_y), 1)
        
        
        marker_text = font.render(str(degree) + "°", True, GREEN)
        text_width, text_height = marker_text.get_size()
        screen.blit(marker_text, (marker_x - text_width // 2, marker_y - text_height // 2))

    
    
    rotated_line = pygame.Surface((2 * CIRCLE_RADIUS, 2 * CIRCLE_RADIUS), pygame.SRCALPHA)
    
    pygame.draw.line(rotated_line, GREEN, (CIRCLE_RADIUS, CIRCLE_RADIUS), (CIRCLE_RADIUS, 0), 45)
    
    rotated_line = pygame.transform.rotate(rotated_line, angle)
    angle += ROTATION_SPEED
    if angle >= 360:
        angle = 0

    
    scan_line_length = 2.7*CIRCLE_RADIUS
    scan_line_angle = math.radians(angle)
    scan_line_end_x = CENTER[0] + scan_line_length * math.cos(scan_line_angle)
    scan_line_end_y = CENTER[1] + scan_line_length * math.sin(scan_line_angle)
    pygame.draw.line(screen, GREEN, CENTER, (scan_line_end_x, scan_line_end_y), 2)
    
    audio_data = stream.read(1024)
    rms = audioop.rms(audio_data, 2)
    if rms > FILL_THRESHOLD:
        fill_value += FILL_SPEED                                                                                                                                                                                                              
    else:
        fill_value -= 10*FILL_SPEED
        if fill_value < 0:
            fill_value = 0

    
    data = stream.read(1024)
    audio_data = np.frombuffer(data, dtype=np.int16)
    decibel = 20 * np.log10(np.abs(audio_data).mean())
    distance_old = 100 / (decibel + 1)
    distance = distance_old - 1
    print(f"Decibel level: {decibel:.2f} dB, Estimated Distance: {distance:.2f} units")


    pygame.draw.circle(screen, GREEN, CENTER, int(CIRCLE_RADIUS * fill_value))
    pygame.draw.circle(screen_2, GREEN, CENTER_2, int(0.235*CIRCLE_RADIUS * fill_value))
    pygame.draw.circle(screen_3, GREEN, CENTER_3, int(0.125*CIRCLE_RADIUS * fill_value))
    
    pygame.draw.circle(screen, GREEN,CENTER, CIRCLE_RADIUS, 1)
    pygame.draw.circle(screen_2, GREEN,CENTER_2, CIRCLE_RADIUS, 1)
    pygame.draw.circle(screen_3, GREEN,CENTER_3, CIRCLE_RADIUS, 1)
    
    pygame.draw.circle(screen, GREEN,CENTER, CIRCLE_RADIUS, 1)
    pygame.draw.circle(screen_2, GREEN,CENTER_2, CIRCLE_RADIUS, 1)
    pygame.draw.circle(screen_3, GREEN,CENTER_3, CIRCLE_RADIUS, 1)
    
    pygame.draw.circle(screen, GREEN,CENTER, CIRCLE_RADIUS//2, 1)
    pygame.draw.circle(screen_2, GREEN,CENTER_2, CIRCLE_RADIUS//2, 1)
    pygame.draw.circle(screen_3, GREEN,CENTER_3, CIRCLE_RADIUS//2, 1)
    
    pygame.draw.circle(screen, GREEN,CENTER, 1.5*CIRCLE_RADIUS, 1)
    
    pygame.draw.circle(screen, GREEN,CENTER, 2*CIRCLE_RADIUS, 1)
    pygame.draw.circle(screen_2, GREEN,CENTER_2, 0.25*CIRCLE_RADIUS, 1)
    pygame.draw.circle(screen_2, GREEN,CENTER_2, 0.75*CIRCLE_RADIUS, 1)
    pygame.draw.circle(screen_3, GREEN,CENTER_3, 0.25*CIRCLE_RADIUS, 1)
    pygame.draw.circle(screen_3, GREEN,CENTER_3, 0.75*CIRCLE_RADIUS, 1)
    
    pygame.draw.circle(screen, GREEN,CENTER, 2.6*CIRCLE_RADIUS, 1)
    
    
    elapsed_time = pygame.time.get_ticks() - start_time
    time_text = font.render(f"Time: {elapsed_time/1000:.1f} s", True, GREEN)
    screen.blit(time_text, (25, 380))  
    text_1 = font.render("___________", True, GREEN)
    screen.blit(text_1, (15, 380))
    text_2 = font.render("    Motions    ", True, GREEN)
    screen.blit(text_2, (5, 65))
    text_m = font.render("    Plane    ", True, GREEN)
    screen.blit(text_m, (5, 100))
    text_m = font.render("      ET XXXX    ", True, GREEN)
    screen.blit(text_m, (5, 120))
    text_m = font.render("    Rocket    ", True, GREEN)
    screen.blit(text_m, (5, 140))
    text_m = font.render("    Military    ", True, GREEN)
    screen.blit(text_m, (5, 160))
    text_m = font.render("    Unknown    ", True, GREEN)
    screen.blit(text_m, (5, 180))
    text_3 = font.render(" _________ ", True, GREEN)
    screen.blit(text_3, (15, 67))
    text = font.render("Radio Detection and Ranging Screen ", True, GREEN)
    screen.blit(text, (578, 10))  
    text_4 = font.render("Description...", True, GREEN)
    screen.blit(text_4, (5, 650))
    text_5 = font.render("____________________________", True, GREEN) 
    screen.blit(text_5, (1205, 80))
    text_6 = font.render("Signal Processing and Analysis", True, GREEN)
    screen.blit(text_6, (1205,70))
    text_7 = font.render("____________________________", True, GREEN)
    screen.blit(text_7, (1205, 40))
    text_8 = font.render("  Pressure of Object    ", True, GREEN)
    screen.blit(text_8, (1275,370))
    text_9 = font.render("  Frequency(MHz)    ", True, GREEN)
    screen.blit(text_9, (1275,650))
    text_10 = font.render("Fuel Amount = 00.000 units", True, GREEN)
    screen.blit(text_10, (25,500))
    text_11 = font.render("Altitude = 00.00 units", True, GREEN)
    screen.blit(text_11, (25,540))
    text_12 = font.render("Rocket Direction= 00.00i,00.00j,00.00k", True, GREEN)
    screen.blit(text_12, (25,580))
    text_13 = font.render("Trust Force = 00.00N", True, GREEN)
    screen.blit(text_13, (25,620))
    
    
    speed = font.render(f'Speed = {(distance/elapsed_time)*10000} m/s',True , GREEN)
    screen.blit(speed,(1050,730))
    speed = font.render(f'{(distance/elapsed_time)*1000}',True , GREEN)
    screen.blit(speed,(1135,700))
    Distance =font.render(f'Distance = {distance} m',True ,GREEN)
    screen.blit(Distance,(200,730))
    Distance =font.render(f'{distance}',True ,GREEN)
    screen.blit(Distance,(310,700))
    dicebel = font.render(f'Decibel = {decibel} dB',True , GREEN)
    screen.blit(dicebel,(600,730))
    dicebel = font.render(f'{decibel}',True , GREEN)
    screen.blit(dicebel,(700,700))
     
    pygame.display.flip()
    clock.tick(60)


stream.stop_stream()
stream.close()
audio.terminate()
pygame.quit()
