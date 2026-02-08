<p style="display: flex; align-items: center;">
  <img src="../itc.png" alt="Institute Logo" style="float: left; width: 120px; margin-right: 20px;">
  <span style="font-family: Arial, sans-serif; line-height: 1.6;">
    <strong>Lab 13</strong><br/>
    <strong>Course:</strong> Networks System Design<br>
    <strong>Name:</strong> Do Davin<br>
    <strong>Student ID:</strong> P20230018<br>
    <strong>Instructor:</strong> Mr. Kuy Movsun<br>
  </span>
</p>
<hr style="border: 1px solid #ccc;">

<br/>

# Part 1: Infrastructure Mode & Connectivity

![alt text](image.png)

![alt text](image-1.png)

![alt text](image-2.png)

![alt text](image-3.png)

![alt text](image-4.png)

![alt text](image-5.png)

![alt text](image-6.png)

# Part 2: Analyzing Wireless Management Frames

![alt text](image-7.png)

![alt text](image-8.png)

![alt text](image-9.png)

# Part 3: Channel Management and Frequency Reuse

![alt text](image-10.png)

![alt text](image-11.png)

![alt text](image-12.png)

# Part 4: Implementing Layer 2 Security

![alt text](image-13.png)

![alt text](image-14.png)

![alt text](image-15.png)

![alt text](image-16.png)

## Questions:
1. Why do we use non-overlapping channels like 1, 6, and 11 in professional deployments?
2. What happened to the connection when you applied the MAC filter? Is this an effective
security measure on its own?
3. In Simulation Mode, what is the main difference you noticed between a "Beacon" frame
and an "Association" frame?
## Answers:
1. We don’t use non-overlapping channels (1, 6, and 11) in professional deployments because it prevent interference between adjacent access points. 2.4GHz channels
overlap, but these three have 25MHz separation so they don't interfere. Allows multiple
APs in same area without performance degradation.
2. When you applied the MAC filter, the router blocked the connection from laptop0 immediately while Laptop1 worked normally. It’s not an effective security measure on
its own because it easily bypass MAC spoofing.
3. **Beacon**:
        * AP -> Broadcast, periodic advertisements
        * ongoing advertisements
    **Association:**
        * Client -> Specific AP, connection request
        * one-time connection setup.