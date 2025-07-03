# range_sensor

Node ROS 2 (Python) pour capteur ultrason **HC-SR04** sur Raspberry Pi 5, utilisant `gpiozero`.

---

## ⚙️ Dépendances

- ROS 2 (Humble / Iron / Jazzy)
- Python 3.10+
- `gpiozero`

```bash
sudo apt install python3-gpiozero python3-rpi.gpio python3-pigpio
pip install gpiozero --break-system-packages
```

- `sensor_msgs`

---

## 🔌 Connexions GPIO (avec pont diviseur)

| HC-SR04 Pin | GPIO RPi 5     | Broche physique | Remarque                        |
|-------------|----------------|------------------|----------------------------------|
| VCC         | 5V             | Pin 2            | Ne pas utiliser 3.3V ❌          |
| GND         | GND            | Pin 6            | Masse commune                    |
| TRIG        | GPIO 23        | Pin 16           | Sortie de déclenchement          |
| ECHO        | GPIO 24 (via pont) | Pin 18       | Entrée protégée (5V abaissé)     |

---

## 🧰 Pont diviseur de tension

**But** : abaisser le signal 5V du capteur à ~3.3V compatible GPIO.

- **R1 = 1 kΩ** entre ECHO et GPIO
- **R2 = 2.2 kΩ** entre GPIO et GND

Montage :
```
ECHO HC-SR04 ---[ R1 = 1kΩ ]---+--- GPIO24
                               |
                           [ R2 = 2.2kΩ ]
                               |
                              GND
```

---

## 🖼️ Schéma visuel

![Schéma HC-SR04 sur Raspberry Pi 5](./A_schematic_digital_illustration_showcases_the_wir.png)

---

## 🚀 Lancer le node

```bash
ros2 run range_sensor range_node
```

---

## 📡 Topic ROS 2

Le node publie sur :

- `/ultrasonic_range` (`sensor_msgs/msg/Range`)

Champs :

- `range`: distance en mètres
- `radiation_type`: `ULTRASOUND`
- `min_range`: `0.02`
- `max_range`: `4.0`
- `field_of_view`: `0.26` (~15°)

---

## 🧪 Calibration (facultatif)

Si la mesure est sous-estimée :

```python
COEFF = 100 / mesuré  # ex: 100 / 91 ≈ 1.10
```

Puis applique :

```python
distance_cm = mesure_brute * COEFF
```

---

## 📁 Arborescence du package

```
range_sensor/
├── range_sensor/
│   ├── __init__.py
│   └── range_node.py
├── setup.py
├── package.xml
├── README.md
├── .gitignore
└── A_schematic_digital_illustration_showcases_the_wir.png
```
